# 3 - input

User input via stdin (terminal)

## Agenda
- Learn how to use input() method in python

## Learn how to use input() methon in python
You can use the `input()` funtion in python to get user's input. You can use this input to keep as a variable, or to answer questions, etc.

Example below. (inputsample.py)
```python
question = "What's your name? "
answer = input(question)
print("Hi,  " + answer)


inp = ""
while inp != "q":
    print("input q to quit.")
    inp = input("Your input: ")
print("You pressed 'q'")

```