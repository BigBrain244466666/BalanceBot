# The Balancer

**Description**: This is a robot that can autonomously balance on two wheels while being controlled with regular movements (forward, backward, left, right) via Bluetooth on a computer.

**Why I did this project**: I found this project online when searching for good robotics challenges. It sounded fun because I had just seen things like hoverboards (those two-wheel boards that you can ride on) and thought it would be cool if I could make a miniature version of them. Of course, the design isn't the same, but it's the same concept.

**Description of Files**
My files may be a bit confusing, so I'm going to go through them.

CAD: This one's pretty straightforward; it's the entire build in a .step file.
PCB: Here is the main stuff. There are two schematics, one for the breakout boards and one to show the real wiring. The breakout board one exists as I am using non-SMD parts, and all the footprints I could find online are using SMD, so I used pads on the real PCB to connect them to the breakout boards. When referencing the wiring, please use the **Balance Bot - Real.kicad_sch** file. Also, the kicad_pro file only includes the PCB due for this reason, when looking at them, please open the schematics separately.
Production: Here are all my production files, including the top, middle, bottom, and motor holder .step files. Also included is the PCB gerber file.
Wiring: A Fritzing file is attached here to see the wiring of the motors and battery packs, as those wires are not included in the CAD file.
Firmware: Firmware was not included due to it being too dependent on the physical bot (measurements and calibrating the gyroscope).

![Image](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-07%20213608.png)
![Image](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-07%20213556.png)
![Image](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-07%20205014.png)
![Image](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-07%20005523.png)
![Image](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-07%20005739.png)

**BOM**
Will Update soon
