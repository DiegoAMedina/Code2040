import requests
import json



# python dictionary with api token and string variable
dictionary = {'token': token removed, 'string':''}



#-------------------------------------------- convert dictionary to json

# convert python dictionary to json string
dumps_dictionary = json.dumps(dictionary)

# convert json string to json dictionary
loads_dictionary = json.loads(dumps_dictionary)



#-------------------------------------------- retrieve string to be reversed and reversal

reverseStr = requests.post('http://challenge.code2040.org/api/reverse', loads_dictionary)

reverseStr = str(reverseStr.text)

# loop will reverse the given string
# length of string / 2 so it only loops the necessary amount of times, which is half of the length of the string


length = len(reverseStr) / 2


#------you can reverse a string using [::-1] but lets use a for loop.

# create a list out of the string to be able to manipulate it. 
strList = list(reverseStr)


for i in range (0, length ):
	temp = strList[i]
	strList[i] = strList[ len(reverseStr) - i - 1]
	strList[ len(reverseStr) - i - 1] = temp
	
	
# convert list back to a string	
reverseStr = "".join(strList)	

	
#-------------------------------------------- return the reversed string


loads_dictionary['string'] = reverseStr

validate = requests.post('http://challenge.code2040.org/api/reverse/validate',loads_dictionary)
