import flask
import pandas as pd
import json
from flask import request, jsonify

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
corfiot_df = pd.read_csv("corfiot_dictionary.csv")

# Route of the main or index page (eg. website.com/)
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Corfiot Archive</h1>
<p>Mock API of with data for words in the Corfiot dialect and their meaning.</p>'''

# A route to return all of the available entries in our catalog (eg. website.com/api/words/all)
@app.route('/api/words/all', methods=['GET'])
def api_all():
    return json.loads(corfiot_df.to_json(force_ascii=False))

# A route to return one or more records based on the given word (website.com/api/words?word=λέξη)
@app.route('/api/words', methods=['GET'])
def api_word(word=None):
    # Check if a word was provided as part of the UR or as a function parameterL.
    # If a word is provided, assign it to a variable.
    # If no word is provided, display an error in the browser.
    if word is None:
        if 'word' in request.args:
            word = request.args['word']
        else:
            return "Error: No id field provided. Please specify an id."


    # Find the dataframe records containing the given word in the column 'Λήμμα'
    # Append the dataframe records containing the given word in the column 'Επεξήγηση' in the first dataframe
    # Create a json string from the dataframe

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return json.loads(results_json)

# Functions to make the API more accessible to third party users
def get_words():
    return ___()

def get_word(word):
    return ____(word)

if __name__ == '__main__':
    app.run()
