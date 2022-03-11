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

# Pretty Table
for i in range(0, 9568):
    for j in range(i, 16 + i):
        t.add_row(list(X[:][j]))
    print(Fore.GREEN + str(t), end = "\r")
    t.clear_rows()
    T.sleep(0.5)
    subprocess.call('clear', shell=True)

"""
The total space that is aquired by the terminal table is number of entries + 4, this bit of information
is quite useful when it comes to space management on the terminal. 

"""

