import requests
import json

"""
# GET method to fetch data
url = 'https://jsonplaceholder.typicode.com/posts'

# Pass the response to a variable
r = requests.get(url)

# Extract the json representation of the file
data = r.json()

for i in data:
    print("Title: ", i['title'])
    print("Body: ", i['body'])


# print(json.dumps(data, indent=4))
print("Return of requests.get when fetching many files:", type(data))
print("Return type of requests.get when fetching many files: ", type(data[0]))

"""

"""

# Same as before but with only one record
url_1 = 'https://jsonplaceholder.typicode.com/posts/1'

r_1 = requests.get(url_1)
data_1 = data = r_1.json()

print(data_1)

# Now data is a dict because there aren't any other records
print("Return of requests.get when fetching a single file:", type(data_1))
print("Dict data from single file", data_1)

"""

#  POST method to upload data

# Sample JSON to upload
task = {'userId': 1, 'id': 1, 'title': 'foo', 'body': 'bar'}
task_json = json.dumps(task) # Optional, good practice

# Use the correct requests function to call the POST method for the json
resp = requests.post('https://jsonplaceholder.typicode.com/posts', json=task)

# Print response number. 201 => success
print(resp)
print('Created task with ID:', resp.json()["id"])

#  Because this is a dummy API, POST methods don't actually upload something
print(requests.get('https://jsonplaceholder.typicode.com/posts/101'))
