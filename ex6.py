# Study drill: Write a comment above each line explaining it

# First string with %d which displays a variable to users
x = "There are %d types of people." % 10

binary = "binary"

do_not = "don't"

# Placing the "binary" and "don't" string it the second string below
y = "Those who know %s and those who %s." % (binary, do_not)

# displays the string x is assigned to
print x

# displays the string y is assignes to
print y 


print "I said: %r." % x

print "I also said: '%s'." % y 

# on the line 28 the joke_evaluation is assigned a False! answer despite the question
hilarious = False


joke_evaluation = "Isn't that joke so funny?!  %r"

print joke_evaluation % hilarious

w = "This is the left side of..."

e = "a string with a right side."

# string concatenation done by the variables assigned to w and e respectively
print w + e

# %r is used for debugging since it displays the raw data of the variable
# the %r is the best for debugging whereas the other formats %s and %d are used to display variables to users

