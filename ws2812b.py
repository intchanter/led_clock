import machine
import neopixel


pixels = 60


def main():
    print("Entering main()")
    tape = machine.Pin(13, machine.Pin.OUT)
    neo = neopixel.NeoPixel(tape, pixels)
    for i in range(pixels):
        neo[i] = (i * 4, 256 - (i * 4), 0)
    neo.write()


if __name__ == "__main__":
    main()