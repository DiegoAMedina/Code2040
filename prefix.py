import requests
import json
import ast		# convert string to dictionary


# python dictionary
dictionary = {'token':'e2f2c742e71d0ea6a9f5e02545228de9', 'array':''}


#-------------------------------------------- convert dictionary to json

# convert python dictionary to json string
dumps_dictionary = json.dumps(dictionary)

# convert json string to json dictionary
loads_dictionary = json.loads(dumps_dictionary)

#--------------------------------------- retrieve json dictionary & convert to python dictionary

# post will return a dictionary with "prefix" and "array"
dictionaryRequest = requests.post('http://challenge.code2040.org/api/prefix', loads_dictionary)

# converts dictionary into json dictionary
dictionaryRequest = dictionaryRequest.json()

print dictionaryRequest
