
"""
This is a prototype version of pyConsole which is still in the making. The following functions 
that are already added are given below:

1. Welcome Text 
2. Saving Datum in a temporary file 
3. Colour coding the data 
3. Creating a Table of the input data on terminal 
4. Plotting a 2-D graph of any 2 user input columns

"""

# Importing the Libraries
import pandas as pd
import numpy as np 
import time as T 
import collections as col
import subprocess
import dill
import os
from prettytable import PrettyTable
from colorama import Fore, Style
from pyfiglet import Figlet
import matplotlib.pyplot as plt

class Channel:

    flag = 0

    # Constructor
    def __init__(self, channel_id = None):
        self.channel_id = channel_id

    # Clear the screen
    def clear_screen(self):
        return subprocess.call('clear', shell=True)
    
    # Welcome Text
    def welcome_text(self, text):
        f = Figlet(font='slant')
        print(Fore.GREEN + f.renderText(text))
        # Print a nice banner 
        print("-" * 60)
        print("The data from the port is given below ")
        print("-" * 60)
        print(Style.RESET_ALL)
    
    # Importing the data
    def data_import(self, file_address):
        dataset = pd.read_csv(file_address)
        return  dataset.iloc[:, :].values

    # Storing data in a temporary file
    def save_data(self, datum):
        self.flag = 1
        with open("c:/Users/RD/Documents/GitHub/pyConsole/array.pkl", "wb") as o:
            dill.dump(datum, o)

    # Loading data from a temporary file
    def load_data(self):
        if self.flag == 1:
            with open("c:/Users/RD/Documents/GitHub/pyConsole/array.pkl", "rb") as o:
                load = dill.load(o)
            return load
        else:
            return self.data_import

    # Printing Pretty table 
    def table(self, *args):
        t = PrettyTable()
        X = self.load_data()

        # Get terminal size
        self.columns, self.rows = os.get_terminal_size()

        # Taking arguments of table class as field names
        names = []
        for arg in args:
            names.append(arg)
        t.field_names = names

        # Pretty Table
        for i in range(0, X.shape[0]):
            last_index = self.rows - 4 + i
            if last_index <= X.shape[0]:
                for j in range(i, last_index):
                        t.add_row(list(X[:][j]))
            else:
                break
            print(Fore.RED + str(t), end = "\r")
            t.clear_rows()
            T.sleep(0.3)
            subprocess.call('clear', shell=True)
        
        print(Style,RESET_ALL)
    
    # Graphing 2-D plots
    def graph_it(self, x_axis, y_axis):
        # Saving data into an array and taking transpose 
        X = np.array(self.load_data())
        x = X.T
        if x.shape[0] >= x_axis or x.shape[0] >= y_axis:
            plt.scatter(x[x_axis][:], x[y_axis][:])
            plt.xlabel("x-axis ------->")
            plt.ylabel("y-axis ------->")
            plt.show()
        else:
            print("index is out of bounds")



            


