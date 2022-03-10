
""" 
The purpose of this class is to split, clean, decode and time tag each datum. 
It is a singleton object common to all channels and for serial devices. 

"""

import time
import numpy as np
from serial import Serial

class Parser:

    flag = 0

    def __init__(self, comm_port, rate, time_out): # Constructor of the class Parser

        # Creating an instance of the Serial from pySerial module 
        self.port = Serial(port = comm_port, timeout = time_out, baudrate = rate)

    def sep(self):

        self.flag = 1

        #Split String into distinct numbers
        self.split = self.line.split('\t') 


    def register(self):
        data_stream = self.port

        # Creating seperate lists for datums and its corresponding time_tag
        self.time_tag = []
        self.line_buffer = []

        # Checking if there is any data in the input buffer
        if data_stream.in_waiting > 0:
            while 1:
                self.line = data_stream.readline().decode('ascii')
                if self.flag == 1:
                    self.line_buffer.append(self.split)
                else:
                    self.line_buffer.append(self.line)
                self.time_tag.append(time.perf_counter())
        else:
            return False
            
    def open(self):

        return self.line_buffer

    def start_time(self):

        # Returning the initial time of execution
        return self.time_tag[0]

    def close(self):
        return self.port.close()

    def process(self):
        time = self.time_tag
        buffer = self.line_buffer

        # Creating an array of datums and its corresponding elapsed time 
        if not len(time) != len(buffer):
            return np.concatenate((buffer.reshape(len(buffer), 1), time.reshape(len(time), 1)), 1)

        try:
		    numeric_data = [int(number) for number in buffer] #Convert into integers
		    for i, curve in enumerate[curve]:
				curve_data.append(numeric_data[i]) #Add to respective data fields
			return True

		# If Conversion to integers fails
		except (UnicodeDecodeError, ValueError) as e:
			print(f"Decode Error! - time: {duration}")
			Errors = Errors + 1
			return False
        else:
            return False
        

    def forward():
    
