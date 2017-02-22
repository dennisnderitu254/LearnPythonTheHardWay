def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" %  cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


# Using the function , you can give the functions directly
print "We can just give the function numbers directly:"

cheese_and_crackers(20,30)

# Using the function , You can also use variables from your script
print "OR, we can use variables from our script:"
amount_of_cheese = 10 
amount_of_crackers = 50

# calling the function cheese_and_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# using the function to call cheese_and_crackers whern doing some math inside it
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


#Using the function , you can combine variables and math to achieve the result
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


print "We can do some simple math inside:"
cheese_and_crackers(1000 + 500 , 900 + 250)

print "We can also use variables in our script directly:"
cheese_and_crackers(2000,3000)

