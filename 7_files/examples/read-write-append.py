# read write append .py

## read example 1 ##
print("Read example 1")
import os 
os.system("echo foo > bar.txt") # Create a sample text file to read in

with open("bar.txt","r") as f:
    for line in f:
        print("Line: " + line)

## read example two ##
print("Read example 2")
os.system("echo foo > bar.txt") # Create a sample text file to read in
os.system("echo I love python >> bar.txt") # Create a sample text file to read in

with open("bar.txt","r") as f:
    content = f.readlines()
    print(content)

os.system("rm bar.txt") # Delete the file we created

## write example ##
print("Write example")
grocery_list = ["eggs","apples","milk","steak"]

with open("groceries.txt",'w') as f:
    for item in grocery_list:
        f.write("Item: " + item + "\n")

print(os.system("cat groceries.txt")) # Print the contents of the file using the os.system syntax (not recommended)
os.system("rm groceries.txt") # Delete the file we created

## append example ##
print("Append example")
os.system("echo foo > bar.txt") # Create a sample text file
with open("bar.txt",'a') as f:
    f.write("I'm being appended!\n")

print(os.system("cat bar.txt")) # Print the contents of the file using the os.system syntax (not recommended)

with open("bar.txt",'a') as f:
    f.write("Again!")

print(os.system("cat bar.txt")) # Print the contents of the file using the os.system syntax (not recommended)
os.system("rm bar.txt") # Delete the file we created