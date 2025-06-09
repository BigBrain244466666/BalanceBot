from machine import Pin, PWM, I2C
import math
import time

# -------------------------------
#       MPU6050 Driver (Basic)
# -------------------------------

class MPU6050:
    def __init__(self, i2c):
        self.i2c = i2c
        self.addr = 0x68  # Default MPU6050 address
        self.i2c.writeto(self.addr, b'\x6B\x00')  # Wake up MPU6050

    def get_raw_values(self):
        raw_bytes = self.i2c.readfrom_mem(self.addr, 0x3B, 14)
        return list(bytearray(raw_bytes))

    def get_values(self):
        raw = self.get_raw_values()
        ax, ay, az = [x / 16384.0 for x in twos_complement([raw[0], raw[1]], [raw[2], raw[3]], [raw[4], raw[5]])]
        gx, gy, gz = [x / 131.0 for x in twos_complement([raw[8], raw[9]], [raw[10], raw[11]], [raw[12], raw[13]])]
        return ax, ay, az, gx, gy, gz

def twos_complement(hi, lo, dummy=None):
    def to_int(h, l):
        val = (h << 8) + l
        return val - 65536 if val > 32767 else val
    return [to_int(hi[0], lo[0]), to_int(hi[1], lo[1]), to_int(hi[2], lo[2])]

# -------------------------------
#       PID Controller
# -------------------------------

class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.last_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value, dt):
        error = setpoint - measured_value
        self.integral += error * dt
        derivative = (error - self.last_error) / dt if dt > 0 else 0
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.last_error = error
        return output

# -------------------------------
#       Motor Control
# -------------------------------

class Motor:
    def __init__(self, pwm_pin, dir_pin):
        self.pwm = PWM(Pin(pwm_pin))
        self.pwm.freq(1000)  # Set frequency to 1kHz
        self.dir = Pin(dir_pin, Pin.OUT)

    def set_speed(self, speed):
        # Speed: -100 to 100
        if speed >= 0:
            self.dir.value(1)  # Forward
            self.pwm.duty_u16(int(speed / 100 * 65535))
        else:
            self.dir.value(0)  # Reverse
            self.pwm.duty_u16(int(-speed / 100 * 65535))

# -------------------------------
#       Main Program
# -------------------------------

# Initialize I2C and MPU6050
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
mpu = MPU6050(i2c)

# Motors
motor_left = Motor(2, 3)  # PWM: GP2, Direction: GP3
motor_right = Motor(4, 5)  # PWM: GP4, Direction: GP5

# PID Controller
pid = PID(Kp=50, Ki=0.1, Kd=1.0)

# Sensor Fusion Settings
alpha = 0.98  # Complementary filter coefficient
angle = 0.0
gyro_x_bias = 0.0
accel_y = 0.0

# Timing
last_time = time.ticks_ms()

print("Calibrating Gyro...")
for _ in range(100):  # Simple bias calibration
    _, _, _, gx, _, _ = mpu.get_values()
    gyro_x_bias += gx
    time.sleep(0.01)
gyro_x_bias /= 100
print(f"Gyro Bias: {gyro_x_bias}")

# Setpoint is 0 degrees (upright)
setpoint = 0.0

# -------------------------------
#       Main Loop
# -------------------------------

while True:
    current_time = time.ticks_ms()
    dt = (current_time - last_time) / 1000  # seconds
    last_time = current_time

    # Read sensor values
    ax, ay, az, gx, gy, gz = mpu.get_values()

    # Subtract gyro bias
    gx -= gyro_x_bias

    # Calculate angle from accelerometer
    acc_angle = math.atan2(ay, az) * 180 / math.pi  # In degrees

    # Integrate gyroscope
    angle = alpha * (angle + gx * dt) + (1 - alpha) * acc_angle

    # Run PID
    output = pid.compute(setpoint, angle, dt)

    # Limit output
    output = max(min(output, 100), -100)

    # Send to motors
    motor_left.set_speed(output)
    motor_right.set_speed(output)

    # Optional delay (depends on loop timing)
    time.sleep(0.01)
