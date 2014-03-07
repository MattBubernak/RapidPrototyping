from flask import Flask
from flask import request
from flask import render_template 
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lib.db'
db = SQLAlchemy(app)

class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    gender = db.Column(db.String(120), unique=True)
    age = db.Column(db.Integer)
    speed = db.Column(db.String(120))

    def __init__(self, name, gender, age, speed):
        self.name = name
        self.gender = gender
        self.age = age
        self.speed = speed

    def __repr__(self):
        return 'ID: %r' % str(self.id)
        
class Book(db.Model):
    """"""
    __tablename__ = "books"
 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    author = db.Column(db.String)
    renterID = db.Column(db.String)
 
 
    #----------------------------------------------------------------------
    def __init__(self, title, genre, author, renterID):
        """"""
        self.title = title
        self.genre = genre
        self.author = author
        self.renterID = renterID
        
testData = [
	{
			"title" : "Into the Wild",
			"genre" : "History",
			"author" : "Bilbo Baggins",
			"renterID" : "24",
			"renterIDf" : "24"
	}
]

@app.route('/')
def hello_world():
	return 'Hello Matt and James - Rapid Prototyping 2014'

@app.route('/checkout')
def checkout(): 
	return render_template('checkout.html')

@app.route('/nud')
def nud():
	
	nud = Pets.query.all()
	print nud
	return "hi"
	
	
@app.route('/inquire')
def inquire(search = "false"):
	GetReq = "false" 
	print "nud"
	
	#Data = Book.query.filter_by(title="Into the Wild").all()
	#for item in Data: 
	#	print item.title
	
	
	return render_template('inquire.html', search = "true")
	#return render_template('inquire.html')

@app.route('/grabBook', methods=['GET'])
def grabBook(title = "null"):
	returnObject = {
			"title" : "failure",
			"genre" : "failure",
			"author" : "failure",
			"renterID" : "failure"
			}
	#print returnObject["author"]
	nud = request.args.get('title')
	print nud
	Data = Book.query.filter_by(title=nud).all()
	
	for item in Data: 
		#print item.title
		returnObject = {
			"title" : item.title,
			"genre" : item.genre,
			"author" : item.author,
			"renterID" : item.renterID
	}
	#return nud
	#print returnObject["author"]
	print "returning"
	return jsonify(result=returnObject)
		
	
	
@app.route('/addToDB', methods=['POST','GET'])
def addToDB():

	if request.method == "POST":
		nud = "nud"
        new_checkout = Book(request.json['title'],
                              request.json['genre'],
                              request.json['author'],
                              request.json['renterID'])
        
        # Add the record to the session object
        db.session.add(new_checkout)
      
        # commit the record the database
        db.session.commit()
        
	return "success"





if __name__ == '__main__':
	app.run()
