from flask import Flask
from flask import render_template,request,make_response
import requests

app = Flask(__name__)

@app.route("/<num1>/<num2>/<sign>")
def default(num1,num2,sign):
	if sign == 'Sum':
		result=requests.get('http://sum:5000/'+num1+'/'+num2).text
	elif sign == 'Diff':
		result=requests.get('http://diff:5000/'+num1+'/'+num2).text
	elif sign == 'Multiply':
		result=requests.get('http://multiply:5000/'+num1+'/'+num2).text
	elif sign == 'Div':
		result=requests.get('http://div:5000/'+num1+'/'+num2).text
	return result

if __name__ == "__main__":
    	app.run(host="0.0.0.0", debug=True)




