import json

#  In terminal: curl -o data.json https://jsonplaceholder.typicode.com/posts

#  Open data.json file
f = open('data.json', "r")

#  Load data from json file to data variable.
#  Because there are multiple items the data type is a list.
#  When there is only one item it usually will be a dict
data = json.load(f)

for i in data:
    print("Title: ", ____)
    print("Body: ", ____)


# Use json.dumps to
data_json = json.dumps(data, indent=4)

f.close()
