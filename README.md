# The Balancer

**Description**: This is a robot that can autonomously balance on two wheels while being controlled with regular movements (forward, backward, left, right) via Bluetooth on a computer.

**Why I did this project**: I found this project online when searching for good robotics challenges. It sounded fun because I had just seen things like hoverboards (those two-wheel boards that you can ride on) and thought it would be cool if I could make a miniature version of them. Of course, the design isn't the same, but it's the same concept.

**Description of Files**
My files may be a bit confusing, so I'm going to go through them.

- CAD: This one's pretty straightforward; it's the entire build in a .step file.
- PCB: Here is the main stuff. There are two schematics, one for the breakout boards and one to show the real wiring. The breakout board one exists as I am using non-SMD parts, and all the footprints I could find online are using SMD, so I used pads on the real PCB to connect them to the breakout boards. When referencing the wiring, please use the **Balance Bot - Real.kicad_sch** file. Also, the kicad_pro file only includes the PCB due for this reason, when looking at them, please open the schematics separately.
- Production: Here are all my production files, including the top, middle, bottom, and motor holder step files. Also included is the PCB gerber file.
- Wiring: A Fritzing file is attached here to see the wiring of the motors and battery packs, as those wires are not included in the CAD file.
- Firmware: Firmware was not included due to it being too dependent on the physical bot (measurements and calibrating the gyroscope).

![Image](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-07%20213608.png)
![Image](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-07%20213556.png)
![Image](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-07%20205014.png)
![Image](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-07%20005523.png)
![Image](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-07%20005739.png)

**BOM**


Item # |	Part Name	Quantity |	Description |	Source |	Cost
---
1 |	Raspberry Pi Pico W |	1 |	Microcontroller |	AliExpress |	15.37
2 |	DRV8833 |	1 |	Motor Driver |	AdaFruit |	5.95
3 |	Mpu6040 |	1 |	Gyroscope |	AdaFruit |	12.95
4 |	Motor and Wheels |	1 |	Kit |	Temu |	10
5 |	PCB |	5 |	Pack |	PCBWay | 5
6 |	Chassis |	1 |	Bottom, 191 g |	Waterloo Public Library |	6
7 |	Chassis |	1 |	Middle, 100 g |	Waterloo Public Library |	4
8 |	Chassis |	1 |	Top, 40 g |	Waterloo Public Library |	2
9 |	Chassis |	8 |	Motor Holder, 0.74 g |	Waterloo Public Library |	1
10 |	Screws, M3 |	1 |	25 Pc |	AliExpress |	4.39
11 | Bolts, M3 |	1 |	25 Pc | AliExpress |	2.71
12 |	Googly Eyes |	1 |	10 Pc |	AliExpress |	3.47
13 |	Batteries |	2 |	4 and 2 AA holder |	AliExpress |	5
14 | Shipping | N/A |	N/A |	N/A |	20-40

