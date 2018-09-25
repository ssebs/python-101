# popular.py

## common ##
# OS
import os
os.system("pwd") # run pwd command
os.chmod("./tmp", 644) # chmod tmp file to R/W R R

# SYS
import sys
print(sys.argv) # handles cli arguments
print(sys.argv[0]) # python filename
print(sys.argv[1]) # first argument after filename(if exists)
print(len(sys.argv)) # amount of arguments given. $ python foo.py <- is 1 arg total

# SHUTIL
import shutil
shutil.copytree("./folder","./folder")   # cp -R ./folder ./folder2

# CSV
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


## pip ##
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