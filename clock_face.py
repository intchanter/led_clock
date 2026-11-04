#import datetime
import machine
import neopixel
import network
import ntptime
import time


PIXELS = 60
WIFI_SSID = "Disneyfam"
WIFI_KEY = "modernroad510"


def connect():
    print("Attempting to connect...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_KEY)
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(0.5)
    print(f"Connected: {wlan.ifconfig()}")
    ntptime.settime()
    print(time.localtime(time.time() + (-7 * 3600)))
    print(machine.RTC().datetime())


def main():
    print("Entering main()")
    led_tape = machine.Pin(13, machine.Pin.OUT)
    neo = neopixel.NeoPixel(led_tape, PIXELS)
    connect()

    while True:
        hour, minute, second = get_time()
        hour, minute, second = process_time_components(hour, minute, second)
        #now = datetime.now()
        #print(now)
        #hour, minute, second = get_time_components(now)
        #print(f"{hour}:{minute}:{second}")
        #print("Displaying on LED strip")
        for led in range(0, 60):
            red, green, blue = calculate_rgb(led, hour, minute, second)
            red, green, blue = (int(color * 255) for color in (red, green, blue))
            #print(f"RGB: {red}, {green}, {blue}")
            neo[led] = (red, green, blue)
        neo.write()
        time.sleep(0.014)


def get_time() -> tuple[float, float, float]:
    _y, _mo, _d, _wkd, hour, minute, second, micro = machine.RTC().datetime()
    second = second + micro / 1_000_000
    return hour, minute, second


def set_time(hour: int, minute: int, second: float):
    machine.RTC().datetime()


def add_time(hour: float, minute: float, second: float, amount: float):
    time.sleep(amount)
    second += amount * 4
    if second >= 60:
        second -= 60
        minute += 1
    if minute >= 60:
        minute -= 60
        hour += 1
    if hour > 12:
        hour -= 12
    return hour, minute, second


def process_time_components(hour, minute, second) -> tuple[float, float, float]:
    """
    Given a time.time(), return fractional hours, minutes, and seconds
    """
    #second = timestamp.second + timestamp.microsecond / 1_000_000
    minute = int(minute) + second / 60
    hour = (int(hour) + minute / 60) % 12
    return hour, minute, second


def calculate_color_value(light: int, position: float):
    value = 0
    close = abs(position - light)
    if close < 1:
        value = 1 - close
    if close > 59:
        value = close - 59
    return value


def calculate_rgb(light: int, hour: float, minute: float, second: float):
    red, green, blue = (0, 0, 0)
    hour_pos = hour * 5
    red = calculate_color_value(light, hour_pos)
    green = calculate_color_value(light, minute)
    blue = calculate_color_value(light, second)
    return red, green, blue


if __name__ == "__main__":
    main()