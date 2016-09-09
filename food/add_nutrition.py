import numpy as np
from pandas import Series,DataFrame
import pandas as pd
from food.models import Nutrition
import sys,os


nutrition = pd.read_csv('food/static/food/NUT_DAT.csv',sep=',',  names = ['food','test','value'])
 

for index, item in nutrition.iterrows():
    nutrition = Nutrition()
    nutrition.food = item['food']
    nutrition.test = item['test']
    nutrition.value = item['value']
    nutrition.save()
    