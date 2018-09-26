# 5 - objects

Programs in python don't have to be object-oriented like in other programming languages (See Java). You can think of an *object* as a complex variable, with functions and properties. Functions inside of an object are called "methods", and variables inside an object are called "attributes".

## Agenda
- What's an object/class?
- Object-oriented?
- Why is this useful?

> See https://www.w3schools.com/python/python_classes.asp for more examples
> See http://introtopython.org/classes.html#Inheritance for inheritance

## What's an object?
Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template (or blueprint) to create your objects.

You'd create your object using a *constructor*, which is a starting function that sets variables for your object. You may see the keyword *self*, this refers to the object itself. 

Each time you use the class to create an object, you create a new *instance* of it.

What kind of things can go in an object?

Let's have a pseudocode example of both a class and object: (pseudocode is code that gets the point across, but doesn't have valid syntax)
```
## class below ##
blueprint Dog:
    
    constructor(name_param,breed_param,age_param,height_param):
        self.name = name_param
        self.breed = breed_param
        self.age = age_param
        self.height = height_param

    method print_info():
        print(self.name + " is a " + self.breed + ", is " + self.age + " years old, and is " + self.height + " inches tall")
# end Dog blueprint(class)

## object below ## 
bud = Dog("Bud","Golden Retriever", 3, 31)    # <- this is an instance of a dog

bud.print_info()
## OUTPUT ##
# Bud is a Golden Retriever, is 3 years old, and is 31 inches tall"

```

The above example shows the basics of classes and objects. The `bud` object we created was an instance of the `Dog` *class*. We set the default variables, and printed them out using the `print_info()` method.

Let's show some real syntax. Below is the python syntax for what we did above, with some comments explaining a few things.

```python
class Dog:
    # below is the contructor, this gets called when you call Dog()
    def __init__(self,nam,bred,ag,ht,ownr="No one"):
        self.name = nam
        self.breed = bred
        self.age = ag
        self.height = ht
        self.owner = ownr   # The ownr syntax above sets a default value of "No one". You can put in values if you want, but you don't have to

    # Note: The self parameter is a reference to the class instance itself, and is used to access variables that belongs to the class.

    def print_dog_info(self):
        print(self.name + " is a " + self.breed + ", is " + str(self.age) + " years old, and is " + str(self.height) + " inches tall, and his owner is " + self.owner)

    def adopt(self,new_owner):
        self.owner = new_owner
# End Dog class


bud = Dog("Bud","Golden Retriever", 3, 31)    # <- this is an instance of a dog
bud.print_dog_info()

answer = input("You can adopt " + bud.name + ", enter your name to adopt him! ")
bud.adopt(answer)
bud.print_dog_info()

## OUTPUT ##
# ssafari@meshinprod12 ~/python-101 $ python3.6 5_objects/examples/dog.py
# Bud is a Golden Retriever, is 3 years old, and is 31 inches tall, and his owner is No one
# You can adopt Bud, enter your name to adopt him! Seb
# Bud is a Golden Retriever, is 3 years old, and is 31 inches tall, and his owner is Seb
# ssafari@meshinprod12 ~/python-101 $
```

## Object-oriented?
Python is object-oriented, what does that mean? Object-oriented programming, or OOP for short, focuses on building reusable blocks of code called classes. When you want to use a class in one of your programs, you make an object from that class, which is where the phrase "object-oriented" comes from. Python itself is not tied to object-oriented programming, but you will be using objects in most or all of your Python projects.

Why use an object? I could have just made `bud` into a dict? 
This is true, we could have had this dictionary below:

```python
bud = {"name":"Bud",
        "breed":"Golden Retriever",
        "age":3,
        "height":31,
        "owner":"No one"}
print(bud['name'] + " is a " + bud['breed'] " ...")
```

But instead we chose to create an object. One of the main reasons for this is that it lets you keep your code in an organized fashion. We also can write methods to modify the data in predictible ways, instead of modifying it wherever the dict lies. 

Example (Of bad practice...)

```python
bud['owner'] = "Seb"
print(bud['name'] + " owner is  " + bud['owner'] " ...")

bud['age'] = bud['age'] + 1     # This could be bud.birthday() instead

```

## Why is this useful?
Objects let you have full control of your data in an orginized way, and let you modify that data in an organized way. This lets you create more powerful and clean programs.
