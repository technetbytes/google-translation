from nltk.corpus import stopwords
from googletrans import Translator
from nltk.tokenize import word_tokenize
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/service/ping', methods=['GET'])
def ping():
	return "YesIAmLive"

@app.route('/api/v1/service/getheader', methods=['GET'])
def get_header():
	if 'txt' in request.args:
		urdu_text = request.args['txt']
		translator = Translator()
		result = translator.translate(urdu_text, src='ur')
		tokens = word_tokenize(result.text)
		tokens_without_sw = [word for word in tokens if not word in stopwords.words()]
		sw = [word for word in tokens_without_sw if word.isalnum()]
		header = ("_").join(sw)
	else:
		return "Error: No TXT field provided. Please specify an TXT."

	return header	



app.run()