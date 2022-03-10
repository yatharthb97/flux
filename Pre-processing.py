
"""
This is a prototype version of pyConsole which is still in the making. The following functions 
that are already added are given below:

1. Welcome Text 
2. Saving Datum in a temporary file 
3. Colour coding the data 
3. Creating a circular buffer

"""

# Importing the Libraries
import pandas as pd
import time as t 
import collections as col
import subprocess
import dill
from colorama import Fore

# Clear the screen
subprocess.call('clear', shell=True)

# Welcome Text
from pyfiglet import Figlet
f = Figlet(font='slant')
print(Fore.GREEN + f.renderText('Welcome to pyConsole'))

# Importing the data
dataset = pd.read_csv('c:/Users/RD/Documents/GitHub/pyConsole/Data_Powerplant.csv')
x = dataset.iloc[:, -1].values

# Storing data in a temporary file
def save_data(datum):
    with open("c:/Users/RD/Documents/GitHub/pyConsole/array.pkl", "wb") as o:
        dill.dump(datum, o)

save_data(x)

def load_data():
    with open("c:/Users/RD/Documents/GitHub/pyConsole/array.pkl", "rb") as o:
        load = dill.load(o)
    return load

# Creating a buffer using deque
temp_list = load_data()
buffer = temp_list[0:10]
de = col.deque(buffer, maxlen = 10)

# Print a nice banner 
print("-" * 60)
print("The data from the port is below ")
print("-" * 60)

# Appending the dataset in the buffer 
for i in range(10, len(x)):
    t.sleep(0.5)
    de.append(x[i])
    print(Fore.RED + str(list(de)), end = "\r")
