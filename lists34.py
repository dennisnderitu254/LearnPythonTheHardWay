
animals = ['bear' , 'python' , 'peacock', 'kangaroo' , 'whale' , 'platypus']

# print "The first (1st) animal is at 0 and is a bear." 

for i in range(len(animals)):
	print "The %d animal is at %d and is a %s" % (i+1 ,i, animals[i])

# "The animal at 0 is the 1st animal and is a bear."

for i in range(len(animals)):
	print "The animal at %d is the %d and is a %s " % (i, i+1, animals[i])

	