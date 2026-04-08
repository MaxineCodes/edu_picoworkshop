from boot import connection
import machine
import time
import network
import urequests as requests
import json
import config

# LED pinnen
internal_led_pin = 25
warning_led_pin = 15

# Sensor pin
sensor_pin = 4

# Initialiseren van de pinnen
internal_led = machine.Pin(internal_led_pin, machine.Pin.OUT)
warning_led = machine.machine.Pin(warning_led_pin, machine.Pin.OUT)

# ADC voor de temperatuursensor
adc = machine.ADC(machine.Pin(sensor_pin))

while connection.isconnected():
    # Lees temperatuur
    raw_value = adc.read_u16()
    voltage = (raw_value / 65535) * 3.3
    temperature = (voltage - 0.5) * 100

    # Verstuur temperatuur naar server
    url = f"http://{config.SERVER}:{config.PORT}{config.ENDPOINT}"
    data = {
        "temperature": temperature,
        "led_status": warning_led.value(),
        "timestamp": time.time()
    }
    response = requests.post(url, json=data)

    # Flash interne LED om aan te geven dat temperatuur is verzonden
    internal_led.on()
    time.sleep(0.1)
    internal_led.off()

    # Lees antwoord van server
    answer = response.json()

    # Zet of schakel waarschuwings-LED uit op basis van serverantwoord
    if answer.get("warning"):
        warning_led.on()
    else:
        warning_led.off()

    # Wacht tot de volgende meting
    time.sleep(5)  # B.v. elke 5 seconden
