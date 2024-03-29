import RPi.GPIO as GPIO
import time
buzzer_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
# Make buzzer sound
GPIO.output(buzzer_pin, GPIO.HIGH)
time.sleep(0.5)
# Stop buzzer sound
GPIO.output(buzzer_pin, GPIO.LOW)
GPIO.cleanup()