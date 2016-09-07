#run once to populate the database with nutritional information
import numpy as np
from pandas import Series,DataFrame
import pandas as pd

# foods = pd.read_csv('food/static/food/FOOD_DES.txt',sep=',',  header=None,  usecols = [0,2,4])
# dbcol = pd.read_csv('food/static/food/nut_def.csv', sep = ',', header=None,  usecols = [1,2,4])
# nutrition = pd.read_csv('food/static/food/NUT_DAT.csv', sep = ',', header=None, usecols = [0,1,2])


def load_foods(cols):
    foods = pd.read_csv('food/static/food/FOOD_DES.txt',sep=',',  names = cols)
    return foods

def load_defs(cols):
    dbcol = pd.read_csv('food/static/food/nut_def.csv', sep = ',', names = cols)
    return dbcol
    
def load_nut(cols):
    nutrition = pd.read_csv('food/static/food/NUT_DAT.csv', sep = ',', names = cols)
    return nutrition


def find_food_names(partial_name):
    """
    input partial word that is being looked up and return food names that match
    """
    content = []
    if len(partial_name) > 2:
        foods = load_foods([2])
        print(partial_name)
        for index, food in foods.iterrows():
            if partial_name.lower() in food[2].lower() and food[2] not in content:
                content.append(food[2])
            
    return content
    
def find_food_code(food_name):
    """
    input food name and return food code
    """
    content = []
    if len(food_name) > 2:
        foods = load_foods([2])
        print(food_name)
        for index, food in foods.iterrows():
            if food_name.lower() in food[2].lower() and food[2] not in content:
                content.append(food[2])
            
    return content


def find_components(food_code):
    """
    input is the code number and return nutritional data
    """
    content = {}
    
    return content
    
    
def find_food_name(food_name):
    """
    input food names and return food name
    """
    content = []
    if len(food_name) > 2:
        foods = load_foods([2])
        print(food_name)
        for index, food in foods.iterrows():
            if food_name.lower() in food[2].lower() and food[2] not in content:
                content.append(food[2])
            
    return content
    
def dict_food_codes():
    food_codes = load_foods(['code','group','name','desc0','desc1','desc2','desc3','desc4','desc5','desc6','desc7','desc8','desc9'])
    content = {}
    for index, food_code in food_codes.iterrows():
        desc = ""
        for i in range(10):
            desc_index = 'desc' + str(i)
            if type(food_code[desc_index]) is str:
                desc += food_code[desc_index].lower() + " "
        content[food_code['code']] =  food_code['name'].lower() + ' (' + desc + ')'
    print(content)

def dict_test_codes():
    test_codes = load_defs(['code','unit','abrev','name'])
    content = {}
    for index, test_code in test_codes.iterrows():
        content[test_code['code']] =  test_code['name'].lower() + ' (' + test_code['unit'] + ')'
    print(content)   

dict_food_codes()

