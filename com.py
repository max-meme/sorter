import smbus
import time
# for RPI version 1, use bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x8

def writeData(value):
    byteValue = StringToBytes(value)    
    bus.write_i2c_block_data(address,0x00,byteValue) #first byte is 0=command byte.. just is.
    return -1


def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal

def sendI2C(m):
    print("sending: " + m)
    writeData(m)
