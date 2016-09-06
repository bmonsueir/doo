#run once to populate the database with nutritional information
import numpy as np
from pandas import Series,DataFrame
import pandas as pd

foods = pd.read_csv('food/static/food/FOOD_DES.txt',sep=',',  header=None,  usecols = [0,2,4])
dbcol = pd.read_csv('food/static/food/nut_def.csv', sep = ',', header=None,  usecols = [1,2,4])
nutrition = pd.read_csv('food/static/food/NUT_DAT.csv', sep = ',', header=None, usecols = [0,1,2])
for i in range(len(nutrition)):
    
    print(nutrition[1][i])


