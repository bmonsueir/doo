import numpy as np
from pandas import Series,DataFrame
import pandas as pd
from activity.models import Activity
import sys,os


foods = pd.read_csv('activity/static/activity/activity.csv',sep=',',  names = ['exercise','weight1','weight2','weight3','weight4'])
 

for index, item in foods.iterrows():
    activity = Activity()
    activity.exercise = item['exercise']
    activity.weight1 = item['weight1']
    activity.weight2 = item['weight2']
    activity.weight3 = item['weight3']
    activity.weight4 = item['weight4']
    activity.save()
    