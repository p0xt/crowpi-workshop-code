import datetime
import time
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import spidev
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,1)
spi.max_speed_hz=1000000
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2
# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)
# Turn backlight on
lcd.set_backlight(0)
symbols = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': '\'',
    '-.-.--': '!',
    '-..-.': '/',
    '-.--.': '(',
    '-.--.-': ')',
    '.-...': '&',
    '---...': ':',
    '-.-.-.': ';',
    '-...-': '=',
    '.-.-.': '+',
    '-....-': '-',
    '..--.-': '_',
    '.-..-.': '"',
    '...-..-': '$',
    '.--.-.': '@'
}
# define touch pin
touch_pin = 17
# define buzzer
buzzer_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(touch_pin, GPIO.IN)
def listToString(s):  
    # Function to convert list to string  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  
class ButtonMatrix():
    def __init__(self):
        # Define key channels
        self.key_channel = 4
        self.delay = 0.1
        self.adc_key_val = [30,90,160,230,280,330,400,470,530,590,650,720,780,840,890,960]
        self.key = -1
        self.oldkey = -1
        self.num_keys = 16
        self.indexes = {
            12:1,
            13:2,
            14:3,
            15:4,
            10:5,
            9:6,
            8:7,
            11:8,
            4:9,
            5:10,
            6:11,
            7:12,
            0:13,
            1:14,
            2:15,
            3:16
        }
    def ReadChannel(self,channel):
        # Function to read SPI data from MCP3008 chip
        # Channel must be an integer 0-7
        adc = spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data
    
    def GetAdcValue(self):
        adc_key_value = self.ReadChannel(self.key_channel)
        return adc_key_value
    def GetKeyNum(self,adc_key_value):
        for num in range(0,16):
            if adc_key_value < self.adc_key_val[num]:
                return num
        if adc_key_value >= self.num_keys:
            num = -1
            return num
    def activateButton(self, btnIndex):
        # get the index from SPI
        btnIndex = int(btnIndex)
        # correct the index to better format
        btnIndex = self.indexes[btnIndex]
        # return the button pressed
        return btnIndex
def calc_delta_in_sec(time1, time2):
    delta = time2 - time1
    return delta.seconds + (delta.microseconds / 1000000.0)
# initialize button matrix
buttons = ButtonMatrix()
# define state, press & release
last_edge = GPIO.LOW
press = datetime.datetime.now()
release = datetime.datetime.now()
# define sequence, letters, words
sequence = ""
letters = []
words = []
while True:
    # check if matrix button pressed
    adc_key_value = buttons.GetAdcValue()
    key = buttons.GetKeyNum(adc_key_value)
    if key != buttons.oldkey:
        time.sleep(0.1)
        adc_key_value = buttons.GetAdcValue()
        key = buttons.GetKeyNum(adc_key_value)
        if key != buttons.oldkey:
            oldkey = key
            if key >= 0:
                # button pressed
                button = buttons.activateButton(key)
                # button 13 is to confirm and translate morse to letters
                if(button == 13):
                    print("button pressed: %s" % button)
                    try:
                        letter = symbols[sequence]
                        letters.append(letter)
                        print("letter: %s" % letter)
                        # clear the sequence
                        sequence = ""
                        # write english sentence on LCD
                        lcd.clear()
                        lcd.message("English sentence:\n" + listToString(letters))
                        print("English sentence:\n" + listToString(letters))
                    except:
                        lcd.clear()
                        lcd.message("Unrecognized input!")
                        print("Unrecognized input!")
                        # clean the sequence
                        sequence = ""
                # button 14 is to clear the sentence
                if(button == 14):
                    letters = []
                    words = []
                    sequence = ""
                    # let us know that data cleared
                    lcd.clear()
                    lcd.message("Data cleaned!")
                    print("Data cleaned!")
                # button 15 is for space in the sentence
                if(button == 15):
                    letters.append(" ")
                    words.append(listToString(letters))
                    sequence = ""
                    # let us know that we added word to sentence
                    lcd.clear()
                    lcd.message("Added space!")
                    print("added space")
    # touch pressed - determine if start of new letter/word
    if GPIO.input(touch_pin) == GPIO.HIGH and last_edge == GPIO.LOW:
        
        GPIO.output(buzzer_pin, GPIO.HIGH)
        
        last_edge = GPIO.HIGH
        press = datetime.datetime.now()
    # Button released - determine what the input is
    elif GPIO.input(touch_pin) == GPIO.LOW and last_edge == GPIO.HIGH:
        
        GPIO.output(buzzer_pin, GPIO.LOW)
        
        last_edge = GPIO.LOW
        release = datetime.datetime.now()
        
        delta = calc_delta_in_sec(press, release)
        if(delta <= 0.3):
            sequence += '.'
            lcd.clear()
            lcd.message("Writing morse:\n" + sequence)
            print("Added dot to sequence: " + sequence)
        elif (delta >= 0.3):
            sequence += '-'
            lcd.clear()
            lcd.message("Writing morse:\n" + sequence)
            print("Added dash to sequence: " + sequence)