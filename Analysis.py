# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:32:55 2018

@author: abhis
"""

from bokeh.io import show, output_file
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource
from pandas import read_csv

dataset1 = read_csv('cereal_data.csv', header=0)

newdata = dataset1.drop(['xPosition','yPosition'], axis = 1)

avgdD = 0
countD = 0
avgdM = 0
countM = 0
avgdP = 0
countP = 0
avgdT = 0
countT = 0
avgcD = 0
avgcM = 0
avgcP = 0
avgcT = 0
for index, row in newdata.iterrows():
    if str(row['Stage Name']).startswith("Dist_"):
        countD = countD+1
        avgdD = avgdD + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcD = avgcD + int(temp)
    elif str(row['Stage Name']).startswith("Manuf_"):
        countM = countM+1
        avgdM = avgdM + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcM = avgcM + int(temp)
    elif str(row['Stage Name']).startswith("Part_"):
        countP = countP+1
        avgdP = avgdP + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcP = avgcP + int(temp)
    elif str(row['Stage Name']).startswith("Trans_"):
        countT = countT+1
        avgdT = avgdT + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcT = avgcT + int(temp)

dataCereal = {'StageTime': {'part':int(avgdP/countP),'manuf':int(avgdM/countM),
                            'dist':int(avgdD/countD),'trans':int(avgdT/countT)},
              'StageCost': {'part':int(avgcP/countP),'manuf':int(avgcM/countM),
                            'dist':int(avgcD/countD),'trans':int(avgcT/countT)}}

dataset2 = read_csv('Perfume_SD.csv', header=0)

newdata = dataset2.drop(['xPosition','yPosition'], axis = 1)

avgdD = 0
countD = 0
avgdM = 0
countM = 0
avgdP = 0
countP = 0
avgdR = 0
countR = 0
avgcD = 0
avgcM = 0
avgcP = 0
avgcR = 0
for index, row in newdata.iterrows():
    if str(row['Stage Name']).startswith("Dist_"):
        countD = countD+1
        avgdD = avgdD + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcD = avgcD + int(temp)
    elif str(row['Stage Name']).startswith("Manuf_"):
        countM = countM+1
        avgdM = avgdM + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcM = avgcM + int(temp)
    elif str(row['Stage Name']).startswith("Part_"):
        countP = countP+1
        avgdP = avgdP + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcP = avgcP + int(temp)
    elif str(row['Stage Name']).startswith("Retail_"):
        countR = countR+1
        avgdR = avgdR + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcR = avgcR + int(temp)
        
dataPerfume = {'StageTime': {'part':int(avgdP/countP),'manuf':int(avgdM/countM),
                             'dist':int(avgdD/countD),'retail':int(avgdR/countR)},
              'StageCost': {'part':int(avgcP/countP),'manuf':int(avgcM/countM),
                             'dist':int(avgcD/countD),'retail':int(avgcR/countR)}}       


dataset3 = read_csv('Aircraft_SD.csv', header=0)

newdata = dataset3.drop(['xPosition','yPosition'], axis = 1)

avgdR = 0
countR = 0
avgdM = 0
countM = 0
avgdP = 0
countP = 0
avgdT = 0
countT = 0
avgcT = 0
avgcM = 0
avgcP = 0
avgcR = 0
for index, row in newdata.iterrows():
    if str(row['Stage Name']).startswith("Retail_"):
        countR = countR+1
        avgdR = avgdR + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcR = avgcR + int(temp)
    elif str(row['Stage Name']).startswith("Manuf_"):
        countM = countM+1
        avgdM = avgdM + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcM = avgcM + int(temp)
    elif str(row['Stage Name']).startswith("Part_"):
        countP = countP+1
        avgdP = avgdP + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcP = avgcP + int(temp)
    elif str(row['Stage Name']).startswith("Trans_"):
        countT = countT+1
        avgdT = avgdT + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcT = avgcT + int(temp)


dataAircraft = {'part':int(avgdP/countP),'manuf':int(avgdM/countM),
        'retail':int(avgdR/countR),'trans':int(avgdT/countT)}

dataAircraft = {'StageTime': {'part':int(avgdP/countP),'manuf':int(avgdM/countM),
                              'retail':int(avgdR/countR),'trans':int(avgdT/countT)},
                'StageCost': {'part':int(avgcP/countP),'manuf':int(avgcM/countM),
                             'retail':int(avgcR/countR),'trans':int(avgcT/countT)}} 

dataset4 = read_csv('Computer_SD.csv', header=0)

newdata = dataset4.drop(['xPosition','yPosition'], axis = 1)

avgdR = 0
countR = 0
avgdM = 0
countM = 0
avgdP = 0
countP = 0
avgdT = 0
countT = 0
avgcT = 0
avgcM = 0
avgcP = 0
avgcR = 0
for index, row in newdata.iterrows():
    if str(row['Stage Name']).startswith("Retail_"):
        countR = countR+1
        avgdR = avgdR + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcR = avgcR + int(temp)
    elif str(row['Stage Name']).startswith("Manuf_"):
        countM = countM+1
        avgdM = avgdM + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcM = avgcM + int(temp)
    elif str(row['Stage Name']).startswith("Part_"):
        countP = countP+1
        avgdP = avgdP + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcP = avgcP + int(temp)
    elif str(row['Stage Name']).startswith("Trans_"):
        countT = countT+1
        avgdT = avgdT + row['stageTime']
        temp = str(row['stageCost']).lstrip("$")
        avgcT = avgcT + int(temp)

dataComputer = {'StageTime': {'part':int(avgdP/countP),'manuf':int(avgdM/countM),
                              'retail':int(avgdR/countR),'trans':int(avgdT/countT)},
                'StageCost': {'part':int(avgcP/countP),'manuf':int(avgcM/countM),
                             'retail':int(avgcR/countR),'trans':int(avgcT/countT)}}
    

