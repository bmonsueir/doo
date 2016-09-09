import numpy as np
from pandas import Series,DataFrame
import pandas as pd
from food.models import Method
import sys,os


methods = pd.read_csv('food/static/food/NUTR_DEF.txt',sep=',',  names = ['code','unit','abrev','name'])
 

for index, item in methods.iterrows():
    method = Method()
    method.code = item['code']
    method.unit = item['unit']
    method.abrev = item['abrev']
    method.name = item['name']
    method.save()
    