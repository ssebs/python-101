# 1 - logic

Logic in programming is split up into two ideas: **Conditionals** **Boolean logic**

## Agenda
- Conditional Logic
- Boolean logic

## Conditional logic
This would be using things like if, else, else if to run different code based on a condition

An example of if below: (conditional-1.py)
```python
age = 17
print("You are " + str(age))

if age >= 21:       # Is the age equal to or over 21?
    print("You can do anything! Even drink!")
elif age >= 18:    # If not, is it equal to or over 18?
    print("You can drive and your an adult!")
elif age >= 16:    # If not, is it equal to or over 16?
    print("You can drive")
else:               # Otherwise, do this
    print("You can't do anything!")

```

The above example (*if*, *elif*, *else*) is stating that if this condition is not met, check the next one, then the next, and finally if nothing else checks out, do this.

You can also use just a bunch of *if*'s instead of using *elif* or *else*'s. See below example
(conditional-2.py)
```python
age = 17
print("You are " + str(age))

if age >= 21:       # Is the age equal to or over 21?
    print("You can drink!")
if age >= 18:       # Is the age equal to or over 18?
    print("You are an adult!")
if age >= 16:       # Is the age equal to or over 16?
    print("You can drive!")
if age < 16:       # Is the age under 16?
    print("You can't do anything!")

```

## Boolean logic
This would be using things like and, or, not to see if multiple things are true, or not true, etc based on multiple conditions

Example below(logic-1.py)
```python
name = "Sebastian"

if "Seb" in name and len(name) < 2:
    print("AND")
elif "bas" in name or name.endswith("%"):
    print("OR")
elif lower(name) not in "seb":
    print("NOT")
```

The above example should result in "OR", because "bas" is found within the *name* variable. It doesn't need to end with "%", since it's an or operator

