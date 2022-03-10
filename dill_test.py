
"""
This program demonstrates the use of dill module which is very handy for reading and writing any python 
objects.

"""

import pickle
import pandas as pd

# Importing the data
dataset = pd.read_csv('Data_Powerplant.csv')
x = dataset.iloc[:, -1].values


# array = [[1,1,1], [2,2,2], [3,3,3]]

def save_data(a):
    with open("c:/Users/RD/Documents/GitHub/pyConsole/array.pkl", "wb") as o:
        pickle.dump(a, o)

save_data(x)

def load_data():
    with open("c:/Users/RD/Documents/GitHub/pyConsole/array.pkl", "rb") as o:
        load = pickle.load(o)
    return load

store = load_data()
print(store[0:10])