# Execute app: run flask

import spacy
from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_cors import CORS, cross_origin
from extract_keywords import extract_keywords
from textRank import TextRank4Keyword
#from fuzzy import get_fuzzy_similarity
import subprocess

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000)

# CORS(app)

# if you want to download the large model
# subprocess.call("python -m spacy download en_core_web_lg",shell=True)
subprocess.call("python -m spacy download es_core_news_sm", shell=True)



# if you want to load the large model
# nlp = spacy.load("en_core_web_lg")
nlp = spacy.load("es_core_news_sm")
print("Loaded language model")


# A decorator used to tell the application 
# which URL is associated function 
@app.route('/', methods= ["GET", "POST"])
def main():
    return render_template("index.html")

# @app.route('/api/keywords', methods =["GET", "POST"]) 
# def gfg(): 
#     if request.method == "POST": 
#        # getting input with name = fname in HTML form 
#        query_string = request.form.get("query_string")
#        #tags = request.form.get("tags")
#        #keywords = extract_keywords(nlp, query_string, tags)
#        keywords = extract_keywords(nlp, query_string)
       
#        #return redirect(url_for("user",usr = keywords))
#        return jsonify(text=query_string, keywords=keywords)
#        # getting input with name = lname in HTML form  
#        #last_name = request.form.get("lname")  
#        #return "Your name is "+first_name + last_name 
#     return render_template("form.html") 

@app.route('/api/textrank', methods =["GET", "POST"]) 
def get_textrank(): 
    if request.method == "POST": 
        tr4w = TextRank4Keyword()
        # query_string = request.form.get("query_string")
        # keywords_qty = int(request.form.get("keywords_qty"))
        query_string = request.json.get("query_string")
        keywords_qty = int(request.json.get("keywords_qty"))
        tr4w.analyze(query_string, candidate_pos=[
                    'NOUN', 'PROPN', 'ADJ'], window_size=4, lower=False)
        keywords = tr4w.get_keywords(keywords_qty)
        return jsonify(keywords=keywords,text = query_string)
    return render_template("form2.html") 

# @app.route("/<usr>")
# def user(usr):
#     return f"<p>{usr}</p>"

# @app.route('/api/keywords2', methods=['POST'])
# def get_keywords():
#     query_string = request.json.get("query_string")
#     tags = request.json.get("tags")
#     keywords = extract_keywords(nlp, query_string, tags)
#     return jsonify(keywords=keywords)


# @app.route('/api/textrank2', methods=['POST'])
# def get_textrank():
#     tr4w = TextRank4Keyword()
#     query_string = request.json.get("query_string")
#     tr4w.analyze(query_string, candidate_pos=[
#                  'NOUN', 'PROPN'], window_size=4, lower=False)
#     keywords = tr4w.get_keywords(10)
#     return jsonify(keywords=keywords)

