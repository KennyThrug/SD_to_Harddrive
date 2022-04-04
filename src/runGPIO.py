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

lcd = None
GPIO.setmode(GPIO.BCM)

#sets up LCD screen
def setupScreen():
    lcd = CharLCD(numbering_mode=GPIO.BCM,cols=16,rows=2,pin_rs=13,pin_e=6,pins_data=[5,19,26,23,12,16,20,21],auto_linebreaks=True,backlight_enabled=True)
    
#Writes a string to the LCD Screen
def writeString(message):
    global lcd
    if lcd == None:
        setupScreen()
    lcd.write_string(message)

#Sets up Button on specific GPIO port
def setupButton(buttonGPIO):
    GPIO.setup(buttonGPIO,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#Checks for a button press on a specific GPIO port
def checkForButton(buttonGPIO):
    return GPIO.input(buttonGPIO) == GPIO.HIGH