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

def get_values(food, test):
    nutrition = load_nut(['food','test','value'])
    content = nutrition.loc[nutrition['food'] == food]
    content = content.loc[content['test'] == test]
    return content['value']

    
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
    return content

def dict_test_codes():
    test_codes = load_defs(['code','unit','abrev','name'])
    content = {}
    for index, test_code in test_codes.iterrows():
        content[test_code['code']] =  test_code['name'].lower() + ' (' + test_code['unit'] + ')'
    return content

# dict_food_codes()
print(get_values(1001, 405))