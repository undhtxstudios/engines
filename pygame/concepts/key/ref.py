"""
key module: dealing with keyboard input

pygame.key.get_focused()
    checks if the display window has keyboard focus

pygame.key.get_pressed()
    returns a sequence representing the state of every key
    each key's state is either 1 (pressed) or 0 (not pressed)

pygame.key.set_mods(mods)
    temporarily sets the modifier keys (like shift, ctrl, etc.)
    mods is a bitmask of KMOD_* constants

pygame.key.get_mods()
    returns a bitmask of the modifier keys currently pressed

pygame.key.set_repeat(delay, interval)
    controls how held keys are repeated
    delay: time in milliseconds before the key starts repeating
    interval: time in milliseconds between repeated key events

pygame.key.get_repeat()
    returns the current repeat settings as a tuple (delay, interval)

pygame.key.name(key)
    returns the name of the key corresponding to the given key constant

pygame.key.key_code(name)
    returns the key constant corresponding to the given key name

pygame.key.start_text_input()
    begins receiving text input events (useful for on-screen keyboards)

pygame.key.stop_text_input()
    stops receiving text input events

pygame.key.get_input_rect()
    returns the rectangle of the area where text input is received

pygame.key.set_text_input_rect(rect)
    sets the rectangle of the area where text input is received
    rect is a pygame.Rect object or a tuple (x, y, width, height)

Constants

K_* Constants:
    pygame.K_* constants represent all the keys on the keyboard.
    Examples:
    - pygame.K_a: The 'a' key
    - pygame.K_SPACE: The spacebar key
    - pygame.K_RETURN: The enter key
    - pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT: The arrow keys

Modifier Key Constants (KMOD_*):
    pygame.KMOD_* constants represent modifier keys.
    Examples:
    - pygame.KMOD_SHIFT: The shift key
    - pygame.KMOD_CTRL: The control key
    - pygame.KMOD_ALT: The alt key
    - pygame.KMOD_CAPS: The caps lock key
    - pygame.KMOD_META: The meta key (Windows key on PC)

Usage Example:

import pygame
pygame.init()

# Check if a specific key is pressed
keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE]:
    print("Spacebar is pressed")

# Set key repeat settings
pygame.key.set_repeat(250, 30)

# Get the name of a key from its key code
print(pygame.key.name(pygame.K_a))  # Output: 'a'
"""
