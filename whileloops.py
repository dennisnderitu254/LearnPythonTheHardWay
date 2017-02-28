def f(i,x,numbers):
    if (i < x):
        print "At the top i is %d" %i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" %i
        f(i,x,numbers)
    return numbers

numbers = f(0,6,[])
for num in numbers:
    print num

# The above code is about a function that had been derived from a while-loop


# A for-loop can only iterate (loop) "over" collections of things.
# A while loop can do any kind of iteration (looping )you require.


# The while-loop still remains here in the code below

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num


