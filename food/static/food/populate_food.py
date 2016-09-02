#run once to populate the database with nutritional information
import numpy as np
from pandas import Series,DataFrame
import pandas as pd

dframe = pd.read_csv('FOOD_DES.txt',sep=',', usecols = [0,2,4])

print(dframe)
