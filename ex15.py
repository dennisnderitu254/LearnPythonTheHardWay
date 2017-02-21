from sys import argv

# the file in the ex15_sample being located 
script, ex15_sample = argv

# the file ex15_sample is opened 
txt = open(ex15_sample)

# the file ex15_sample is printed out 
print "Here's your file %r:" % ex15_sample
print txt.read()



print "I'll also ask you to type it again:"
file_again = raw_input("> ")

#requests for the filemane to reopen the document again

txt_again = open(file_again)

# the text is printed out again
print txt_again.read()

txt_again.close()

