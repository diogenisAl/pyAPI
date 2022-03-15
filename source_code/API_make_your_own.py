import flask
from flask import request, jsonify

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
animals = [
    {'id': 0,
     'latin_name': 'Canis Lupus Familiaris',
     'english_name': 'Dog',
     'genus': 'Canis',
     'class': 'Mammalia'},
    {'id': 1,
     'latin_name': 'Felis Catus',
     'english_name': 'Cat',
     'genus': 'Felis',
     'class': 'Mammalia'},
    {'id': 2,
     'latin_name': 'Carassius Auratus',
     'english_name': 'Goldfish',
     'genus': 'Carassius',
     'class': 'Actinopterygii'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Pet Archive</h1>
<p>Mock API of with data for animals that are usually kept as pets.</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/api/animals/all', methods=['GET'])
def api_all():
    return jsonify(animals)

@app.route('/api/animals', methods=['GET'])
def api_id():
    # Check if an English Name was provided as part of the URL.
    # If English Name is provided, assign it to a variable.
    # If no English Name is provided, display an error in the browser.
    # URL example: http://127.0.0.1:5000/api/animals?english_name=Dog

    #if 'id' in request.args:
    #    id = int(request.args['id'])

    if 'english_name' in request.args:
        english_name = str(request.args['english_name'])
    else:

        return "Error: No english_name field provided. Please specify an english_name."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for animal in animals:
#        if animal['id'] == id:
        if animal['english_name'] == english_name:
            results.append(animal)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

# TODO: Make a function to return the animal with the name given in the GET method

# Run the app
if __name__ == '__main__':
    app.run()
