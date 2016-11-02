import requests # requests http
import json		# json dictionary



# dictionary with two keys
# token with api url and github with github link 
twoKeys = {'token': token removed, 'github':'https://github.com/DiegoAMedina/Code2040.git'}



#--------------------------------- convert python dictionary to a json dictionary

# converts twoKeys into json string
dumps_twoKeys = json.dumps(twoKeys)

# convert json string of twokeys to a json dictionary
loads_twoKeys = json.loads(dumps_twoKeys)


#--------------------------------- http request

# http request with the json dictionary passed in as a parameter
httpRequest = requests.post('http://challenge.code2040.org/api/register',loads_twoKeys)






