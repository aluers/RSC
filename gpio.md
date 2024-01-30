sudo apt install python3-gpiozero

Gpiozero provides may different modules or "interfaces". You typically import the ones you use by name so you can refer to them with a short name.

from gpiozero import LED

to allow using the gpiozero.LED module and refer to it as "LED"

from gpiozero import LED, Button
Example

led = LED(1)
led = LED("GPIO1")
led = LED("BCM1")
led = LED("BOARD11")
led = LED("WPI0")
led = LED("J8:11")

For driving an output connected to an LED, for example, you use the LED module. You create an instance by passing the GPIO name.

#!/usr/bin/python3

from gpiozero import LED
from time import sleep

led = LED(24)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)


    https://www.ics.com/blog/control-raspberry-pi-gpio-pins-python
    https://raspberry-projects.com/pi/command-line/io-pins-command-line/io-pin-control-from-the-command-line
    https://projects.drogon.net/raspberry-pi/wiringpi/the-gpio-utility/
