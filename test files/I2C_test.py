from smbus import SMBus;
from time import sleep;

addr = 0x8
bus = SMBus(1)

while True:
    sleep(1)
    bus.write_byte(addr, 0x0)
    sleep(1)
    bus.write_byte(addr, 0x1)

