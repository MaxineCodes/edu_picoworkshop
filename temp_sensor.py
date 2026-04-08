from time import sleep
from machine import Pin
from machine import ADC

led = Pin(1, Pin.OUT)  # gewijzigd pinnummer
sensor = ADC(26)  # gewijzigde pin

prop = 3.3 / 65535
v_out = sensor.read_u16() * prop
temp = (100 * v_out) - 50  # gewijzigde berekening
print(temp)

#
#for _ in range(5):
#    led.on()
#    sleep(1)
#    led.off()
#    sleep(1)
    

