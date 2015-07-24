import json, csv
import os.path

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




#reading emails from a file
with open('emails.csv', 'rb') as csvfile:
	email_value = csv.reader(csvfile)
	print "total_row_count:" , total_count
	count = 0
	i = 1
	for result in email_value:
		count +=1
		if i%2==1:
			print interrupt_row_number
			if interrupt_row_number !=0:
				interrupt_row_number-=1
				continue

			pass
			print result[0], "\n"
			if i==21:
				break
			# whois(row[0], api_key)

		i+=1   # email value




'''
stats = {'facebook': 0, 'foursquare':0, 'twitter':0, 'googleplus':0}



s = open('json_return.txt', "r")
data = json.load(s)

print data

# STATS calculation

for p in data['socialProfiles']:
	#print p['type']
	if p['type'] == 'facebook':
		stats['facebook'] +=1
	elif p['type'] == 'twitter':
		stats['twitter'] +=1
	elif p['type'] == 'googleplus':
		stats['googleplus'] +=1
	elif p['type'] == 'foursquare':
		stats['foursquare'] +=1
		print data


print repr(stats)


s.close()
'''
i=0