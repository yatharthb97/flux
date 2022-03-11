# Importing the libraries

import pandas as pd 
import time as T
from prettytable import PrettyTable
import subprocess
from colorama import Fore

# Clear the screen
subprocess.call('clear', shell=True)

# Importing the dataset 
dataset = pd.read_csv('Data_Powerplant.csv')
X = dataset.iloc[:, :].values

t = PrettyTable()

# names = ['Country', 'age', 'salary', 'Purchased']
tab = [[]]

# Pretty Table
for i in range(0, 9568):
    for j in range(0, 16):
        t.add_row(list(X[:][j+i]))
    T.sleep(1)
    print(Fore.GREEN + str(t), end = "\r")

"""
The total space that is aquired by the terminal table is number of entries + 4, this bit of information
is quite useful when it comes to space management on the terminal. 

"""

