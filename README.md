# raspi_sousevide
Controlling a slow cooker to make a homebrew sous vide

Parts Required

Raspberry Pi
Any variant will do.  You need GPIO, so if you got a Zero, get that solding iron out.  Make sure you can connect to it over a network, because you won't be able to use a TTY with the Pi-Mote attached.  I'm also including power, wifi/ethernet/SD card etc in this.

Thermocouple and thermocouple amplifier

Energenie Pi-Mote and a compatible socket

GPIO Splitter (maybe)

If you have an older, 26-pin Pi, you might need a splitter to connect the Pi-Mote and the thermocouple at the same time. The Pi-Mote has a 26-pin connector, but doesn't use all of the GPIO lines available. There are enough pins unused that you can attach the termocouple and the Pi-Mote to a single Pi at the same time. To to this, you either need a splitter (like this one), or if you have the soldering skills, you could replace the 26-pin connector on the Pi-Mote with a pass-through connector

If you have a 40-pin Pi, you will probably be able to attach the Pi-Mote and still have enough room at the end for the thermocouple. Be careful to not bend any pins though! If you're not sure, you can get splitters (like this one) for 40-pin boards

Case and connectors (optional)

It's probably a good idea to put all of the above into an enclosure of some kind, especially as you'll have it next to a pot of water. It doesnt have to be anything fancy. A tupperware or cliplok will do the job. Poke some holes for power and thermocouple cables, and add some playdoh for rustic sealing.  If you do want to go fancy, get a nice box and some panel-mount connectors for the USB power and thermocouple connections and attach them to the enclosure.

Setup



Pictures

Software

Rasp

Cooking

http://www.seriouseats.com/2015/06/food-lab-complete-guide-to-sous-vide-steak.html#tempchart1


