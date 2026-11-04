import machine
import time


LED = machine.Pin(2, machine.Pin.OUT)
UNIT = 1 / 5


letters = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def morse_letter(letter: str):
    print(letter,)
    for symbol in letters[letter]:
        length = UNIT * (3 if symbol == "-" else 1)
        LED.on()
        time.sleep(length)
        LED.off()
        time.sleep(UNIT)
    time.sleep(UNIT * 2)


def run():
    while True:
        for letter in "abcdefghijklmnopqrstuvwxyz":
            morse_letter(letter)
        time.sleep(UNIT * 4)