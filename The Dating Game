
import requests 
import json


dictWithToken = {'token': token removed,'datestamp':''}


# retrieving json dictionary from code2040
dictionaryRequest = requests.post('http://challenge.code2040.org/api/dating', dictWithToken)
dictionaryRequest = dictionaryRequest.json()

timeStamp = dictionaryRequest['datestamp']


# Parsing the timestamp to individual variables to be able to manipulate them
year = int( timeStamp[:4] )
month = timeStamp[5:-13] 
day = int( timeStamp[8:-10] )
hours = int( timeStamp[11:-7] )
minutes = int( timeStamp[14:-4] )
seconds = int( timeStamp[17:-1] )
interval = int( dictionaryRequest['interval'] )

#--------------------------------------- Determine how many minutes there are in the interval

#first check how many minutes there are in the interval to add them to the minutes and the left to the seconds
minutes += ( interval / 60 )
seconds += ( interval - ( (interval / 60) * 60) )

# if there is more than 60 seconds then add one more minutes and subtract 60 from seconds
if seconds >= 60:
	minutes += 1
	seconds -= 60
	
#--------------------------------------- Determine how many hours there are in the minutes

hours += ( minutes / 60 )
minutes = ( minutes - ( (minutes / 60) * 60 ) )

if minutes >= 60:
	hours += 1
	minutes += minutes - 60
	
#--------------------------------------- Determine if hours are greater than 48, if so add one to the day

if hours >= 24:
	hours -= 24
	day += 1

	if hours >= 24:
		hours -= 24
		day += 1

	
#--------------------------------------- Edit dictionary with new datestamp

# Converting the variables back to strings to be able to add them to the dictionary
year = str(year)
month = str(month)
day = str(day)
hours = str(hours)
minutes = str(minutes)
seconds = str(seconds)


# Adding "0" in front of the numbers to return the timestamp identical to the requirements asked by Code 2040
if len(month) < 2:
	month = "0" + month

if len(day) < 2:
	day = "0" + day

if len(hours) < 2:
	hours = "0" + hours

if len(minutes) < 2:
	minutes = "0" + minutes

if len(seconds) < 2:
	seconds = "0" + seconds


# new datestamp in Code 2040 format
newDateStamp = year + "-" + month + "-" + day + "T" + hours + ":" + minutes + ":" + seconds + "Z"

# Assigning the new datestamp to the dictionary
dictWithToken['datestamp'] = newDateStamp
	
	
	
#--------------------------------------- Request post url

requestsContents = requests.post('http://challenge.code2040.org/api/dating/validate', json = dictWithToken)

print requestsContents.content



#--------------------------------------- Debugging outputs


print dictionaryRequest
#print timeStamp
'''
print "year:", year
print "month: ", month
print "day:", day
print "hours:", hours
print "minutes:", minutes
print "seconds:", seconds
print "interval:", interval
'''
#print "new date stamp:", newDateStamp

print dictWithToken

	
	
	
	
	
	
	
