import numpy as np
from pandas import Series,DataFrame
import pandas as pd
from food.models import Food
import sys,os


foods = pd.read_csv('food/static/food/FOOD_DES.txt',sep=',',  names = ['code','group','name','desc0','desc1','desc2','desc3','desc4','desc5','desc6','desc7','desc8','desc9'])
 

for index, item in foods.iterrows():
    food = Food()
    food.code = item['code']
    food.group = item['group']
    food.name = item['name']
    desc = ""
    Y = False
    for i in range(10):
        desc_index = 'desc' + str(i)
        if item[desc_index] == 'Y' or Y:
            Y = True
        else:
            desc += str(item[desc_index]).lower() + " "
    food.description = desc      
    food.save()
    