# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:14:15 2018

@author: abhis
"""

from pandas import read_csv

dataset1 = read_csv('cereal_data.csv', header=0)
dataset2 = read_csv('Perfume_SD.csv', header=0)
dataset3 = read_csv('Aircraft_SD.csv', header=0)
dataset4 = read_csv('Computer_SD.csv', header=0)
avgc1 = 0
avgc2 = 0
avgc3 = 0
avgc4 = 0
count = 0
countR1 = 0
countM1 = 0
countP1 = 0
countT1 = 0
countD1 = 0
countR2 = 0
countM2 = 0
countP2 = 0
countT2 = 0
countD2 = 0
countR3 = 0
countM3 = 0
countP3 = 0
countT3 = 0
countD3 = 0
countR4 = 0
countM4 = 0
countP4 = 0
countT4 = 0
countD4 = 0
time1 = dataset1['stageTime'].mean()
for index, row in dataset1.iterrows():
    count = count + 1
    if str(row['Stage Name']).startswith("Retail_"):
        countR1 = countR1+1
    if str(row['Stage Name']).startswith("Manuf_"):
        countM1 = countM1+1
    if str(row['Stage Name']).startswith("Part_"):
        countP1 = countP1+1
    if str(row['Stage Name']).startswith("Trans_"):
        countT1 = countT1+1
    if str(row['Stage Name']).startswith("Dist_"):
        countD1 = countD1+1
    temp = str(row['stageCost']).lstrip("$")
    avgc1 = avgc1 + int(temp)
    if row['relDepth'] != 0:
        dataset1 = dataset1.drop([index],axis=0)
demand1 = dataset1['avgDemand'].mean()
avgc1 = avgc1/count
count = 0
time2 = dataset2['stageTime'].mean()
for index, row in dataset2.iterrows():
    count = count + 1
    if str(row['Stage Name']).startswith("Retail_"):
        countR2 = countR2+1
    if str(row['Stage Name']).startswith("Manuf_"):
        countM2 = countM2+1
    if str(row['Stage Name']).startswith("Part_"):
        countP2 = countP2+1
    if str(row['Stage Name']).startswith("Trans_"):
        countT2 = countT2+1
    if str(row['Stage Name']).startswith("Dist_"):
        countD2 = countD2+1
    temp = str(row['stageCost']).lstrip("$")
    avgc2 = avgc2 + int(temp)
    if row['relDepth'] != 0:
        dataset2 = dataset2.drop([index],axis=0)
demand2 = dataset2['avgDemand'].mean()
avgc2 = avgc2/count
count = 0
time3 = dataset3['stageTime'].mean()
for index, row in dataset3.iterrows():
    count = count + 1
    if str(row['Stage Name']).startswith("Retail_"):
        countR3 = countR3+1
    if str(row['Stage Name']).startswith("Manuf_"):
        countM3 = countM3+1
    if str(row['Stage Name']).startswith("Part_"):
        countP3 = countP3+1
    if str(row['Stage Name']).startswith("Trans_"):
        countT3 = countT3+1
    if str(row['Stage Name']).startswith("Dist_"):
        countD3 = countD3+1
    temp = str(row['stageCost']).lstrip("$")
    avgc3 = avgc3 + int(temp)
    if row['relDepth'] != 0:
        dataset3 = dataset3.drop([index],axis=0)
demand3 = dataset3['avgDemand'].mean()
avgc3 = avgc3/count
count = 0
time4 = dataset4['stageTime'].mean()
for index, row in dataset4.iterrows():
    count = count + 1
    if str(row['Stage Name']).startswith("Retail_"):
        countR4 = countR4+1
    if str(row['Stage Name']).startswith("Manuf_"):
        countM4 = countM4+1
    if str(row['Stage Name']).startswith("Part_"):
        countP4 = countP4+1
    if str(row['Stage Name']).startswith("Trans_"):
        countT4 = countT4+1
    if str(row['Stage Name']).startswith("Dist_"):
        countD4 = countD4+1
    temp = str(row['stageCost']).lstrip("$")
    avgc4 = avgc4 + int(temp)
    if row['relDepth'] != 0:
        dataset4 = dataset4.drop([index],axis=0)
demand4 = dataset4['avgDemand'].mean()
avgc4 = avgc4/count

dataSummary = { 'Cereal Co.' : {'ChainDemand': demand1,
                                'ChainCost':avgc1,
                                'ChainTime':time1,
                                'ChainMetric':demand1/(avgc1*time1),
                                'ChainStages':{'Part':countP1,
                                               'Trans':countT1,
                                              'Manuf':countM1,
                                              'Dist':countD1,
                                              'Retail':countR1}},
                'Perfume Co.':{'ChainDemand': demand2,
                               'ChainCost':avgc2,
                               'ChainTime':time2,
                               'ChainMetric':demand2/(avgc2*time2),
                               'ChainStages':{'Part':countP2,
                                               'Trans':countT2,
                                              'Manuf':countM2,
                                              'Dist':countD2,
                                              'Retail':countR2}},
                'Computer Co.':{'ChainDemand': demand3,
                                'ChainCost':avgc3,
                                'ChainTime':time3,
                                'ChainMetric':demand1/(avgc3*time3),
                                'ChainStages':{'Part':countP3,
                                               'Trans':countT3,
                                              'Manuf':countM3,
                                              'Dist':countD3,
                                              'Retail':countR3}},
                'Aircraft Co.':{'ChainDemand': demand4,
                                'ChainCost':avgc4,
                                'ChainTime':time4,
                                'ChainMetric':demand1/(avgc4*time4),
                                'ChainStages':{'Part':countP4,
                                               'Trans':countT4,
                                              'Manuf':countM4,
                                              'Dist':countD4,
                                              'Retail':countR4}}}