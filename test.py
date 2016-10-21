from bottle import route, run, template, debug
import pymongo
from pymongo import MongoClient


@route('/')
def index():
	connection = MongoClient('localhost', 27017)
	db = connection.video
	coll = db.movies
	collitems = coll.find()
	#return template('<b>Hello {{name}}</b>!', name=name)
	return template('index', items=collitems)


debug(True)
run(host='localhost', port=8080)

