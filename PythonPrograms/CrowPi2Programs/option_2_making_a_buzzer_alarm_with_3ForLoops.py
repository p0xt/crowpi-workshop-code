import RPi.GPIO as GPIO
import time

buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

# While Loop to repeat the buzzing sound
#while True:
# For Loop to repeat the buzzing sound a certain amount of times
for i in range(2):
    # Make buzzer sound
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(0.5)
    
    # Stop buzzer sound
    GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(0.5)

for i in range(3):
    # Make buzzer sound
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(0.25)
    
    # Stop buzzer sound
    GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(0.25)

for i in range(4):
    # Make buzzer sound
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(0.1)
    
    # Stop buzzer sound
    GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(0.1)
# Clean up GPIO
GPIO.cleanup()
