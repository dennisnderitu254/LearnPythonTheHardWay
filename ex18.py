# working with functions

# Functions do 3 things

# 1.They name pieces of code the way variables name strings and numbers

# 2.They take arguments the way your scripts take argv

# 3.Using 1 and 2 they ley you make your own "mini-scripts" or "tiny commands."


# this one is like your scripts with  argv 

# the * in *args tells python to take all the arguments to the function and then put them in args as a list.

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok,  thats *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1 %r, arg2: %r " % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r " % arg1

	# this one takes no arguements
def print_none():
	print "I got nothin'."

print_two ("Dennis","Nderitu")
print_two_again("Dennis","Nderitu")
print_one("First!")
print_none()

"To 'run', 'call' or 'use' a function all mean the same thing."

