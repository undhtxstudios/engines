from pygame import quit
from sys import exit

def quit_listener(event):
    print(f"Quit listener called: {event}")
    quit()
    exit()

def mouse_down_listener_1(event):
    print(f"Mouse down listener 1 called: {event}")

def mouse_down_listener_2(event):
    print(f"Mouse down listener 2 called: {event}")

def key_down_listener(event):
    print(f"Key down listener called: {event}")