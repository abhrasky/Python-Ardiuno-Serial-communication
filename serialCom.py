import serial
import time
import pandas as pd
import numpy as np






class serial_module():
    
    def __init__(self):
        self.port='/dev/ttyACM0'
        self.baud_rate=9600
        self.rx_data=""          # data recieved from controller 
        self.tx_data=""          # data to send to controller

    def serial_open(self):
        self.ser=serial.Serial(self.port,self.baud_rate)
        print('starting...')
        
    def serial_read(self):
        self.rx_data=self.ser.readline().decode('utf-8')
        print(self.rx_data)
        
    def serial_write(self):
        if(type(self.tx_data)==str):
            self.tx_data=self.tx_data.encode('utf-8') # converting to byte before sending as serial port sends bytes
        self.ser.write(self.tx_data) #converiting string to byte before





SL=serial_module()

SL.port='COM4'




data=pd.read_csv('myFile.csv', usecols= ['A'])

print(type(data))
data=np.array(data)


#data=np.array([1.2,2.2,3.2,4.2,5.2])

SL.serial_open()
while(1):
    for i in data:
        
        
        
        SL.tx_data=str(i[0])+'\n'
        SL.serial_write()
        
        print('sending=',i[0])
        SL.serial_read()
       
        time.sleep(.005)

        
            


        





