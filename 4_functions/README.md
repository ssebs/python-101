# 4 - functions

Functions are ways to create repeatable code. They are also useful to add *function* to your code.

## Agenda
- Learn what a function is
- Learn how to create and use it

## Learn what a function is
Functions are used to utilize code in more than one place in a program. The only way without functions to reuse code consists in copying the code. A function in Python is defined by a `def` statement.

## Learn how to create and use it

#### Creating a Function
In Python a function is defined using the `def` keyword:

Example
```python
def my_function():
  print("Hello from a function")
```
#### Calling a Function
To call a function, use the function name followed by parenthesis:

Example
```python
my_function()   # prints... "Hello from a function"
```

You can make these functions more useful by having them return values, using the `return` keyword. Parameters are variables that are passed to the funtion to be used within it. See example below.

```python
def add_two(test_num):
    return test_num + 2

print("Add two: " + str(add_two(2))) # prints... 4
```

A more complex example shown below:
```python
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
```