# 2 - loops

## Agenda
- For loops
    - In range
    - In list
- While loops

##  For loops
Loop over a set of numbers, or a list of items. In python, you can use the `in` keyword to specify what you want to loop over.

###  In range
You can loop over a "range" of nunbers. This would be equivelent to other languages' `for(int i = 0; i < 10; i++)`

Python syntax for this is `for i in range(0,10)`

Both would go over: 0,1,2,3,4,5,6,7,8,9 (starting at index 0)

for.py
```python
# i is typically used for iterating
for i in range(0,10):
    print(str(i))
```

###  In list
You can also loop over a python list. Say you have a list of fruits and you want to print them all out, and say that you love Apples but nothing else. 

```python
fruit = ["banana", "apple", "kiwi", "strawberry"]

for f in fruit:
    if "apple" in f:
        print("I like to eat " + f)
    else:
        print("I don't like " + f)

```


##  While loops

