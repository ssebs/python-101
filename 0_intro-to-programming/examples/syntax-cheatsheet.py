# Syntax CheatSheet 
# Examples of valid python3 that covers lots of topics

## Basics: data types ##

#primitives
int1 = 4
float1 = float(3.5)
double1 = 3.14
char1 = 'x'
string1 = "Hello!"

multi_line_string = '''It start's here
blah blah blah
and ends here!'''

#data structures
list1 = ["item1","item2","item3"]
dictionary1 = {"key1":"value1", "key2":"value2"}

## Basics: logic ##
if int1 < double1:
    print(str(int1) + " is less than " + str(double1))
    # Note that we have to cast to a string before printing it using str()
elif char1 in string1:
    print(char1 + " is in " + string1)

if 'h' in string1 and string1.endswith("!"):
    print("h is in " + string1)
elif float1 != double1 or 'x' not in char1 :
    print(str(float1) + " is not " + str(double1) + " or x not in " + char1)

## Basics: string manipulation
print(string1.lower())
print(string1.upper())
print(string1.capitalize())
print(len(string1))
print(string1[:3])
print(string1[:-1])
print(string1[1:])

## Basics: number calculations
print("4 + 5 = " + str(4+5))
print("4 - 5 = " + str(4-5))
print("4 * 5 = " + str(4*5))
print("4 / 5 = " + str(4/5))
print("4 % 5 = " + str(4%5))
print("4 ** 5 = " + str(4**5))

## Basics: loops

for x in range(1,10):
    print("X is " + str(x))

for item in list1:
    print(item)

i4 = "item4"
while i4 not in list1:
    print(i4 + " not in list1 yet")
    list1.append(i4)
    print(i4 + " now in list1")
print(list1)

## Basics: input

question = "What's your name? "
answer = input(question)
print("Name = " + answer)

## Basics: functions

def addTwo(param1):
    return param1 + 2
# end addTwo

print(addTwo(46))

## Basics: objects
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

## Basics: modules
import os

filename = "text.txt"   # note that this is relative to where you're running the command, not where the .py file is

os.system("pwd")
os.system("echo \"" + string1 + "\" > " + filename)

## Basics: files

#read
with open(filename, "r") as f:
    for line in f:
        print("from " + filename + ": " + line)
print("changing file...")

#write
with open(filename, "w") as f:
    f.write("Hello from python!")
#read (again)
with open(filename, "r") as f:
    for line in f:
        print("from " + filename + ": " + line)

print("changing file...")
#write (append)
with open(filename, "a") as f:
    f.write("\n")
    f.write("Hello from python again!")
#read (again)
with open(filename, "r") as f:
    for line in f:
        print("from " + filename + ": " + line)
os.remove(filename)