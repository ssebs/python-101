# 6 - modules

A module in python is a library that adds prebuilt functionality. It can also be a neighbor python file.

## Agenda
- How modules are useful
- Some popular modules & how to use them
    - pip
- Custom modules 
    - Neighbor files
    - Module dir (packages)


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

You would want to create files with functions that you'd use, or if you want the whole file to run, use a package.

> See custom/ dir for examles
### Neighbor files
To use neighboring python files as modules, import them with the functions that you want to use. 

Examples: 

`neighbor.py`

```python
# neighbor.py

def test_neighbor():
    print("I'm a function in the neighbor.py file under neighbor!")
```

`use-neighbor.py`

```python
import neighbor

neighbor.test_neighbor()

## OUTPUT ##
# ssafari@meshinprod12 ~/python-101 $ python3.6 6_modules/examples/custom/use-neighbor.py
# I'm a function in the neighbor.py file under neighbor!
```

### Module dir (packages)
Please see https://docs.python.org/3/tutorial/modules.html#packages

> Below contents are pasted from the above, as the python docs explain it well.

Packages
Packages are a way of structuring Python's module namespace by using "dotted module names". For example, the module name A.B designates a submodule named B in a package named A. Just like the use of modules saves the authors of different modules from having to worry about each other's global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other's module names.

Suppose you want to design a collection of modules (a "package") for the uniform handling of sound files and sound data. There are many different sound file formats (usually recognized by their extension, for example: .wav, .aiff, .au), so you may need to create and maintain a growing collection of modules for the conversion between the various file formats. There are also many different operations you might want to perform on sound data (such as mixing, adding echo, applying an equalizer function, creating an artificial stereo effect), so in addition you will be writing a never-ending stream of modules to perform these operations. Here's a possible structure for your package (expressed in terms of a hierarchical filesystem):

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.

The __init__.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable, described later.

Users of the package can import individual modules from the package, for example:

`import sound.effects.echo`
This loads the submodule sound.effects.echo. It must be referenced with its full name.

`sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)`
An alternative way of importing the submodule is:

`from sound.effects import echo`
This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:

`echo.echofilter(input, output, delay=0.7, atten=4)`
Yet another variation is to import the desired function or variable directly:

`from sound.effects.echo import echofilter`
Again, this loads the submodule echo, but this makes its function echofilter() directly available:

`echofilter(input, output, delay=0.7, atten=4)`
Note that when using from package import item, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. The import statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an ImportError exception is raised.

Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package; the last item can be a module or a package but can't be a class or function or variable defined in the previous item.

