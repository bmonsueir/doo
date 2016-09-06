import numpy as np
from pandas import Series,DataFrame
import pandas as pd

def load_foods(cols):
    # text_file = open("food/static/food/FOOD_DES.txt", "r")
    # foods = text_file.read().split(',')
    foods = pd.read_csv('food/static/food/FOOD_DES.txt',sep=',',  header=None,  usecols = cols)
    return foods

def load_defs(cols):
    dbcol = pd.read_csv('food/static/food/nut_def.csv', sep = ',', header=None,  usecols = cols)
    return dbcol
    
def load_nut(cols):
    nutrition = pd.read_csv('food/static/food/NUT_DAT.csv', sep = ',', header=None, usecols = cols)
    return nutrition


def find_food(input):
    content = []
    foods = load_foods([2])
    print(foods)
    
    for food in foods:
        # food.lower()
        print(input)
        print(food)



def find_components(input):
    content = {}
    
    return content

print(find_food("but"))
