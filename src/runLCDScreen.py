# Ground
# 5v
# Backlight (resistor into Ground)
# Register Select: GPIO 13
# Enable: GPIO 6
# Data 0: GPIO 5 
# Data 1: GPIO 19
# Data 2: GPIO 26
# Data 3: GPIO 23
# Data 4: GPIO 12
# Data 5: GPIO 16
# Data 6: GPIO 20
# Data 7: GPIO 21
# Backlight Anode (resister into 5v)
# Backlight Cathode (Ground)

from RPLCD import CharLCD
import RPi.GPIO as GPIO
from time import sleep

def setupScreen():
    #GPIO.setmode(GPIO.BCM)
    lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16,rows=2,pin_rs=33,pin_e=31,pins_data=[29,35,37,16,32,36,38,40],auto_linebreaks=True,backlight_enabled=True)
    lcd.write_string(u'Hi Gabe\r\nLCD screens suck')