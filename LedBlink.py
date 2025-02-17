import gpiozero
import time
import sys

led = gpiozero.LED(17)
print("Program Starting...")
while True:
    try:
        led.on()
        print("The led is on")
        time.sleep(1)
        led.off()
        time.sleep(1)
        print("The led is off")
    except KeyboardInterrupt:
        print("Program Ending...")
        sys.exit()