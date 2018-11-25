from gpiozero import Robot
import time
import curses

front = Robot(left=(7, 8), right=(9, 10))
back = Robot(left = (21, 20), right = (26, 19))

def stop():
    front.stop()
    back.stop()

def forward():
    front.forward()
    back.forward()

def backward():
    front.backward()
    back.backward()

def circleRight():
    front.right()
    back.right()
def circleLeft():
    front.left()
    back.left()

def circleRight(x):
    front.right(x)
    back.right(x)
def circleLeft(x):
    front.left(x)
    back.left(x)
    
import sys, termios, tty, os, time
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2

if __name__ == '__main__':
    while True:
        char = getch()

        if (char == "p"):
            print("Stop!")
            exit(0)

        if (char == "a"):
            circleLeft(1) 
        elif (char == "d"):
            circleRight(1)
        elif (char == "w"):
            forward()
        elif (char == "s"):
            backward()
        elif (char == "1"):
            print("Number 1 pressed")
