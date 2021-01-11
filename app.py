# Execute app: run flask

import spacy
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from extract_keywords import extract_keywords
#from fuzzy import get_fuzzy_similarity
import subprocess

# if you want to download the large model
# subprocess.call("python -m spacy download en_core_web_lg",shell=True)
subprocess.call("python -m spacy download es_core_news_sm", shell=True)

app = Flask(__name__)
CORS(app)

# if you want to load the large model
# nlp = spacy.load("en_core_web_lg")
nlp = spacy.load("es_core_news_sm")
print("Loaded language model")


@app.route('/')
def hello_world():
    return 'Tiempo Arg keywords supervised generator!'


@app.route('/api/keywords', methods=['POST'])
def get_keywords():
    query_string = request.json.get("query_string")
    tags = request.json.get("tags")
    keywords = extract_keywords(nlp, query_string, tags)
    return jsonify(keywords=keywords)
