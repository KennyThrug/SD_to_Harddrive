#Change the Following Values if you wish to change the GPIO Ports used

# Ground
# 5v
# Backlight (resistor into Ground)
RegSelect = 13
# Read/Write : Ground
Enable = 6
Data0 = 5 
Data1 = 19
Data2 = 26
Data3 = 23
Data4 = 12
Data5 = 16
Data6 = 20
Data7 = 21
# Backlight Anode (resister into 5v)
# Backlight Cathode (Ground)

from RPLCD import CharLCD
import RPi.GPIO as GPIO
from time import sleep

lcd = None
GPIO.setmode(GPIO.BCM)
CurMessage = ""
finalMessage = ""

def resetFinalMessage():
    global finalMessage
    finalMessage = ""

def setFinalMessage(strin):
    global finalMessage
    if finalMessage == "":
        finalMessage = strin

def outputFinalMessage():
    global finalMessage
    writeString(finalMessage)

#sets up LCD screen
def setupScreen():
    global Enable,RegSelect,Data0,Data1,Data2,Data3,Data4,Data5,Data6,Data7
    global lcd
    lcd = CharLCD(numbering_mode=GPIO.BCM,cols=16,rows=2,pin_rs=13,pin_e=Enable,pins_data=[Data0,Data1,Data2,Data3,Data4,Data5,Data6,Data7],auto_linebreaks=True,backlight_enabled=True)
    
#Writes a string to the LCD Screen
def writeString(message):
    global lcd
    global CurMessage
    if lcd == None:
        setupScreen()
    if not message == CurMessage:
        CurMessage = message
        lcd.clear()
        lcd.write_string(message)

#Sets up Button on specific GPIO port
def setupButton(buttonGPIO):
    GPIO.setup(buttonGPIO,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#Checks for a button press on a specific GPIO port
def checkForButton(buttonGPIO):
    return GPIO.input(buttonGPIO) == GPIO.HIGH
