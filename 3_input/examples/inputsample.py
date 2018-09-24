# inputsample.py
 
question = "What's your name? "
answer = input(question)
print("Hi,  " + answer)


inp = ""
while inp != "q":
    print("input q to quit.")
    inp = input("Your input: ")
print("You pressed 'q'")
