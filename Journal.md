---
Title: BalanceBot
Author: Victor Jiao
Description: A robot that balances on two wheels autonomously and can be controlled through Bluetooth.
Created At: 2025-05-31
---

# June 4th: Designed and made the Schematic!

It's been a few days since I created this project. I was busy the past few days, so no work was done. I was able to lock in today and finish designing the breadboard circuit, giving me an idea of what the robot will be like. I used Fritzing to make the diagram, and it's helping me visualize what the circuits, schematic, and PCB will be.

![Breadboard Diagram](https://github.com/BigBrain244466666/BalanceBot/blob/main/Balance%20Bot/Images/Screenshot%202025-06-04%20222751.png)

This technically should not have taken this long, but I spent a long time trying to find the perfect parts. Since this was a Bluetooth-controlled car, I didn't want to get a microcontroller with a separate Bluetooth module, nor did I want to get an extremely bulky one, so I settled with an ESP32 Wroom 32. It is small, powerful, and has Bluetooth, making it perfect for my car.

![ESP32](https://github.com/BigBrain244466666/BalanceBot/blob/main/Balance%20Bot/Images/ESP32.png)

I also spent time learning how to import components into Fritzing (I'm kind of new to this). It worked out in the end, but boy was it a tough journey. I couldn't find much help online, so I had to resort to the AI to teach me...

Finally, with the breadboard circuit sorted out, I finished the breadboard. It was much easier than the first time (when I made my Macropad, learning how to use Kicad for the first time). I knew how the software worked, and I could easily import new symbols. It felt awesome!

![Schematic](https://github.com/BigBrain244466666/BalanceBot/blob/main/Balance%20Bot/Images/Balance%20Bot%20-%20Breadboard%20Circuit%20-%20Draft%202.png)

Overall, I think today was an extremely productive day. I even worked a bit during the Zoom meeting! Hope tomorrow will be as productive as today. :)

Edit: Tomorrow, I need to change the ESP32 version to 32U. I can't find anywhere that sells the other one.

**Total time spent: 4h**



# June 5th: So many problems!!

I forgot to journal yesterday, so I'm catching up right now. 

Oh my gosh, why does can't things just work properly?? Originally, I planned to use the ESP32, but I couldn't find a good version of it that fitted eveyrhting, so after many different trys with differnt microcontrollers, I finally settled on the Raspberry Pi Pico W, cheap, powerful, and effective. I also had to change my gyroscope, as I couln't find a good place to buy it, its now still the same module, but the Adafruit version of it. I was able to finally save the breadboard and start on the PCB.

IMAGE HERE

I hate footprints. Every footprint I find is for the SMD version. Like, come on! I need the breakout board version! So I spent so long trying to find a way to make it work. No luck. In the end, I had to physically trace out the pads and place the breakout board myself; it was very tedious. But after many hardships, I finished the PCB. It's simple, but it gets the job done. I'm very proud of it. (It is my first custom PCB...)

IMAGE HERE

Finally, I spent some time working on the CAD. I made the bottom of my robot and the prongs that would hold the motors. I'm starting to get used to the weird controls of Fusion 360, and I think my robots are coming together really well!

IMAGE HERE

That's about it for today (technically yesterday...), I will update soon again!

**Total time spent: 4.5h**
