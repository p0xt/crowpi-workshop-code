import time
import Adafruit_CharLCD as LCD
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2
# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)
# Turn backlight on
lcd.set_backlight(0)
# Print a two line message
lcd.message('Hello World!... \n...I said Hello!')
# Wait 5 seconds
time.sleep(5.0)
# Demo showing the cursor.
lcd.clear()
lcd.show_cursor(True)
lcd.message('Show cursor')
time.sleep(5.0)
# Demo showing the blinking cursor.
lcd.clear()
lcd.blink(True)
lcd.message('Blink cursor')
time.sleep(5.0)
# Stop blinking and showing cursor.
lcd.show_cursor(False)
lcd.blink(False)
# Demo scrolling message right/left.
lcd.clear()
message = 'Scrolling!'
lcd.message(message)
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_right()
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_left()
# Turn backlight off.
time.sleep(2)
lcd.clear()
#lcd.set_backlight(1)
# Demo scrolling message right/left.
lcd.clear()
message = '(:Goodbye:)'
lcd.message(message)
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_right()
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_left()
# Turn backlight off.
time.sleep(2)