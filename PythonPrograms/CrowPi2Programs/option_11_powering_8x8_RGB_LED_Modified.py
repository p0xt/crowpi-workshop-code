import time
from rpi_ws281x import PixelStrip, Color
# LED strip configuration:
LED_COUNT = 64        # Number of LED pixels.
LED_PIN = 12          # GPIO pin connected to the pixels (18 uses $
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800$
LED_DMA = 10          # DMA channel to use for generating signal ($
LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN $
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
RIGHT_BORDER = [7,15,23,31,39,47,55,63]
LEFT_BORDER = [0,8,16,24,32,40,48,56]
# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 5000.0)
def colorWipe2(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        i+=32
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)
def theaterChase2(strip, color, wait_ms=50, iterations=3):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(2):
            for i in range(0, strip.numPixels(), 2):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 500.0)
            for i in range(0, strip.numPixels(), 2):
                strip.setPixelColor(i + q, 0)
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)
def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)
# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()
# start animation
print('Color wipe animations.')
colorWipe(strip, Color(255, 0, 0))  # Red wipe
colorWipe(strip, Color(0, 255, 0))  # Green wipe
colorWipe(strip, Color(0, 0, 255))  # Blue wipe
colorWipe(strip, Color(230, 230, 250))  # Lavender wipe
# start animation ColorWipe2
print('Color wipe 2.0 animations.')
colorWipe2(strip, Color(255, 0, 0))  # Red wipe
colorWipe2(strip, Color(0, 255, 0))  # Green wipe
print('Theater chase animations.')
theaterChase(strip, Color(127, 127, 127))  # White theater chase
theaterChase(strip, Color(127, 0, 0))  # Red theater chase
theaterChase(strip, Color(0, 0, 127))  # Blue theater chase
theaterChase(strip, Color(0, 255, 1))  # Green theater chase
print('Theater chase 2.0 animations.')
theaterChase2(strip, Color(127, 0, 0))  # Red theater chase
theaterChase2(strip, Color(127, 127, 127))  # White theater chase
theaterChase2(strip, Color(0, 0, 127))  # Blue theater chase
print('Rainbow animations.')
rainbow(strip)
print('Wipe LEDs')
colorWipe(strip, Color(0, 0, 0), 10)