class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

        

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
    	print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"


son = Child()

son.implicit()
son.override()
son.altered()


# in this code , im not using the name Parent, since there is not a parent-child is-a relationship.This is a has-a relationship
# where CHILD has-a Other that is uses to get its work done.

# When to use inheritance or Composition

# Avoid multiple inheritance at all costs, as it's too complex to be reliable. If you're stuck with it, then be prepared to know the class hierarchy and spend time finding where everything is coming from.
# Use composition to package code into modules that are used in many different unrelated places and situations
# Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.
