import json, os

# {"number": "3", "unit": "inches", "place": "kitchen", "adjective": "small", "noun": "note"}

def run():
	full = input('Write in your fields in JSON format Ex. {"number": "3", "unit": "meters"...} \n')
	
	# check if input is empty
	if not full == '':
		# check if input is valid json
		try:
			valid = json.loads(full)

			# store the values into vars for later use
			num = valid["number"]
			unit = valid["unit"]
			place = valid["place"]
			adjective = valid["adjective"]
			noun = valid["noun"]
			
			print(f'num: {num}\n unit: {unit}\n place: {place}\n adjective: {adjective}\n noun: {noun}\n ')
			
			# check for length restrictions
			for a, b in valid.items():
				check = lambda b : True if (len(b) > 12) else False
				if check(b) == True:
					print(f"Character limit exceeded (15) on field: {a}")
			
			# check if file exists
			if not os.path.exists('./stories.json'):
				file = open('./stories.json','w+') 		# create a new file otherwise
				file.write('[')
				file.write(json.dumps(valid, indent=4, sort_keys=True))		# add the first data to it
				file.write(']')
				file.close()
			else:
				# file already exists, lets append

				# load all previous data
				this = open('./stories.json')
				data = json.load(this)

				# add our new data to the previous
				data.append(valid)

				# write new data into the file
				with open('./stories.json', 'w') as otherfile:
					json.dump(data, otherfile, indent=4)

		except:
			print('reason', valid)
			print("Input could not be converted to JSON. Give it another try.")
	else:
		print("Empty input.")

def save():
	the = {"number": "4", "unit": "meters", "place": "kitchen", "adjective": "small", "noun": "note"}
	if not os.path.exists('./stories.json'):
		file = open('./stories.json','w+')
		file.write('[')
		file.write(json.dumps(the, indent=4, sort_keys=True))
		file.write(']')
		file.close()
	else:
		# file already exists, lets append

		# load all previous data
		this = open('./stories.json')
		data = json.load(this)

		# add our new data to the previous
		data.append(the)

		# write new data into the file
		with open('./stories.json', 'w') as otherfile:
			json.dump(data, otherfile, indent=4)

run()