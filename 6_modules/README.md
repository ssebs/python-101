# 6 - modules

A module in python is a library that adds prebuilt functionality. It can also be a neighbor python file.

## Agenda
- How modules are useful
- Some popular modules & how to use them
    - pip
- Custom modules
    - Neighbor files
    - Module dir


## How modules are useful
Python modules are useful in that they save you time and effor. For example, the csv module lets you work with csv files pretty easily, handling different seperators and delimiters. 

Contrast this to creating your own csv parser (which may seem easy at the time), the csv parser will be missing features unless you spend lots of time debugging and testing.

## Some popular modules & how to use them
- os
    - examples below:
    ```python
    import os
    os.system("pwd") # run pwd command
    os.chmod("./tmp", 644) # chmod tmp file to R/W R R
    ``` 
- sys
    - examples below:
    ```python
    import sys
    print(sys.argv) # handles cli arguments
    print(sys.argv[0]) # python filename
    print(sys.argv[1]) # first argument after filename(if exists)
    print(len(sys.argv)) # amount of arguments given. $ python foo.py <- is 1 arg total
    ``` 
- shutil
    - examples below:
    ```python
    import shutil
    shutil.copytree("./folder","./folder")   # cp -R ./folder ./folder2
    ``` 
- csv
    - examples below:
    ```python
    import csv

    # writer
    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    # reader
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
    ## OUTPUT ##
    # Spam, Spam, Spam, Spam, Spam, Baked Beans
    # Spam, Lovely Spam, Wonderful Spam
    ``` 
- etc

### pip
There are only so many prepackaged modules in python. If you find something you want to use and it's not built it, you'll likely need to install it. `pip` is a package manager for python. You can `pip install` the module that you're looking for. 

> Note: If you have to use python3.6 [FILE], then you'll have to use pip3.6 instead of regular pip

For example:
```shell
$ pip install markdown
```
```python
import markdown
sample_md = '''# Sample!
This will be converted into html using the *markdown* module

> I'm a quote!
'''
print(markdown.markdown(sample_md))
### SAMPLE OUTPUT ###
## ssafari@meshinprod12 ~/python-101 $ python3.6 6_modules/examples/popular.py
## <h1>Sample!</h1>
## <p>This will be converted into html using the <em>markdown</em> module</p>
## <blockquote>
## <p>I'm a quote!</p>
## </blockquote>
```

## Custom modules
Let's say you want to create your own library, or have some code in a separate file, you can do that with custom modules. The prior would be having a full module, and the latter would be importing a neighboring file as a module.

> See custom/ dir for examles
### Neighbor files

### Module dir