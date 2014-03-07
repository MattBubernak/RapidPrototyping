from flask import Flask
from flask import request
from flask import render_template 


app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
	return 'Hello Matt and James - Rapid Prototyping 2014'

@app.route('/home')
def home():
	message = "Welcome to my Webpage"; 
	title = "My Webpage"; 
	
	data = [
	{
			"caption" : "CNN",
			"href" : "www.cnn.com"
	},
		
	{
			"caption" : "Twitter",
			"href" : "www.twitter.com"
	},
	{
			"caption" : "Facebook",
			"href" : "www.facebook.com"
	}
	]
	
	return render_template('home.html',navigation=data,a_variable = message, title = title)


@app.route('/find', methods=['POST','GET'])
def find():
	word = request.args.get('course')
	print("["+word+"]")
	word.rstrip()
	if word == 'CSCI1300':
		return "Find the classroom for CSCI1300 ... ATLAS 100. "
	if word ==  "CSCI2240":
		return "Find the classroom for CSCI2240 ..ITTL 1B50."
	else:
		return "Find the classroom for " + word + " ... Sorry. No result for " + word
	
	


@app.route('/notification')
def notification():
	return 'Get notificfation. To be implemented'


#@app.route('/search/<name>')


@app.route('/search')
def search(param=None,n=5):
	
	num = 5
	param = "any"
	maxNum = 5
	
	#check to see if a number was provided 
	if (request.args.has_key('n')):
		num = request.args.get('n')
	#check to see if a search param was provided 
	if (request.args.has_key('param')):
		param = request.args.get('param')
	
	newData = data

	#if we need to filter the data 
	if ( int(num) < 5 or (param != "any")):
		#store count of number of elements we've used
		count = 0; 
		#clear current data
		newData = []
		#loop through all data 
		for nud in data:
			#if we havent hit max num of elements
			if (count < int(num)):
				#if we are looking at any parameter or it matches
				if ((param != "any" and nud["breed"] == param) or (param == "any")):
					#append data and update count
					newData.append(nud)
					count = count+1
				
	return render_template('search.html',param=param,data=newData,n=num)


@app.route('/view/<string:petID>')
def view(petID="null"):
	exi = "false"
	#getpetID
	newData = []
	for nud in data:
		if (nud["petID"] == petID):
			newData.append(nud)
			exi = "true"
	return render_template('view.html',data=newData,petID = petID,exi = exi)

@app.route('/breed')
def breed(breed="null"):
	
	breed = "null"
	exi = "false"
	newData = breedData
	#get breed
	if (not request.args.has_key('breed')):
		exi = "none"
	breed = request.args.get('breed')
	newData = []
	for nud in breedData:
		if (nud["name"] == breed):
			newData.append(nud)
			exi = "true"
	return render_template('breed.html',data=newData,exi = exi)





if __name__ == '__main__':
	app.run()
