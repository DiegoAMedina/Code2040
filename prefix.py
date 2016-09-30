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

#-------------------------------------- create new array with out the words including the prefix

# new variable to make the code easier to read.
prefix = dictionaryRequest['prefix']

# newArray variable will be the string of the new array without the words beginning with the prefix given.
newList = []

iterator = 0

# iterates through array of strings
for key in dictionaryRequest['array']:
	# checks to see if a word begins with the prefix provided
	if (key.startswith( prefix, 0, len(prefix) ) ):
		continue
	# if it does not start with it then add it to the newArray
	else:
		newList.append( str(key) )

newDictionary = {'token':'e2f2c742e71d0ea6a9f5e02545228de9', 'array': newList}
 
#-------------------------------------- convert new python dictionary to json dictionary

r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = newDictionary) 

print r.content
 


