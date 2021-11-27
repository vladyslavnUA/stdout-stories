import json, os

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
			print("");print("################################")
			print("");print("Your Generated Story: ")
			print(f"One day Anna was walking her {num} {unit} commute to {place} and found a {adjective} {noun} on the ground.")
			print("");print("################################");print("")
		except:
			print("Input could not be converted to JSON. Give it another try.")
	else:
		print("Empty input.")

run()