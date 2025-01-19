from subprocess import Popen, PIPE 
from time import sleep, perf_counter 
from signal import pause
from datetime import datetime 
from gpiozero import OutputDevice, Button, LED
from digitalio import DigitalInOut, Direction, Pull
from os import path
import board 
import adafruit_character_lcd.character_lcd as characterlcd 
import pygame
from enum import Enum

# constants
HOLD_TIME = 0.25
LCD_COLUMNS = 16
LCD_ROWS = 2

class Status(Enum):
    INITIALIZING = 0
    READY = 1
    WORKING = 2

# globals
SYSTEM_STATUS = Enum('Status', 'INITIALIZING') 

y
# switch_1 = create_switch()    todo: figure out how to wire, use as relay disconnect


def display_message(line_1):
    # we can create a system.status enum (0 Initialization, 1 Ready, 2 Working) and write line 1 without requiring line_1 parameter
    lcd.clear()
    lcd.message = SYSTEM_STATUS + lcd_line_2
    return

def create_button(pin, hold_action):
    button = Button(pin, hold_time=HOLD_TIME)
    button.when_pressed = button_press
    button.when_held = hold_action
    button.when_released = button_release

    return button

def init_sounds(file_path):
    # really just want a single file initializer here (init_sound)
    # we need to refer to and call the method in a not-dumb way. maybe an action' enum (0 squirrel, 1 food, 2 out, etc)
    # or a tuple (0 squirrel squirrel.wav, 1 food lucy_food.wav, etc)
    pygame.init()
    
    sound_0 = pygame.mixer.Sound(path.join(path.dirname(__file__), 'assets', 'system_test.wav'))
    sound_0.set_volume(1)
    sound_1 = pygame.mixer.Sound(path.join(path.dirname(__file__), 'assets', 'lucy_food.wav'))
    sound_1.set_volume(1)
    sound_2 = pygame.mixer.Sound(path.join(path.dirname(__file__), 'assets', 'lucy_out.wav'))
    sound_2.set_volume(1)

    pygame.mixer.Sound.play(sound_0)

    return


def squirt_them_squirrels():
    print("squirt them squerrls")
    return

def lucy_wants_to_eat():
    print("lucy wants to eat")
    pygame.mixer.Sound.play(sound_1)
    return

def lucy_wants_to_go_out():
    print("lucy wants out")
    pygame.mixer.Sound.play(sound_2)
    return

def button_press(button):
    print("press")
    return

def button_release(button):
    print("release")
    return

def button_hold(button):
    print("hold")
    # led.blink(0.25, 0.25, 10, True)

    # do a switch on the button to define which method to exec
    if button.pin.number == 14:
        print("button.pin: ", button.pin.number)
        squirt_them_squirrels()

    return


try:
    # -> system_initialize()
    lcd = characterlcd.Character_LCD_Mono(DigitalInOut(board.D4), DigitalInOut(board.D17), DigitalInOut(board.D27), DigitalInOut(board.D22), DigitalInOut(board.D25), DigitalInOut(board.D24), LCD_COLUMNS, LCD_ROWS)
    relay_1 = OutputDevice(23) 
    led_r = LED(7)
    led_b = LED(8)
    led_y = LED(15)

    display_message('Initializing','Please wait...')

    btn_b = create_button(18, squirt_them_squirrels)
    btn_y = create_button(14, lucy_wants_to_go_out)
    btn_r = create_button(11, lucy_wants_to_eat)
    pygame.init()

    #led_b.blink(0.2,0.2,100,background=False)
    #sleep(0.1)
    #led_y.blink(0.2,0.2,100,background=True)
    #sleep(0.1)
    #led_r.blink(0.2,0.2,100,background=True)
    #sleep(0.1)

    display_message('Initializing','Relay test...')

    relay_1.on()
    sleep(0.5)
    relay_1.off()
    sleep(0.5)
    relay_1.on()
    sleep(0.5)
    relay_1.off()

    display_message('Initializing','Light test...')
    sleep(0.5)
    display_message('Initializing','Yellow:')
    led_y.blink(0.1,0.1,10,background=False)
    display_message('Initializing','Blue:')
    led_b.blink(0.1,0.1,10,background=False)
    display_message('Initializing','Red:')
    led_r.blink(0.1,0.1,10,background=False)

    display_message('Initializing','Sound test...')

    init_sounds()

    display_message('Initializing','Finalizing...')
    sleep(1)    # tricky!
    display_message('Ready!','')
    sleep(1)
    display_message('datetime','Armed')

    input('loaded!')

except KeyboardInterrupt:
    print("bye bye!")
except Exception as ex:
    print("some error happened: ", ex)
    pause()
finally:
    print("good bye!, lol: ", lol)
    pygame.quit()
    raw_input("wait")







# main loop:
# while True:
#     if btn_1.value == True:
#         squirt_them_squirrels()

#     if btn_2.value == True:
#         lucy_wants_to_eat()

#     if btn_3.value == True:
#         lucy_wants_to_go_out()

#     # lcd_line_1 = "y: " + str(btn_yel.value)  + " 1: " +  str(btn_1.value)
#     # lcd_line_2 = "2: " + str(btn_2.value) + " 3: " + str(btn_3.value)
#     lcd_line_1 = "volume:"
#     lcd_line_2 = potentiometer.value + "%"

#     lcd.message = lcd_line_1 + "\n" + lcd_line_2
#     # print(lcd_line_1 + " " + lcd_line_2)
    
#     sleep(0.25)
#     lcd.clear()


# looking for an active Ethernet or WiFi device
def find_interface():
#    dev_name = 0 # sets dev_name so that function does not return Null and crash code
    find_device = "ip addr show"
    interface_parse = run_cmd(find_device)
    for line in interface_parse.splitlines():
        if "state UP" in line:
            dev_name = line.split(':')[1]
            return dev_name
    return 1 # avoids returning Null if "state UP" doesn't exist

# find an active IP on the first LIVE network device
def parse_ip():
    if interface == 1: # if true, no device is in "state UP", skip IP check
        return "not assigned " # display "IP not assigned"
    ip = "0"
    find_ip = "ip addr show %s" % interface
    ip_parse = run_cmd(find_ip)
    for line in ip_parse.splitlines():
        if "inet " in line:
            ip = line.split(' ')[5]
            ip = ip.split('/')[0]
            return ip # returns IP address, if found
    return "pending      " # display "IP pending" when "state UP", but no IPv4 address yet

# run unix shell command, return as ASCII
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output.decode('ascii')

# wipe LCD screen before we start
#lcd.clear()


# before we start the main loop - detect active network device and ip address
# set timer to = perf_counter(), for later use in IP update check
#interface = find_interface()
#ip_address = parse_ip()
#timer = perf_counter()

#GPIO.cleanup()

#lcd_line_1 = datetime.now().strftime('%b %d  %H:%M:%S\n')
#lcd_line_2 = "ready :)"
#lcd.message = lcd_line_1 + lcd_line_2

# while True:
    # check for new IP addresses, at a slower rate than updating the clock
#    if perf_counter() - timer >= 15:
#        interface = find_interface()
#        ip_address = parse_ip()
#        timer = perf_counter()


