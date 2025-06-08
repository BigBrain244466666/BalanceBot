---
Title: BalanceBot
Author: Victor Jiao
Description: A robot that balances on two wheels autonomously and can be controlled through Bluetooth.
Created At: 2025-05-31
---

# June 4th: Designed and made the Schematic!

It's been a few days since I created this project. I was busy the past few days, so no work was done. I was able to lock in today and finish designing the breadboard circuit, giving me an idea of what the robot will be like. I used Fritzing to make the diagram, and it's helping me visualize what the circuits, schematic, and PCB will be.

![Breadboard Diagram](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Screenshot%202025-06-04%20222751.png)

This technically should not have taken this long, but I spent a long time trying to find the perfect parts. Since this was a Bluetooth-controlled car, I didn't want to get a microcontroller with a separate Bluetooth module, nor did I want to get an extremely bulky one, so I settled with an ESP32 Wroom 32. It is small, powerful, and has Bluetooth, making it perfect for my car.

![ESP32](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/ESP32.png)

I also spent time learning how to import components into Fritzing (I'm kind of new to this). It worked out in the end, but boy was it a tough journey. I couldn't find much help online, so I had to resort to the AI to teach me...

Finally, with the breadboard circuit sorted out, I finished the breadboard. It was much easier than the first time (when I made my Macropad, learning how to use Kicad for the first time). I knew how the software worked, and I could easily import new symbols. It felt awesome!

![Schematic](https://github.com/BigBrain244466666/BalanceBot/blob/main/Images/Balance%20Bot%20-%20Breadboard%20Circuit%20-%20Draft%202.png)

Overall, I think today was an extremely productive day. I even worked a bit during the Zoom meeting! Hope tomorrow will be as productive as today. :)

Edit: Tomorrow, I need to change the ESP32 version to 32U. I can't find anywhere that sells the other one.

**Total time spent: 4h**



# June 5th: So many problems!!

I forgot to journal yesterday, so I'm catching up right now. 

Oh my gosh, why can't things just work properly?? Originally, I planned to use the ESP32, but I couldn't find a good version of it that fitted everything, so after many different tries with different microcontrollers, I finally settled on the Raspberry Pi Pico W, cheap, powerful, and effective. I also had to change my gyroscope, as I couldn't find a good place to buy it; it's still the same module, but the Adafruit version of it. I was able to finally save the breadboard and start on the PCB.

IMAGE HERE

I hate footprints. Every footprint I find is for the SMD version. Like, come on! I need the breakout board version! So I spent so long trying to find a way to make it work. No luck. In the end, I had to physically trace out the pads and place the breakout board myself; it was very tedious. But after many hardships, I finished the PCB. It's simple, but it gets the job done. I'm very proud of it. (It is my first custom PCB...)

IMAGE HERE

Finally, I spent some time working on the CAD. I made the bottom of my robot and the prongs that would hold the motors. I'm starting to get used to the weird controls of Fusion 360, and I think my robots are coming together really well!

That's about it for today (technically yesterday...), I will update soon again!

**Total time spent: 4.5h**


# June 6th: Finally Done!

Today I finally finished everything. It took a lot of troubleshooting to get the CAD correct, but in the end it worked. The problems first started when I got the wrong PCB measurements, so I had to redo the entire base of the CAD. Next, when I was adding in the electronics, I realized that the actual CAD for the motor driver and the gyroscope didn't exist, so I had to use Adafruit's PCB file and export it as a .step file instead. It took a lot of tries to align the holes of the components and the pads of the PCB, as there wasn't any defined measurement. It worked in the end, but I did have to change the PCB.

IMAGE HERE

When I started adding the battery packs, I realized that they were way too big, so I had to readjust the entire build again, now making the frame much bigger and taller to accommodate the battery packs. I designed a 3-layer case, one to hold the batteries, one to hold the electronics and one for the top cover. I also designed some cool motor holders that should hold the motor pretty easily.

IMAGE HERE

Today was a productive day, I got lots of things done. I should be able to submit tomorrow!

**Total time spent: 3h**

# June 7th: Submitted!

I learned a lot about GitHub today. I'm pretty new to GitHub, so when I uploaded my full CAD file of 27.5MB, you could say I was surprised to see the size was too big. I then spend lots of time (and lots of AI) trying to figure out how to upload a large file to GitHub. I ended up installing Git Bash and LFS to upload the file to my offline files, then learning how to push it back to my online version. It was a lot of trial and error.

Other than that, I just spent most of my time downloading all the necessary files.

**Total time spent: 2h**
