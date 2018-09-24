# func.py

def my_function():
  print("Hello from a function")

my_function()

def add_two(test_num):
    return test_num + 2

print("Add two: " + str(add_two(2))) # prints... 4


# This should print the even numbers and return them
def get_even_nums(my_list):
    evens = []
    for x in my_list:
        if x % 2 == 0:
            print(str(x) + " is an even number")
            evens.append(x)
    if evens:
        return evens
    else:
        return None

my_nums = [3,5,46,74,3,2,4,56,576,4,56]

evens = get_even_nums(my_nums)  # This should save the even numbers and print them out

print(evens)
## OUTPUT BELOW
#
## Hello from a function
## Add two: 4
## 46 is an even number
## 74 is an even number
## 2 is an even number
## 4 is an even number
## 56 is an even number
## 576 is an even number
## 4 is an even number
## 56 is an even number
## [46, 74, 2, 4, 56, 576, 4, 56]
## 