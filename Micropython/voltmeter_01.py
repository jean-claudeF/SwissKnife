from ADC_ADS1115_02a import ADS1115
from machine import I2C, Pin
import time

i2c_channel = 0
#sclpin = 9
#sdapin = 8
sclpin = 21
sdapin = 20

i2c = I2C(i2c_channel, scl=Pin(sclpin), sda=Pin(sdapin))
adc = ADS1115(i2c, address = 72, gain = 1)
k = (5+1)/1                      # for 5M/1M divider
# Calibrated:
k3 = 10/9.834 * k
k2 = 10/9.882 * k
k1 = 10/9.83 * k
k0 = 10/9.804 * k

adc.factors = [k0, k1, k2, k3]

def get_v():
    v = adc.read_all_as_string()
    print(v)
    #return v

if __name__ == "__main__":
    v = get_v()
    #print(v)
    