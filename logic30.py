people = 10000

cars = 4000

trucks = 1500


if cars > people:
	print "We should take the cars."

elif cars < people:
	print "We should not take the cars."

else:
	print "We can't decide."


if  trucks > cars:
	print "That's too many trucks."

elif trucks < cars:
	print "Maybe we could take the trucks."

else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."

else:
	print "Fine, let's stay home then."


# What happens if multiple elif blocks are true ?
# Python starts and the top runs the first block that is true, so it runs only the first one

