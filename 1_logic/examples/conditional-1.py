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