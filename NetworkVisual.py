# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:14:15 2018

@author: abhis
"""
from flask import Flask
from flask import Response, request, render_template, redirect, url_for
from pandas import read_csv
import json
import os

app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__))

# @app.route('/', methods=['GET'])
# def home():
#     return render_template('index.html')


@app.route('/', methods=['GET'])
def home_old():
    dataset1 = read_csv(path + '/data/Cereal_SD.csv',
                        low_memory=False, header=0)
    dataset2 = read_csv(path + '/data/Perfume_SD.csv',
                        low_memory=False, header=0)
    dataset3 = read_csv(path + '/data/Aircraft_SD.csv',
                        low_memory=False, header=0)
    dataset4 = read_csv(path + '/data/Computer_SD.csv',
                        low_memory=False, header=0)
    avgc1, avgc2, avgc3, avgc4 = 0, 0, 0, 0
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
            countR1 = countR1 + 1
        if str(row['Stage Name']).startswith("Manuf_"):
            countM1 = countM1 + 1
        if str(row['Stage Name']).startswith("Part_"):
            countP1 = countP1 + 1
        if str(row['Stage Name']).startswith("Trans_"):
            countT1 = countT1 + 1
        if str(row['Stage Name']).startswith("Dist_"):
            countD1 = countD1 + 1
        temp = str(row['stageCost']).lstrip("$").rstrip(" ")
        avgc1 = avgc1 + int(float(temp))
        if row['relDepth'] != 0:
            dataset1 = dataset1.drop([index], axis=0)
    demand1 = dataset1['avgDemand'].mean()
    avgc1 = avgc1 / count
    count = 0
    time2 = dataset2['stageTime'].mean()
    for index, row in dataset2.iterrows():
        count = count + 1
        if str(row['Stage Name']).startswith("Retail_"):
            countR2 = countR2 + 1
        if str(row['Stage Name']).startswith("Manuf_"):
            countM2 = countM2 + 1
        if str(row['Stage Name']).startswith("Part_"):
            countP2 = countP2 + 1
        if str(row['Stage Name']).startswith("Trans_"):
            countT2 = countT2 + 1
        if str(row['Stage Name']).startswith("Dist_"):
            countD2 = countD2 + 1
        temp = str(row['stageCost']).lstrip("$").rstrip(" ")
        avgc2 = avgc2 + int(float(temp))
        if row['relDepth'] != 0:
            dataset2 = dataset2.drop([index], axis=0)
    demand2 = dataset2['avgDemand'].mean()
    avgc2 = avgc2 / count
    count = 0
    time3 = dataset3['stageTime'].mean()
    for index, row in dataset3.iterrows():
        count = count + 1
        if str(row['Stage Name']).startswith("Retail_"):
            countR3 = countR3 + 1
        if str(row['Stage Name']).startswith("Manuf_"):
            countM3 = countM3 + 1
        if str(row['Stage Name']).startswith("Part_"):
            countP3 = countP3 + 1
        if str(row['Stage Name']).startswith("Trans_"):
            countT3 = countT3 + 1
        if str(row['Stage Name']).startswith("Dist_"):
            countD3 = countD3 + 1
        temp = str(row['stageCost']).lstrip("$").rstrip(" ")
        avgc3 = avgc3 + int(float(temp))
        if row['relDepth'] != 0:
            dataset3 = dataset3.drop([index], axis=0)

    demand3 = dataset3['avgDemand'].mean()
    avgc3 = avgc3 / count
    count = 0
    time4 = dataset4['stageTime'].mean()
    for index, row in dataset4.iterrows():
        count = count + 1
        if str(row['Stage Name']).startswith("Retail_"):
            countR4 = countR4 + 1
        if str(row['Stage Name']).startswith("Manuf_"):
            countM4 = countM4 + 1
        if str(row['Stage Name']).startswith("Part_"):
            countP4 = countP4 + 1
        if str(row['Stage Name']).startswith("Trans_"):
            countT4 = countT4 + 1
        if str(row['Stage Name']).startswith("Dist_"):
            countD4 = countD4 + 1
        temp = str(row['stageCost']).lstrip("$").rstrip(" ")
        avgc4 = avgc4 + int(float(temp))
        if row['relDepth'] != 0:
            dataset4 = dataset4.drop([index], axis=0)
    demand4 = dataset4['avgDemand'].mean()
    avgc4 = avgc4 / count
    dataSummary = {'Cereal Co.': {'ChainDemand': demand1,
                                  'ChainCost': avgc1,
                                  'ChainTime': time1,
                                  'ChainMetric': demand1 / (avgc1 * time1),
                                  'ChainStages': {'Part': countP1,
                                                  'Trans': countT1,
                                                  'Manuf': countM1,
                                                  'Dist': countD1,
                                                  'Retail': countR1}},
                   'Perfume Co.': {'ChainDemand': demand2,
                                   'ChainCost': avgc2,
                                   'ChainTime': time2,
                                   'ChainMetric': demand2 / (time2),
                                   'ChainStages': {'Part': countP2,
                                                   'Trans': countT2,
                                                   'Manuf': countM2,
                                                   'Dist': countD2,
                                                   'Retail': countR2}},
                   'Computer Co.': {'ChainDemand': demand3,
                                    'ChainCost': avgc3,
                                    'ChainTime': time3,
                                    'ChainMetric': demand1 / (avgc3 * time3),
                                    'ChainStages': {'Part': countP3,
                                                    'Trans': countT3,
                                                    'Manuf': countM3,
                                                    'Dist': countD3,
                                                    'Retail': countR3}},
                   'Aircraft Co.': {'ChainDemand': demand4,
                                    'ChainCost': avgc4,
                                    'ChainTime': time4,
                                    'ChainMetric': demand1 / (avgc4 * time4),
                                    'ChainStages': {'Part': countP4,
                                                    'Trans': countT4,
                                                    'Manuf': countM4,
                                                    'Dist': countD4,
                                                    'Retail': countR4}}}
    return render_template('index.html', pie_text="Demands per Cost and Time",
                           label1_pie='Cereal Co.', y1_pie=dataSummary['Cereal Co.']['ChainMetric'],
                           label2_pie='Perfume Co.', y2_pie=dataSummary['Perfume Co.']['ChainMetric'],
                           label3_pie='Computer Co.', y3_pie=dataSummary['Computer Co.']['ChainMetric'],
                           label4_pie='Aircraft Co.', y4_pie=dataSummary['Aircraft Co.']['ChainMetric'],

                           label1Cer=dataSummary['Cereal Co.']['ChainStages']['Part'],
                           label2Cer=dataSummary['Cereal Co.']['ChainStages']['Trans'],
                           label3Cer=dataSummary['Cereal Co.']['ChainStages']['Manuf'],
                           label4Cer=dataSummary['Cereal Co.']['ChainStages']['Dist'],
                           label5Cer=dataSummary['Cereal Co.']['ChainStages']['Retail'],
                           label1Per=dataSummary['Perfume Co.']['ChainStages']['Part'],
                           label2Per=dataSummary['Perfume Co.']['ChainStages']['Trans'],
                           label3Per=dataSummary['Perfume Co.']['ChainStages']['Manuf'],
                           label4Per=dataSummary['Perfume Co.']['ChainStages']['Dist'],
                           label5Per=dataSummary['Perfume Co.']['ChainStages']['Retail'],
                           label1Com=dataSummary['Computer Co.']['ChainStages']['Part'],
                           label2Com=dataSummary['Computer Co.']['ChainStages']['Trans'],
                           label3Com=dataSummary['Computer Co.']['ChainStages']['Manuf'],
                           label4Com=dataSummary['Computer Co.']['ChainStages']['Dist'],
                           label5Com=dataSummary['Computer Co.']['ChainStages']['Retail'],
                           label1Air=dataSummary['Aircraft Co.']['ChainStages']['Part'],
                           label2Air=dataSummary['Aircraft Co.']['ChainStages']['Trans'],
                           label3Air=dataSummary['Aircraft Co.']['ChainStages']['Manuf'],
                           label4Air=dataSummary['Aircraft Co.']['ChainStages']['Dist'],
                           label5Air=dataSummary['Aircraft Co.']['ChainStages']['Retail']
                           )


# @app.route('/cereal_stages', methods=['GET','POST'])
# def ():
#     dataset1 = read_csv(path + '/data/Cereal_SD.csv', low_memory=False)
#     newdata = dataset1.drop(['xPosition', 'yPosition'], axis=1)
#     avgdD, countD, avgdM, countM, avgdP, countP, avgdT, countT, avgcT, avgcM, avgcP, avgcD = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#     for index, row in newdata.iterrows():
#         if str(row['Stage Name']).startswith("Dist_"):
#             countD = countD + 1
#             avgdD = avgdD + row['stageTime']
#             temp = str(row['stageCost']).lstrip("$").rstrip(" ")
#             avgcD = avgcD + float(temp)
#         elif str(row['Stage Name']).startswith("Manuf_"):
#             countM = countM + 1
#             avgdM = avgdM + row['stageTime']
#             temp = str(row['stageCost']).lstrip("$").rstrip(" ")
#             avgcM = avgcM + float(temp)
#         elif str(row['Stage Name']).startswith("Part_"):
#             countP = countP + 1
#             avgdP = avgdP + row['stageTime']
#             temp = str(row['stageCost']).lstrip("$").rstrip(" ")
#             avgcP = avgcP + float(temp)
#         elif str(row['Stage Name']).startswith("Trans_"):
#             countT = countT + 1
#             avgdT = avgdT + row['stageTime']
#             temp = str(row['stageCost']).lstrip("$").rstrip(" ")
#             avgcT = avgcT + float(temp)

#     dataCereal = {'StageTime': {'part': avgdP / countP, 'manuf': avgdM / countM,
#                                 'dist': avgdD / countD, 'trans': avgdT / countT},
#                   'StageCost': {'part': avgcP / countP, 'manuf': avgcM / countM,
#                                 'dist': avgcD / countD, 'trans': avgcT / countT}}

#     dataset_1 = read_csv(path + '/data/Cereal_LL.csv', low_memory=False, header=0)
#     key=list(dataset_1["sourceStage"])
#     value=list(dataset_1["destinationStage"])

#     incoming={}
#     outgoing={}

#     for i in range(len(key)):
#         if key[i] not in incoming:
#             incoming[key[i]]=[value[i]]
#         else:
#             incoming[key[i]].extend([value[i]])

#     for i in range(len(value)):
#         if value[i] not in outgoing:
#             outgoing[value[i]]=[key[i]]
#         else:
#             outgoing[value[i]].extend([key[i]])


#     stage_name= str(request.form.get('stage_id'))
#     print "node_name",stage_name
#     if stage_name:
#         n_count=1
#         if incoming.get(stage_name):
#             n_count+=len(incoming.get(stage_name))
#         if outgoing.get(stage_name):
#             n_count+=len(outgoing.get(stage_name))
#         x,y,z=50,50,100
#         x_data,y_data,z_data,label=[50],[50],[50],[stage_name]
#         if incoming.get(stage_name):
#             for i,item in enumerate(incoming[stage_name],1):
#                 if i%2==0:
#                     y_data.append(50+3*i)
#                 else:
#                     y_data.append(50-3*(i+1))
#                 x_data.append(30-2*i)
#                 z_data.append(50)
#                 label.append(item)
        
#         if outgoing.get(stage_name):
#             for i,item in enumerate(outgoing[stage_name],1):
#                 if i%2==0:
#                     y_data.append(50+3*i)
#                 else:
#                     y_data.append(50-3*(i+1))
#                 x_data.append(75+(2*i))
#                 z_data.append(50)
#                 label.append(item)
        
#         # print y_data,x_data,label
#         return render_template('multiplebarChart.html',y_data=y_data,x_data=x_data,z_data=z_data,label=json.dumps(label),n_count=n_count,
#                                 topic='Stage data of Cereal Co.', ylabel='Stages Time in Supply chain', y1label='Stages Cost in Supply chain',
#                                 x1name="Stage Time(days)", x1label="Stage Time", x2name="Stage Cost($)", x2label="Stage Cost",
#                                 label1='Parts', label2='Manufacture', label3='Transportation', label4='Distribution',
#                                 y1=dataCereal["StageTime"]['part'], y2=dataCereal["StageTime"]['manuf'], y3=dataCereal["StageTime"]['trans'], y4=dataCereal["StageTime"]['dist'],
#                                y5=dataCereal["StageCost"]['part'], y6=dataCereal["StageCost"]['manuf'], y7=dataCereal["StageCost"]['trans'], y8=dataCereal["StageCost"]['dist'])
#     return render_template('multiplebarChart.html',y_data=y_data,x_data=x_data,z_data=z_data,label=json.dumps(label),n_count=n_count,
#                                 topic='Stage data of Cereal Co.', ylabel='Stages Time in Supply chain', y1label='Stages Cost in Supply chain',
#                                 x1name="Stage Time(days)", x1label="Stage Time", x2name="Stage Cost($)", x2label="Stage Cost",
#                                 label1='Parts', label2='Manufacture', label3='Transportation', label4='Distribution',
#                                 y1=dataCereal["StageTime"]['part'], y2=dataCereal["StageTime"]['manuf'], y3=dataCereal["StageTime"]['trans'], y4=dataCereal["StageTime"]['dist'],
#                                y5=dataCereal["StageCost"]['part'], y6=dataCereal["StageCost"]['manuf'], y7=dataCereal["StageCost"]['trans'], y8=dataCereal["StageCost"]['dist'])



@app.route('/cereal_stages', methods=['GET','POST'])
def cereal_stages():
    dataset1 = read_csv(path + '/data/Cereal_SD.csv', low_memory=False)
    newdata = dataset1.drop(['xPosition', 'yPosition'], axis=1)
    avgdD, countD, avgdM, countM, avgdP, countP, avgdT, countT, avgcT, avgcM, avgcP, avgcD = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for index, row in newdata.iterrows():
        if str(row['Stage Name']).startswith("Dist_"):
            countD = countD + 1
            avgdD = avgdD + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcD = avgcD + float(temp)
        elif str(row['Stage Name']).startswith("Manuf_"):
            countM = countM + 1
            avgdM = avgdM + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcM = avgcM + float(temp)
        elif str(row['Stage Name']).startswith("Part_"):
            countP = countP + 1
            avgdP = avgdP + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcP = avgcP + float(temp)
        elif str(row['Stage Name']).startswith("Trans_"):
            countT = countT + 1
            avgdT = avgdT + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcT = avgcT + float(temp)

    dataCereal = {'StageTime': {'part': avgdP / countP, 'manuf': avgdM / countM,
                                'dist': avgdD / countD, 'trans': avgdT / countT},
                  'StageCost': {'part': avgcP / countP, 'manuf': avgcM / countM,
                                'dist': avgcD / countD, 'trans': avgcT / countT}}

    dataset_1 = read_csv(path + '/data/Cereal_LL.csv', low_memory=False, header=0)
    key=list(dataset_1["sourceStage"])
    value=list(dataset_1["destinationStage"])

    incoming={}
    outgoing={}

    for i in range(len(key)):
        if key[i] not in incoming:
            incoming[key[i]]=[value[i]]
        else:
            incoming[key[i]].extend([value[i]])

    for i in range(len(value)):
        if value[i] not in outgoing:
            outgoing[value[i]]=[key[i]]
        else:
            outgoing[value[i]].extend([key[i]])


    stage_name= str(request.form.get('stage_id'))
    if stage_name and stage_name!=None:
        n_count=1
        if incoming.get(stage_name):
            n_count+=len(incoming.get(stage_name))
        if outgoing.get(stage_name):
            n_count+=len(outgoing.get(stage_name))
        x,y,z=50,50,100
        x_data,y_data,z_data,label=[50],[50],[50],[stage_name]
        if incoming.get(stage_name):
            for i,item in enumerate(incoming[stage_name],1):
                if i%2==0:
                    y_data.append(50+3*i)
                else:
                    y_data.append(50-3*(i+1))
                x_data.append(35-2*i)
                z_data.append(50)
                label.append(item)
        
        if outgoing.get(stage_name):
            for i,item in enumerate(outgoing[stage_name],1):
                if i%2==0:
                    y_data.append(50+3*i)
                else:
                    y_data.append(50-3*(i+1))
                x_data.append(65+(2*i))
                z_data.append(50)
                label.append(item)
        
        # print y_data,x_data,label
        return render_template('multiplebarChart2.html',y_data=y_data,x_data=x_data,z_data=z_data,label=json.dumps(label),n_count=n_count,
                                topic='Stage data of Cereal Co.', ylabel='Stages Time in Supply chain', y1label='Stages Cost in Supply chain',
                                x1name="Stage Time(days)", x1label="Stage Time", x2name="Stage Cost($)", x2label="Stage Cost",
                                label1='Parts', label2='Manufacture', label3='Transportation', label4='Distribution',
                                y1=dataCereal["StageTime"]['part'], y2=dataCereal["StageTime"]['manuf'], y3=dataCereal["StageTime"]['trans'], y4=dataCereal["StageTime"]['dist'],
                               y5=dataCereal["StageCost"]['part'], y6=dataCereal["StageCost"]['manuf'], y7=dataCereal["StageCost"]['trans'], y8=dataCereal["StageCost"]['dist'])
    return render_template('multiplebarChart2.html',y_data=[],x_data=[],z_data=[],label=[],n_count=0,
                                topic='Stage data of Cereal Co.', ylabel='Stages Time in Supply chain', y1label='Stages Cost in Supply chain',
                                x1name="Stage Time(days)", x1label="Stage Time", x2name="Stage Cost($)", x2label="Stage Cost",
                                label1='Parts', label2='Manufacture', label3='Transportation', label4='Distribution',
                                y1=dataCereal["StageTime"]['part'], y2=dataCereal["StageTime"]['manuf'], y3=dataCereal["StageTime"]['trans'], y4=dataCereal["StageTime"]['dist'],
                               y5=dataCereal["StageCost"]['part'], y6=dataCereal["StageCost"]['manuf'], y7=dataCereal["StageCost"]['trans'], y8=dataCereal["StageCost"]['dist'])

@app.route('/perfume_stages', methods=['GET','POST'])
def perfume_stages():
    dataset2 = read_csv(path + '/data/Perfume_SD.csv', header=0)
    newdata = dataset2.drop(['xPosition', 'yPosition'], axis=1)
    avgdR, countR, avgdM, countM, avgdP, countP, avgdD, countD, avgcD, avgcM, avgcP, avgcR = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    for index, row in newdata.iterrows():
        if str(row['Stage Name']).startswith("Dist_"):
            countD = countD + 1
            avgdD = avgdD + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcD = avgcD + float(temp)
        elif str(row['Stage Name']).startswith("Manuf_"):
            countM = countM + 1
            avgdM = avgdM + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcM = avgcM + float(temp)
        elif str(row['Stage Name']).startswith("Part_"):
            countP = countP + 1
            avgdP = avgdP + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcP = avgcP + float(temp)
        elif str(row['Stage Name']).startswith("Retail_"):
            countR = countR + 1
            avgdR = avgdR + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcR = avgcR + float(temp)

    dataPerfume = {'StageTime': {'part': avgdP / countP, 'manuf': avgdM / countM,
                                 'dist': avgdD / countD, 'retail': avgdR / countR},
                   'StageCost': {'part': avgcP / countP, 'manuf': avgcM / countM,
                                 'dist': avgcD / countD, 'retail': avgcR / countR}}

    dataset_1 = read_csv(path + '/data/Perfume_LL.csv', low_memory=False, header=0)
    key=list(dataset_1["sourceStage"])
    value=list(dataset_1["destinationStage"])

    incoming={}
    outgoing={}

    for i in range(len(key)):
        if key[i] not in incoming:
            incoming[key[i]]=[value[i]]
        else:
            incoming[key[i]].extend([value[i]])

    for i in range(len(value)):
        if value[i] not in outgoing:
            outgoing[value[i]]=[key[i]]
        else:
            outgoing[value[i]].extend([key[i]])


    stage_name= str(request.form.get('stage_id'))
    if stage_name and stage_name!=None:
        n_count=1
        if incoming.get(stage_name):
            n_count+=len(incoming.get(stage_name))
        if outgoing.get(stage_name):
            n_count+=len(outgoing.get(stage_name))
        x,y,z=50,50,100
        x_data,y_data,z_data,label=[50],[50],[50],[stage_name]
        if incoming.get(stage_name):
            for i,item in enumerate(incoming[stage_name],1):
                if i%2==0:
                    y_data.append(50+3*i)
                else:
                    y_data.append(50-3*(i+1))
                x_data.append(35-2*i)
                z_data.append(50)
                label.append(item)
        
        if outgoing.get(stage_name):
            for i,item in enumerate(outgoing[stage_name],1):
                if i%2==0:
                    y_data.append(50+3*i)
                else:
                    y_data.append(50-3*(i+1))
                x_data.append(65+(2*i))
                z_data.append(50)
                label.append(item)

        # print y_data,x_data,label
        return render_template('multiplebarChart2.html',y_data=y_data,x_data=x_data,z_data=z_data,label=json.dumps(label),n_count=n_count,
            topic='Stage data of Perfume Co.', ylabel='Stages Time in Supply chain', y1label='Stages Cost in Supply chain',
                           x1name="Stage Time(days)", x1label="Stage Time", x2name="Stage Cost($)", x2label="Stage Cost",
                           label1='Parts', label2='Manufacture', label3='Distribution', label4='Retail',
                           y1=dataPerfume["StageTime"]['part'], y2=dataPerfume["StageTime"][
                               'manuf'], y3=dataPerfume["StageTime"]['dist'], y4=dataPerfume["StageTime"]['retail'],
                           y5=dataPerfume["StageCost"]['part'], y6=dataPerfume["StageCost"]['manuf'], y7=dataPerfume["StageCost"]['dist'], y8=dataPerfume["StageCost"]['retail'])


    return render_template('multiplebarChart2.html',y_data=[],x_data=[],z_data=[],label=[],n_count=0,
                        topic='Stage data of Perfume Co.', ylabel='Stages Time in Supply chain', y1label='Stages Cost in Supply chain',
                           x1name="Stage Time(days)", x1label="Stage Time", x2name="Stage Cost($)", x2label="Stage Cost",
                           label1='Parts', label2='Manufacture', label3='Distribution', label4='Retail',
                           y1=dataPerfume["StageTime"]['part'], y2=dataPerfume["StageTime"][
                               'manuf'], y3=dataPerfume["StageTime"]['dist'], y4=dataPerfume["StageTime"]['retail'],
                           y5=dataPerfume["StageCost"]['part'], y6=dataPerfume["StageCost"]['manuf'], y7=dataPerfume["StageCost"]['dist'], y8=dataPerfume["StageCost"]['retail'])


@app.route('/aircraft_stages', methods=['GET'])
def aircraft_stages():
    dataset3 = read_csv(path + '/data/Aircraft_SD.csv', header=0)
    newdata = dataset3.drop(['xPosition', 'yPosition'], axis=1)

    avgdR, countR, avgdM, countM, avgdP, countP, avgdT, countT, avgcT, avgcM, avgcP, avgcR = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for index, row in newdata.iterrows():
        if str(row['Stage Name']).startswith("Retail_"):
            countR = countR + 1
            avgdR = avgdR + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcR = avgcR + float(temp)
        elif str(row['Stage Name']).startswith("Manuf_"):
            countM = countM + 1
            avgdM = avgdM + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcM = avgcM + float(temp)
        elif str(row['Stage Name']).startswith("Part_"):
            countP = countP + 1
            avgdP = avgdP + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcP = avgcP + float(temp)
        elif str(row['Stage Name']).startswith("Trans_"):
            countT = countT + 1
            avgdT = avgdT + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcT = avgcT + float(temp)

    dataAircraft = {'StageTime': {'part': avgdP / countP, 'manuf': avgdM / countM,
                                  'retail': avgdR / countR, 'trans': avgdT / countT},
                    'StageCost': {'part': avgcP / countP, 'manuf': avgcM / countM,
                                  'retail': avgcR / countR, 'trans': avgcT / countT}}


    dataset_1 = read_csv(path + '/data/Aircarft_LL.csv', low_memory=False, header=0)
    key=list(dataset_1["sourceStage"])
    value=list(dataset_1["destinationStage"])

    incoming={}
    outgoing={}

    for i in range(len(key)):
        if key[i] not in incoming:
            incoming[key[i]]=[value[i]]
        else:
            incoming[key[i]].extend([value[i]])

    for i in range(len(value)):
        if value[i] not in outgoing:
            outgoing[value[i]]=[key[i]]
        else:
            outgoing[value[i]].extend([key[i]])


    stage_name= str(request.form.get('stage_id'))

    if stage_name and stage_name!=None:
        n_count=1
        if incoming.get(stage_name):
            n_count+=len(incoming.get(stage_name))
        if outgoing.get(stage_name):
            n_count+=len(outgoing.get(stage_name))
        x,y,z=50,50,100
        x_data,y_data,z_data,label=[50],[50],[50],[stage_name]
        if incoming.get(stage_name):
            for i,item in enumerate(incoming[stage_name],1):
                if i%2==0:
                    y_data.append(50+3*i)
                else:
                    y_data.append(50-3*(i+1))
                x_data.append(35-2*i)
                z_data.append(50)
                label.append(item)
        
        if outgoing.get(stage_name):
            for i,item in enumerate(outgoing[stage_name],1):
                if i%2==0:
                    y_data.append(50+3*i)
                else:
                    y_data.append(50-3*(i+1))
                x_data.append(65+(2*i))
                z_data.append(50)
                label.append(item)

        # print y_data,x_data,label
        return render_template('multiplebarChart2.html',y_data=y_data,x_data=x_data,z_data=z_data,label=json.dumps(label),n_count=n_count,
                        topic='Stage data of Aircraft Co.', ylabel='Stages Time in Supply chain', y1label='Stages Cost in Supply chain',
                           x1name="Stage Time(days)", x1label="Stage Time", x2name="Stage Cost($)", x2label="Stage Cost",
                           label1='Parts', label2='Manufacture', label3='Transportation', label4='Retail',
                           y1=dataAircraft["StageTime"]['part'], y2=dataAircraft["StageTime"][
                               'manuf'], y3=dataAircraft["StageTime"]['trans'], y4=dataAircraft["StageTime"]['retail'],
                           y5=dataAircraft["StageCost"]['part'], y6=dataAircraft["StageCost"]['manuf'], y7=dataAircraft["StageCost"]['trans'], y8=dataAircraft["StageCost"]['retail'])

    return render_template('multiplebarChart2.html',y_data=[],x_data=[],z_data=[],label=[],n_count=0,
         topic='Stage data of Aircraft Co.', ylabel='Stages Time in Supply chain', y1label='Stages Cost in Supply chain',
                           x1name="Stage Time(days)", x1label="Stage Time", x2name="Stage Cost($)", x2label="Stage Cost",
                           label1='Parts', label2='Manufacture', label3='Transportation', label4='Retail',
                           y1=dataAircraft["StageTime"]['part'], y2=dataAircraft["StageTime"][
                               'manuf'], y3=dataAircraft["StageTime"]['trans'], y4=dataAircraft["StageTime"]['retail'],
                           y5=dataAircraft["StageCost"]['part'], y6=dataAircraft["StageCost"]['manuf'], y7=dataAircraft["StageCost"]['trans'], y8=dataAircraft["StageCost"]['retail'])


@app.route('/computer_stages', methods=['GET'])
def computer_stages():
    dataset4 = read_csv(path + '/data/Computer_SD.csv', header=0)
    newdata = dataset4.drop(['xPosition', 'yPosition'], axis=1)

    avgdR, countR, avgdM, countM, avgdP, countP, avgdT, countT, avgcT, avgcM, avgcP, avgcR = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for index, row in newdata.iterrows():
        if str(row['Stage Name']).startswith("Retail_"):
            countR = countR + 1
            avgdR = avgdR + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcR = avgcR + float(temp)
        elif str(row['Stage Name']).startswith("Manuf_"):
            countM = countM + 1
            avgdM = avgdM + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcM = avgcM + float(temp)
        elif str(row['Stage Name']).startswith("Part_"):
            countP = countP + 1
            avgdP = avgdP + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcP = avgcP + float(temp)
        elif str(row['Stage Name']).startswith("Trans_"):
            countT = countT + 1
            avgdT = avgdT + row['stageTime']
            temp = str(row['stageCost']).lstrip("$").rstrip(" ")
            avgcT = avgcT + float(temp)

    dataComputer = {'StageTime': {'part': avgdP / countP, 'manuf': avgdM / countM,
                                  'retail': avgdR / countR, 'trans': avgdT / countT},
                    'StageCost': {'part': avgcP / countP, 'manuf': avgcM / countM,
                                  'retail': avgcR / countR, 'trans': avgcT / countT}}

    dataset_1 = read_csv(path + '/data/Computer_LL.csv', low_memory=False, header=0)
    key=list(dataset_1["sourceStage"])
    value=list(dataset_1["destinationStage"])

    incoming={}
    outgoing={}

    for i in range(len(key)):
        if key[i] not in incoming:
            incoming[key[i]]=[value[i]]
        else:
            incoming[key[i]].extend([value[i]])

    for i in range(len(value)):
        if value[i] not in outgoing:
            outgoing[value[i]]=[key[i]]
        else:
            outgoing[value[i]].extend([key[i]])


    stage_name= str(request.form.get('stage_id'))
    if stage_name and stage_name!=None:
        n_count=1
        if incoming.get(stage_name):
            n_count+=len(incoming.get(stage_name))
        if outgoing.get(stage_name):
            n_count+=len(outgoing.get(stage_name))
        x,y,z=50,50,100
        x_data,y_data,z_data,label=[50],[50],[50],[stage_name]
        if incoming.get(stage_name):
            for i,item in enumerate(incoming[stage_name],1):
                if i%2==0:
                    y_data.append(50+3*i)
                else:
                    y_data.append(50-3*(i+1))
                x_data.append(35-2*i)
                z_data.append(50)
                label.append(item)
        
        if outgoing.get(stage_name):
            for i,item in enumerate(outgoing[stage_name],1):
                if i%2==0:
                    y_data.append(50+3*i)
                else:
                    y_data.append(50-3*(i+1))
                x_data.append(65+(2*i))
                z_data.append(50)
                label.append(item)

        # print y_data,x_data,label
        return render_template('multiplebarChart2.html',y_data=y_data,x_data=x_data,z_data=z_data,label=json.dumps(label),n_count=n_count,
                         topic='Stage data of Computer Co.', ylabel='Stages Time in Supply chain', y1label='Stages Cost in Supply chain',
                           x1name="Stage Time(days)", x1label="Stage Time", x2name="Stage Cost($)", x2label="Stage Cost",
                           label1='Parts', label2='Manufacture', label3='Transportation', label4='Retail',
                           y1=dataComputer["StageTime"]['part'], y2=dataComputer["StageTime"][
                               'manuf'], y3=dataComputer["StageTime"]['trans'], y4=dataComputer["StageTime"]['retail'],
                           y5=dataComputer["StageCost"]['part'], y6=dataComputer["StageCost"]['manuf'], y7=dataComputer["StageCost"]['trans'], y8=dataComputer["StageCost"]['retail'])


    return render_template('multiplebarChart2.html',y_data=[],x_data=[],z_data=[],label=[],n_count=0,
                            topic='Stage data of Computer Co.', ylabel='Stages Time in Supply chain', y1label='Stages Cost in Supply chain',
                           x1name="Stage Time(days)", x1label="Stage Time", x2name="Stage Cost($)", x2label="Stage Cost",
                           label1='Parts', label2='Manufacture', label3='Transportation', label4='Retail',
                           y1=dataComputer["StageTime"]['part'], y2=dataComputer["StageTime"][
                               'manuf'], y3=dataComputer["StageTime"]['trans'], y4=dataComputer["StageTime"]['retail'],
                           y5=dataComputer["StageCost"]['part'], y6=dataComputer["StageCost"]['manuf'], y7=dataComputer["StageCost"]['trans'], y8=dataComputer["StageCost"]['retail'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
