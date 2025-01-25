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
import sys


class Status(Enum):
    INITIALIZING = 0
    ARMED = 1
    WORKING = 2

def display_message(line_2):
    lcd.clear()
    lcd.message = SYSTEM_STATUS.name + '\n' + line_2
    return

def create_button(pin, hold_action):
    button = Button(pin, hold_time=HOLD_TIME)
    button.when_pressed = button_press
    button.when_held = hold_action
    button.when_released = button_release

    return button

def squirt_them_squirrels():
    relay_valve.on()
    sleep(0.5)
    relay_valve.off()
    sleep(0.5)
    relay_valve.on()
    sleep(0.5)
    relay_value.off()
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
    HOLD_TIME = 0.25
    LCD_COLUMNS = 16
    LCD_ROWS = 2
    sound_1 = None
    sound_2 = None
    sound_3 = None

    SYSTEM_STATUS = Status.INITIALIZING

    # -> system_initialize()
    pygame.init()
    pygame.mixer.init()

    lcd = characterlcd.Character_LCD_Mono(DigitalInOut(board.D4), DigitalInOut(board.D17), DigitalInOut(board.D27), DigitalInOut(board.D22), DigitalInOut(board.D25), DigitalInOut(board.D24), LCD_COLUMNS, LCD_ROWS)

    display_message('Initializing...')

    relay_valve = OutputDevice(9)
    relay_bell = OutputDevice(23)

    led_r = LED(7)
    led_b = LED(8)
    led_y = LED(15)

    btn_b = create_button(18, squirt_them_squirrels)
    btn_y = create_button(14, lucy_wants_to_go_out)
    btn_r = create_button(11, lucy_wants_to_eat)

    sound_1 = pygame.mixer.Sound(path.join(path.dirname(__file__), 'assets', 'lucy_food.wav'))
    sound_2 = pygame.mixer.Sound(path.join(path.dirname(__file__), 'assets', 'lucy_out.wav'))
    sound_3 = pygame.mixer.Sound(path.join(path.dirname(__file__), 'assets', 'A3.wav'))

    display_message('Relay test...')

    x = False
    y = 0
    while y < 3:
        sleep(2)
        if  x == True:
             relay_valve.off()
             relay_bell.off()
        else:
             relay_valve.on()
             relay_bell.on()
        x = not x
        y += 1

    display_message('Light test...')

    led_y.blink(0.1,0.1,10,background=False)
    led_b.blink(0.1,0.1,10,background=False)
    led_r.blink(0.1,0.1,10,background=False)
    sleep(0.5)
    led_y.on()
    led_b.on()
    led_r.on()
    sleep(0.5)
    led_y.off()
    led_b.off()
    led_r.off()
    sleep(0.5)
    led_y.on()
    led_b.on()
    led_r.on()
    sleep(0.5)
    led_y.off()
    led_b.off()
    led_r.off()

    display_message('Sound test...')

    pygame.mixer.Sound.play(sound_3, loops=3)

    display_message('Finalizing...')
    sleep(3)    # pause for dramatic effect
    display_message('Ready!')
    sleep(1)

    SYSTEM_STATUS = Status.ARMED

    display_message(datetime.now().strftime('%b %d  %H:%M:%S\n'))

    # input('Armed')
    k = input('Armed.')
except KeyboardInterrupt:
    k = input("quitter!")
except Exception as ex:
    k = input("some error happened: " + str(ex))
finally:
    pygame.quit()
    print("bye! " + k)
    sleep(3)
    sys.exit()
