import json, csv



 #reading emails from a file
with open('emails.csv', 'rb') as csvfile:
	email_value = csv.reader(csvfile)
	email_val = email_value
	#print repr(email_value)
	i = 1
	row_count = sum(1 for t in email_value)
	total_row_count = row_count/2
	print row_count
	print total_row_count
	# count = 0
	# print repr(email_value)
	# email_val = csv.reader(csvfile)
	# print repr(email_value)
	# count = 0
	# for result in email_val:
	# 	print 'loop'
	# 	count +=1
	# 	if i%2==1:
	# 		print result[0], "\n"
	# 		# whois(row[0], api_key)

	# 	i+=1   # email value
	# print count

with open('emails.csv', 'rb') as csvfile:
	email_value = csv.reader(csvfile)
	count = 0
	for result in email_value:
		# print 'loop'
		count +=1
		if i%2==1:
			pass
			# print result[0], "\n"
			# whois(row[0], api_key)

		i+=1   # email value
	print count



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