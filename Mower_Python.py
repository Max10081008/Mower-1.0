import keyboard  # using module keyboard
#import RPi.GPIO as GPIO         # using Rpi.GPIO module
from time import sleep          # import function sleep for delay
#GPIO.setmode(GPIO.BCM)          # GPIO numbering
#GPIO.setwarnings(False)         # enable warning from GPIO
AN2 = 13                # set pwm2 pin on MD10-Hat
AN1 = 12                # set pwm1 pin on MD10-hat
DIG2 = 24               # set dir2 pin on MD10-Hat
DIG1 = 26               # set dir1 pin on MD10-Hat
PROP = 14              # set pin to control propellor
#GPIO.setup(AN2, GPIO.OUT)       # set pin as output
#GPIO.setup(AN1, GPIO.OUT)       # set pin as output
#GPIO.setup(DIG2, GPIO.OUT)      # set pin as output
#GPIO.setup(DIG1, GPIO.OUT)      # set pin as output
sleep(1.75)             # delay for 1.75 seconds
#p1 = GPIO.PWM(AN1, 100)         # set pwm for M1
#p2 = GPIO.PWM(AN2, 100)         # set pwm for M2
global PropOn
Speed = 50
PropOn = False
print('Controls\n--------\nForward: W\nBack: S\nTurn Left: A\nTurn Right: D\nSpeed Up: UP\nSlow Down: DOWN\nPropellor Toggle: K\nEmergency Stop: SPACE\nExit Program: ESC')
def forward(): #code to run for a forward command
    print('roll forward for 2 seconds')
#    GPIO.output(DIG1, GPIO.LOW)          # set DIG1 as LOW, to control direction
#    GPIO.output(DIG2, GPIO.LOW)          # set DIG2 as LOW, to control direction
#    p1.start(Speed)                      # set speed for M1 to Speed variable
#    p2.start(Speed)                      # set speed for M2 at Speed Variable
    sleep(2)                             # delay for 2 second
    stop()                               # stop motors via function
def left(): #code to turn Left
    print('rotate left for 2 seconds')
#    GPIO.output(DIG1, GPIO.LOW)          # set DIG1 as LOW, to control direction
#    GPIO.output(DIG2, GPIO.HIGH)          # set DIG2 as LOW, to control direction
#    p1.start(Speed)                      # set speed for M1 to Speed variable
#    p2.start(Speed)                      # set speed for M2 at Speed Variable
    sleep(2)                             # delay for 2 second
    stop()                               # stop motors via function
def right(): #code to turn right
    print('rotate right for 2 seconds')
#    GPIO.output(DIG1, GPIO.HIGH)         # set DIG1 as LOW, to control direction
#    GPIO.output(DIG2, GPIO.LOW)          # set DIG2 as LOW, to control direction
#    p1.start(Speed)                      # set speed for M1 to Speed variable
#    p2.start(Speed)                      # set speed for M2 at Speed Variable
    sleep(2)                             # delay for 2 second
    stop()                               # stop motors via function
def backwards(): #code to run Backwards
    print('roll backwards for 2 seconds')
#    GPIO.output(DIG1, GPIO.HIGH)          # set DIG1 as LOW, to control direction
#    GPIO.output(DIG2, GPIO.HIGH)          # set DIG2 as LOW, to control direction
#    p1.start(Speed)                      # set speed for M1 to Speed variable
#    p2.start(Speed)                      # set speed for M2 at Speed Variable
    sleep(2)                             # delay for 2 second
    stop()                               # stop motors via function
def proptoggle():
    global PropOn
    if PropOn == False:
        print ('Propellor is on')
#        GPIO.output(PROP, GPIO.HIGH)
        PropOn = True
    elif PropOn == True:
        print ('Propellor is off')
#        GPIO.output(PROP, GPIO.LOW)
        PropOn = False
def stop(): #code to stop motors
        print('Complete')
#        GPIO.output(DIG1, GPIO.LOW)          # Direction can ignore
#        GPIO.output(DIG2, GPIO.LOW)          # Direction can ignore
#        p1.start(0)                          # set speed for M1 at 0%
#        p2.start(0)                          # set speed for M2 at 0%   
def raisespeed(): #code to raise the power to the motors
    global Speed
    if Speed >= 100:
        print('speed is at', Speed, '%')
        sleep(0.3)
    else:
        Speed +=10
        print('speed is at', Speed, '%')
        sleep(0.3)
def lowerspeed(): #code to lower the speed
    global Speed
    if Speed <= 10:
        print('speed is at', Speed, '%')
        sleep(0.3)
    else:
        Speed -=10
        print('speed is at', Speed, '%')
        sleep(0.3)
while True:  # making a loop
    if keyboard.is_pressed('w'):
        forward()
    elif keyboard.is_pressed('a'):
        left()
    elif keyboard.is_pressed('s'):
        backwards()
    elif keyboard.is_pressed('d'):
        right()
    elif keyboard.is_pressed('up'):
        raisespeed()
    elif keyboard.is_pressed('down'):
        lowerspeed()        
    elif keyboard.is_pressed('space'):
        stop()
        sleep(2)
    elif keyboard.is_pressed('esc'):
        stop()
        print('Propellor has been stopped')
#        GPIO.output(PROP, GPIO.LOW)
        break
    elif keyboard.is_pressed('k'):
        proptoggle()
        sleep(0.5)