from machine import Pin, I2C

print("I2C0 [20, 21]:")
i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)
addresses = i2c.scan()
for a in addresses:
    print(hex(a))
