# 7 - files

This chapter will go into how to read/write/append text files.

# Agenda
- How we work with files in general
- Reading Files
- Writing Files
- Appending Files


## How we work with files in general
In python, there are a couple ways we can work with files. The first is using the `open()` function, which we'll cover here. You can also use modules in conjunction with this to modify/create more complex files, like csv/yml/json/etc. A hack-ey way of creating files would be using the command syntax (`os.system("echo foo > bar.txt")`)

## Reading Files
Reading files isn't too hard in python. You use a `with open("filename.txt","r") as f` syntax, and read the lines as you go. The 'r' can instead be 'w', or 'a'. r=read, w=write, a=append

Example below... (See read-write-append.py)
```python
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
```

## Writing Files
Writing files is similar to reading files in python, but instead of printing the contents, we write what we want to the file. Note that this will erase the existing contents of the file. Change the 'r' to an 'w' to write files.

Exmaple below
```python
## write example ##
print("Write example")
grocery_list = ["eggs","apples","milk","steak"]

with open("groceries.txt",'w') as f:
    for item in grocery_list:
        f.write("Item: " + item + "\n")

print(os.system("cat groceries.txt")) # Print the contents of the file using the os.system syntax (not recommended)
os.system("rm groceries.txt") # Delete the file we created
```

## Appending Files
Appending files is extremely similar to writing files, but instead of erasing the contents of the file, you add what you want to the end of it. Change the 'w' to an 'a' to append files.

Example
```python
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
```