import os
import sys
import json
import datetime
import requests

from flask import Flask, request, render_template, redirect, session

app = Flask(__name__,static_url_path='/static')

GENERAL_INFO = {
	'Total users': 100,
	'Total songs': 6726,
	'Training songs': 4721,
	'Test songs': 2005
}

USERS_LIST = [
	'1a849df9dabb15845eb932d46d81e2fd77176786',
	'1b704d4cddabea8258bd93497fcb73eab32fa592',
	'2e37aa820994c7e8465721a6a6ee78f48fc4df7a'
]

METHODS = {
	'fbed': {
		'title': 'Feature-Based',
		'subtitle': 'Euclidean Distance'
	},
	'fbcs': {
		'title': 'Feature-Based',
		'subtitle': 'Cosine Similarity'
	},
	'ptt': {
		'title': 'Pre-Trained',
		'subtitle': 'Tags'
	},
	'ptped': {
		'title': 'Pre-Train. (Pen.)',
		'subtitle': 'Euclidean Distance'
	},
	'ptpcs': {
		'title': 'Pre-Train. (Pen.)',
		'subtitle': 'Cosine Similarity'
	}
}

METRICS = {
	'Correct Predictions': 'TP',
	'Precision@k': 'precision',
	'Recall@k': 'recall',
	'Average Precision': 'average precision',
	'Reciprocal Rank': 'reciprocal rank'
}

RESULTS = {}

def get_file_info(filename,path=None):
	if not path:
		path = filename + '.json'
	else:
		path = path + filename + '.json'
	with open(path) as json_file:
		data = json.load(json_file)
	return data

METHODS_INFO = get_file_info('data/methods_info')
USERS_INFO = get_file_info('data/users_info')
SONGS_INFO = get_file_info('data/songs_info')

USERS_LIST = []

for user in USERS_INFO.keys():
	if len(USERS_LIST) < 50:
		USERS_LIST.append(user)

print(USERS_LIST)

USERS = {}

for user in USERS_LIST:
	for method in METHODS.keys():
		data = get_file_info(user,'data/' + method + '/')
		if user not in RESULTS:
			RESULTS[user] = {}
		RESULTS[user][method] = data

@app.route('/', methods=['GET','POST'])
def main():
	return render_template('index.html',general_info=GENERAL_INFO, users_list=USERS_LIST, results=RESULTS, methods=METHODS, metrics=METRICS, methods_info=METHODS_INFO, users_info=USERS_INFO, songs_info=SONGS_INFO, random=True)

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True, port=int(os.environ.get("PORT", 8888)), use_reloader=False)