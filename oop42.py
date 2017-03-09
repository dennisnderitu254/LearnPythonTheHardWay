#Word drills

# class: Tell python to make a new type of thing

# Object: Two meanings,The most basic type of thing

# Instance: What you get when you tell python to create a class

# def : How to define a function inside a class 

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

# foo = X() means "set foo to an instance of class X."

# foo.M(J) means "From foo get the M function, and call it with parameters self,J."

# foo.K = Q  means "From foo get  the K attribute and set it to Q."



## Animal is-a object(yes, sort of confusing) look at extra credit

class Animal(object):
	pass



## Dog is-a animal
class Dog(Animal):
	def __init__(self,name):
		## class Dog has-a __init__ that takes self and name parameters

		self.name = name


## Cat is-a an  Animal
class Cat(Animal):
	def __init__(self, name):
		## class Cat has-a  __init__ that takes self and name  parameters

		self.name = name


## Person is-a object
class Person(object):
	def __init__(self, name):
		## class Person has-a __init__ that takes self and name parameters
		self.name = name

		## Person has-a pet of some kind
		self.pet = None


## Employee  is-a Person
class Employee(Person):

	def __init__(self,name, salary):

		##class Employee has-a __init__ that takes self , name and salary parameters

		super(Employee, self).__init__(name)
		## From super ,get the employee function and self parameter and super has-a __init__that takes name parameter
		self.salary = salary

## Fish is-a object 
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary is set to the pet attribute and  set it to satan
mary.pet = satan

## frank is-a Employee ang gets 120000
frank = Employee("Frank", 120000)

## frank is set to the pet attribute and then set to rover
frank.pet = rover

## set flipper to an instance of class Fish
flipper = Fish()

## set crouse to an instance in class Slamon
crouse = Salmon()

## set harry to an instance of class Halibut
harry = Halibut()

# foo = X() means "set foo to an instance of class X."