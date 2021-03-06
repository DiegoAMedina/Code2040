import requests
import json
import ast		# convert string to dictionary

# python dictionary
dictionary = {'token': token removed, 'needle':''}


#-------------------------------------------- convert dictionary to json

# convert python dictionary to json string
dumps_dictionary = json.dumps(dictionary)

# convert json string to json dictionary
loads_dictionary = json.loads(dumps_dictionary)


#-------------------------------------------- retrieve json dictionary

# post will return a dictionary with "needle" and "haystack"
dictionaryRequest = requests.post('http://challenge.code2040.org/api/haystack', loads_dictionary)

# request returned a class and converting to a string
dictionaryRequest = str(dictionaryRequest.text)

# converting the string into a dictionary
dictionaryRequest = ast.literal_eval(dictionaryRequest)


#-------------------------------------------- find the needle in the haystack


index = 0

# iterate through dictionary to find the needle string in the haystack string
for key in dictionaryRequest['haystack']:
	
	if key == dictionaryRequest['needle']:
		break
	
	else:
		index += 1


loads_dictionary['needle'] = index

requests.post('http://challenge.code2040.org/api/haystack/validate', loads_dictionary)


