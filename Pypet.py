
cat = {
	'name' : "Giordan's poor cat",
	'age'  : 10,
	'weight': 9.5,
	'hungry': False
	}

def checkiffull(pet):
	if(pet['age'] * 10 > pet['weight']):
		pet['hungry'] = False
		print (cat['name'] + " is not hungry anymore")
	else:
		print (cat['name'] + " is soo hungry. It would appreciate it if you FEED it")
		pet['hungry'] = True

def feed(pet,number):                                      #Gains Weight
	pet['weight'] = pet['weight'] + number
	checkiffull(pet)

def torture(pet,number): 									#Loses Weight
	if(pet['weight'] - number <= 0):
		print("That is not possible")
		checkiffull(pet)
	else:
		pet['weight'] = pet['weight'] - number
	checkiffull(pet)

def growolder(pet,number):
	pet['age'] = pet['age'] + number

def growyounger(pet,number):
	pet['age'] = pet['age'] - number

def changename(pet,newname):
	pet['name'] = newname



print (cat)
print ("Make the cat grow skinner")
torture(cat, 5)
print (cat)

