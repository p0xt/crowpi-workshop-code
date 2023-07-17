import time
import RPi.GPIO as GPIO
from rpi_ws281x import PixelStrip, Color
import random
# LED strip configuration:
LED_COUNT = 64        # Number of LED pixels.
LED_PIN = 12          # GPIO pin connected to the pixels (18 uses $
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800$
LED_DMA = 10          # DMA channel to use for generating signal ($
LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN $
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
# define touch pin
touch_pin = 17
# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)
# set GPIO pin to INPUT
GPIO.setup(touch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Define functions which animate LEDs in various ways.
def colorWipe(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()
# create colors sequence: red, green, blue:
color_sequence = [Color(255,0,0),Color(0,255,0),Color(0,0,255)]
while True:
    random_color = random.choice(color_sequence)
    # check if touch detected
    if(GPIO.input(touch_pin)):
        print('Touch Detected')
        colorWipe(strip, random_color)
    time.sleep(0.1)