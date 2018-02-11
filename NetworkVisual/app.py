from flask import Flask, render_template,json
app = Flask(__name__)


import pandas as pd 
import ggplot
import matplotlib.pyplot as plt
import io
import base64

@app.route('/')
def showList():
    return render_template('list.html')

@app.route('/plot',methods=['GET','POST'])
def visualization():
	cereal = pd.read_csv('cereal_data.csv', low_memory=False)
	x,y =cereal['Stage Name'], cereal['stageTime']           
	dataPoints=[]
	data={'x':1,'y':2}             
	# for i,j in zip(x,y):
	# 	dataPoints.append({ 'label':x , 'y':y })
	# print dataPoints
	# data={'type': "bar",'dataPoints':dataPoints}
	# response = app.response_class(response=json.dumps(data),status=200,mimetype='application/json')
	return json.dumps(data)

	# return render_template('index.html',value =plot_url)


if __name__ == "__main__":
	app.debug = True
	app.run()