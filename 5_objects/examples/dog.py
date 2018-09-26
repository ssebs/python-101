# dog.py

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