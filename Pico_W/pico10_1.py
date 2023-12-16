from machine import ADC, Timer
# Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.

def	callback1(t:Timer):
    sensor = ADC(4)
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706)/0.001721
    print(temperature)
    
time1 = Timer()
time1.init(period = 1000, callback = callback1)