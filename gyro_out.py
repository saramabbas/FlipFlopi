#Connections
#MPU6050 - Raspberry pi
#VCC - 5V  (2 or 4 Board)
#GND - GND (6 - Board)
#SCL - SCL (5 - Board)
#SDA - SDA (3 - Board)


from Kalman import KalmanAngle
import smbus            #import SMBus module of I2C
import time
import math
import numpy as np
import csv

kalmanX = KalmanAngle()
kalmanY = KalmanAngle()

RestrictPitch = True
radToDeg = 57.2957786
kalAngleX = 0
kalAngleY = 0
#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47



import csv

# open the file in the write mode
f = open('2022_gyro_rolltest.csv', 'a')

# create the csv writer
writer = csv.writer(f)

writer.writerow('test started')
#Read the gyro and acceleromater values from MPU6050
def MPU_Init():
    #write to sample rate register
    bus.write_byte_data(DeviceAddress, SMPLRT_DIV, 7)

    #Write to power management register
    bus.write_byte_data(DeviceAddress, PWR_MGMT_1, 1)

    #Write to Configuration register
    #Setting DLPF (last three bit of 0X1A to 6 i.e '110' It removes the noise due to vibration.) https://ulrichbuschbaum.wordpress.com/2015/01/18/using-the-mpu6050s-dlpf/
    bus.write_byte_data(DeviceAddress, CONFIG, int('0000110',2))

    #Write to Gyro configuration register
    bus.write_byte_data(DeviceAddress, GYRO_CONFIG, 24)

    #Write to interrupt enable register
    bus.write_byte_data(DeviceAddress, INT_ENABLE, 1)


def read_raw_data(addr):
    #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(DeviceAddress, addr)
        low = bus.read_byte_data(DeviceAddress, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1)     # or bus = smbus.SMBus(0) for older version boards
DeviceAddress = 0x68   # MPU6050 device address

MPU_Init()

while(1):
 average_samples=15
 average_array = np.zeros((2,average_samples))

 for i in range(average_samples):
  time.sleep(0)
  
  #Read Accelerometer raw value
  accX = read_raw_data(ACCEL_XOUT_H)
  accY = read_raw_data(ACCEL_YOUT_H)
  accZ = read_raw_data(ACCEL_ZOUT_H)

  #print(accX,accY,accZ)
  #print(math.sqrt((accY**2)+(accZ**2)))
  if (RestrictPitch):
     roll = math.atan2(accY,accZ) * radToDeg
     pitch = math.atan(-accX/math.sqrt((accY**2)+(accZ**2))) * radToDeg
  else:
     roll = math.atan(accY/math.sqrt((accX**2)+(accZ**2))) * radToDeg
     pitch = math.atan2(-accX,accZ) * radToDeg
     #print(pitch,roll)

  average_array[0][i] = pitch
  average_array[1][i] = roll
    
 average = round(np.mean(average_array, axis=1),2)


 print (average[0],2, average[1],2)
 

 # write a row to the csv file
 #writer.writerow(round(average[0]), round(average[1]))
#  writer.writerow(average)

# close the file
f.close()


#  print(pitch,roll)



