# while.py

i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

inp = ""
while inp != "q":
    print("input q to quit.")
    inp = input("Your input: ")
