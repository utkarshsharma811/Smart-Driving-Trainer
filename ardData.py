import serial
import time
import pandas as pd
# set up the serial line
ser = serial.Serial('COM5', 9600)

data = []
time = []                       # empty list to store the data
left = []
right = []
print('entering the loop now \n')
for i in range(700):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    print(string)
    if(string.find('x')!=-1):
        data.append(string.split('x'))
ser.close()

for line in data:
    if len(line)!=3:
        continue
    else:
        time.append(line[0])
        left.append(line[1])
        right.append(line[2])

for i in range(len(time)):
  time[i] = int(time[i])
  left[i] = int(left[i])
  right[i] = int(right[i])
  
size = int(time[len(time)-1]/1000) + 1

leftMod = [0] * size
rightMod = [0] * size

for i in range(len(time)):
  n = (time[i])//1000
  if (left[i] >= 1):
    leftMod[n] = 1
  if (right[i] >= 10 ):
    rightMod[n] = 1

timeSec = []
for i in range(size):
    timeSec.append(i)

df = pd.DataFrame({'time':timeSec, 'left': leftMod, 'right': rightMod})    
df.to_csv('ArduinoData1Part2.csv', index = False)
