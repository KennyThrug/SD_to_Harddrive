import moveFiles
import runGPIO
import blinkLights
import os

if __name__ == '__main__':
    runGPIO.setupButton(24)
    while True:
        if runGPIO.checkForButton(24):
            runGPIO.writeString("Secret Message\r\n---- ---->")
        else:
            runGPIO.writeString("Press The Button\r\nOr Don't")
