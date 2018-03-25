#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import rake
import operator
import sys
from flask import Flask

rake_object = rake.Rake("stopwords_pt.txt", 4, 3, 0)

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'It wórks!'

@app.route('/rake')
@app.route("/rake/<text>".decode('utf-8'))
def home(text=""):
	text = text.decode('utf-8')
	keywords = rake_object.run(text)
	kw = []
	for name in keywords:
		if  name[1]>1:
			kw.append(name[0])

	myList = ','.join(map(str, kw))

	return myList
	
if __name__ == '__main__':
    app.run()