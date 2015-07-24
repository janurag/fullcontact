import requests
import json
import csv
import time
from datetime import datetime, timedelta
import os.path


REQUEST_LATENCY = 0.2
next_req_time  = datetime.fromtimestamp(0)
print "\nnext_req_time", next_req_time


api_key = '891f653fab77f251'
url = "https://api.fullcontact.com/v2/person.json"
stats = {'facebook': 0, 'foursquare':0, 'twitter':0, 'googleplus':0}


interrupt_row_number = 0
x = os.path.isfile('interrupt_handle.csv')


####  Interrupt Handling START #####
if x!=True:
	# create file and store count value
	total_row_count = 0
	with open('emails.csv', 'rb') as csvfile:
		email_value = csv.reader(csvfile)
		email_val = email_value
		#print repr(email_value)
		i = 1
		row_count = sum(1 for t in email_value)
		total_row_count = row_count/2
		# print row_count
		print total_row_count
		f = open("interrupt_handle.csv", "w+")
		fcsv = csv.writer(f, delimiter=",")
		fcsv.writerow([total_row_count, 0])


else:
	pass
	interrupt_handle = open('interrupt_handle.csv', 'r+')
	int_handle_read = csv.reader(interrupt_handle)
	for row in int_handle_read:
		print repr(row) 
		total_count = int(row[0])
		interrupt_row_number = int(row[1])+3

#### Interrupt Handling END ####








## function for requesting data
def whois(email, api_key):
	wait_function()
	element = {}
	element['apiKey'] = api_key
	element['email'] = email
	#now = datetime.now()
	r = requests.get(url, params=element)
	print r.url, "\n"
	print repr(r.headers), "\n"
	print r.headers, "\n"

	data = json.loads(r.text)
	result = {}
	result['email'] = email
	result['contact'] = data

	# STATS calculation
	if data['status'] == 200:
		for p in data['socialProfiles']:
			print p['type']
			if p['type'] == 'facebook':
				stats['facebook'] +=1
			elif p['type'] == 'twitter':
				stats['twitter'] +=1
			elif p['type'] == 'googleplus':
				stats['googleplus'] +=1
			elif p['type'] == 'foursquare':
				stats['foursquare'] +=1
		print data

	update_rate_limit(r.headers)    #updating rate limit

	# writing in csv file where first row is email And second row is json data
	with open('contact_csv.csv', 'a+') as fcsv:
		fcsv_writer = csv.writer(fcsv, delimiter=",")
		fcsv_writer.writerow([result['email'], data['status'], result['contact']])
	

def wait_function():
	print "wait_function\n"
	now = datetime.now()
	print "time now:", now
	if next_req_time > now:
		t = next_req_time - new
		print "\ntime difference:", t
		time.sleep(t.total_seconds())

def update_rate_limit(hdr):
	print "update_rate_limit\n"
	remaining = float(hdr['X-Rate-Limit-Remaining'])
	reset = float(hdr['X-Rate-Limit-Reset'])
	spacing = reset / (1.0 + remaining)
	delay = spacing - REQUEST_LATENCY
	next_req_time = datetime.now() + timedelta(seconds=delay)




 #reading emails from a file
with open('emails.csv', 'rb') as csvfile:
	email_value = csv.reader(csvfile)
	print "total_row_count:" , total_count

	#print repr(email_value)
	i = 1
	for row in email_value:
		#print 'loop'
		if i%2==1:
			print interrupt_row_number
			if interrupt_row_number !=0:
				interrupt_row_number-=1
				continue

			print row[0], "\n"
			whois(row[0], api_key)

		i+=1   # email value
	print repr(stats)
	with open('contact_csv.csv', 'a+') as fcsv:
		fcsv_writer = csv.writer(fcsv, delimiter=",")
		fcsv_writer.writerow(["facebook", stats['facebook'], "foursquare",stats['foursquare'], "twitter", stats['twitter'], "googleplus", stats['googleplus']])



# test email list and 
# email_valuex = ['munender9927@gmail.com', 'marrisridhar2015@gmail.com']
# for rowx in email_valuex:
# 	email = rowx
# 	whois(email, api_key)





####  TESTING CODE   #####
# #  #reading data
# f = open('contact.txt', 'rb')
# x = json.load(f)
# print x['email']
# ## testing with csv
# fcsv = open('contact_csv.csv', 'a+')
# fcsv_writer = csv.writer(fcsv, delimiter=",")
# fcsv_writer.writerow([x['email'], x['contact']])
# fcsv_writer.writerow([x['email'], x['contact']])

# fcsv.close()
# testing writing in csv file
 

# print x
