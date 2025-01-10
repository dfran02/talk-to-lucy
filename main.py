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



# constants
lcd_columns = 16
lcd_rows = 2

# gpio pin assignment
lcd_rs = DigitalInOut(board.D4)
lcd_en = DigitalInOut(board.D17)
lcd_d4 = DigitalInOut(board.D27)
lcd_d5 = DigitalInOut(board.D22)
lcd_d6 = DigitalInOut(board.D25)
lcd_d7 = DigitalInOut(board.D24)

# btn_1 = DigitalInOut(board.D14)
# btn_1.direction = Direction.INPUT
# btn_1.pull = Pull.DOWN

# btn_2 = DigitalInOut(board.D15)
# btn_2.direction = Direction.INPUT
# btn_2.pull = Pull.DOWN

# btn_3 = DigitalInOut(board.D18)
# btn_3.direction = Direction.INPUT
# btn_3.pull = Pull.DOWN

# btn_yel = DigitalInOut(board.D7)
# btn_yel.direction = Direction.INPUT
# btn_yel.pull = Pull.DOWN

relay_1 = OutputDevice(23) 

# potentiometer = analogio.AnalogIn(board.D7)

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

l_yel = LED(8)
l_yel.on()

test = path.join(path.dirname(__file__), 'assets', "imhungry.mp3")
test2 = path.join(path.dirname(__file__), 'assets', "wannagoout.mp3")

# pygame.mixer.init()
# sound_1 = pygame.mixer.Sound('./assets/imhungry.mp3')
# sound_2 = pygame.mixer.Sound('./assets/wannagoout.mp3')
# sound_1 = pygame.mixer.Sound(test)
# sound_2 = pygame.mixer.Sound(test2)
# sound_1 = pygame.mixer.music.load(test)
# sound_2 = pygame.mixer.music.load(test2)


def squirt_them_squirrels():

    # play a sound
    # blink the light
    # panel status = "busy" (prevents addl button presses)

    # lcd message "squirt them squirrels"
    # lcd message "3...2...1..."

    # lcd message "turning on water"
    # relay open valve
    # count down 5 seconds or whatever
    # relay close value

    # lcd message "squirt complete"
    
    # reset panel status to "ready"





    print("squirt them squerrls")

    # todo: this isn't working
    # pygame.init()
    # filepath = path.join(path.dirname(__file__), 'assets', "imhungry.mp3")
    pygame.mixer.music.load("./assets/imhungry.mp3")
    pygame.mixer.music.play()
    sleep(20)
    pygame.mixer.music.stop()
    

    return
    # lcd_line_1 = "squirrels!!!"
    # lcd_line_2 = "here we go!"
    # lcd.message = lcd_line_1 + lcd_line_2
    # print("squirt them squirrels!\n")

    # relay_1.on()
    # sleep(5)
    # relay_1.off()
    # return

def lucy_wants_to_eat():
    print("lucy wants to eat")
    # lcd_line_2 = "Lucy is HUNGRY!!"
    # lcd.message = lcd_line_2 + lcd_line_2
    # print("lucy wants to eat\n")
    # return

def lucy_wants_to_go_out():
    print("lucy wants out")
    # lcd_line_1 = "OUT! OUT! OUT!"
    # lcd.message = lcd_line_1 + lcd_line_2
    # print("lucy wants to go out\n")
    # return

def button_press(led):
    led.on()
    print("press")
    return

def button_release(led):
    led.off()
    print("release")
    return

def button_hold(led, button):
    print("hold")

    led.blink(0.25, 0.25, 10, True)

    # do a switch on the button to define which method to exec
    if (button.pin == 18):
        squirt_them_squirrels

    return


lcd.clear()

lcd_line_1 = "initializing...."
lcd.message = lcd_line_1

relay_1.on()
l_yel.on()
sleep(0.5)
relay_1.off()
l_yel.off()
sleep(0.5)
relay_1.on()
l_yel.on()
sleep(0.5)
relay_1.off()
l_yel.off()

lcd.clear()

try:
    pygame.init()
    # btn_1 = Button(14)

    b_yel = Button(18, hold_time=0.25)
    b_yel.when_pressed = button_press
    # b_yel.when_held = button_hold(l_yel, b_yel)
    b_yel.when_held = button_hold
    b_yel.when_released = button_release

except KeyboardInterrupt:
    print("bye bye!")
    pause()
except Exception as ex:
    print("some error happened: ", ex)
    pause()
finally:
    print("good bye!")
    pygame.quit()







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


