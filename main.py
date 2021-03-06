import rake
import operator
import sys
from flask import Flask
from flask import request

rake_object = rake.Rake("stopwords_pt.txt", 4, 3, 0)

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'It works!'

@app.route('/rake', methods=["POST"])
def home(text=""):
	text = request.data
	text = text.decode('base64')
	keywords = rake_object.run(text)
	kw = []
	for name in keywords:
		if  name[1]>1:
			kw.append(name[0])

	myList = ','.join(map(str, kw))
	return myList
	
if __name__ == '__main__':
    app.run()