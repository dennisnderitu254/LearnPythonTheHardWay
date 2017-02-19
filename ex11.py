print "How old are you?",

age = raw_input()

print "How tall are you?",

height = raw_input()

print "How much do you weigh?",

weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

# raw_input is a form of input that takes the argument in the form of a string whereas the input function takes the value depending upon your input. Say, a=input(5) returns a as an integer with value 5 whereas a=raw_input(5) returns a as a string of "5"