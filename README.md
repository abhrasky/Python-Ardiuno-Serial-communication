# Python-Ardiuno-Serial-communication

This small piece of code will come handy while trying to send some data from computer to ardiuno via serial port,
process it there and get back it to PC again.

This is perticularly useful to check realtime operation of ardiuno when no other sensor or device is available.
User can save the sensor data in csv file or get it form internet in the same format and and send it to ardiuno 
to simulate the sensor and process the data inside the ardiuno.

Now, as serial port is used by  python code in PC for transmitting the data, ardiuno IDE cannot access the
port hence, serial plotter can not be used to see the processed data. That problem is solved here by retrivng 
back the processed data from ardiuno to PC again via same python code which can be used to visualise the processed
data.

User instruction:
1. Install python packages : pyserial,pandas and numpy using pip install
2. Place your .csv file and serialCom.py code in same folder
3. Upload serial_read_write.ino code to your ardiuno board
4. Check the port same in the ardiuno IDE
5. Open serailCom.py file in any python IDE
6. Change the present port name given in the code with your port name where ardiuno is connected
7. Run the python code and check 

* Note:
1. .CSV file must contain a column named 'A' where data are stored in number format
2. .ino file is a demo  which just multiplies 2.5 to input number and sends it back
     Change the calculation part in ardiuno code as per your requirement
3.  Ardiuno sends the data in string format. So to plot it data needs to be converted to number



