from gpiozero import LED, Button # This offers lgpio to use
from signal import pause
from subprocess import check_call
import os
import time

def reboot():
    print("I will reboot")
    time.sleep(1)
    led.off()
    check_call(['sudo', 'reboot'])

led = LED(17)
led.on()
reboot_btn = Button(27,hold_time=1)
reboot_btn.when_held = reboot

pause()