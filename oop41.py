#Word drills

# class: Tell python to make a new type of thing

# Object: Two meanings,The most basic type of thing

# Instance: What you get when you tell python to create a class

# def : How to definf a function inside a class 

#self: Inside the function is a class, self is a variable for the instance/object being accessed

#inheritance: The concept that one class can inherit traits from another class,much like you and your parents

#composition: The concept that a class can he composed of other classes as parts,much like how a car owns wheels.

#attribute: A property classes have that are from composition and are usually variables.

# is-a : A phrase to say tha something inherit from another,as in a "salmon" is-a "fish."

# has-a: A phrase to say something is composed of other things or has a trait,as is " a salmon has a mouth."





#Phase Drills

# classX(Y) means "Make a class named X that is-a Y."

# class X(object):def__init__(self,J)  means "Class X has-a __init__ that takes self and J parameters."

# class X(object):def M(self,J) means "class X has-a function named M that takes self and  J parameters."

# foo =X() means "set foo to an instance of class X."

# foo.M(J) means "From foo get the M function, and call it with parameters self,J."

# foo.K = Q  means "From foo get  the K attribute and set it to Q."


import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class subaru(automobile):":
      "Make a class named subaru that is-a automobile.",
    "class subaru(object):\n\tdef __init__(acc, speed)" :
      "class subaru has-a __init__ that takes acc and speed parameters.",
    "class subaru(object):\n\tdef topspeed(acc, speed)":
      "class subaru has-a function named topspeed that takes acc and speed parameters.",
    " topspeed = subaru()":
      "Set topspeed to an instance of class subaru.",
    "topspeed.topspeed(speed)":
      "From subaru get the topspeed function, and call it with parameters acc, speed.",
    "subaru.speed = 'X'":
      "From subaru get the speed attribute and set it to 'X'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"



# result = sentence[:] - This is a python way of copying a list.You're using the list slice syntax [:] to effectively make a slice from the very first element to the very last one.