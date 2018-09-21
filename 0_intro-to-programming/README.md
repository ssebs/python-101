# 0 - intro to programming

## Agenda
- Learn concepts of programming
- Binary 101
- Learn data types
- Learn how to run python programs
- Create a "Hello, World!" application


## Learn concepts of programming

> You'll see some complicated code below, don't worry it's just for concept

What is a program? At it's simplest, a program is a set of instructions that a computer follows. 

How to we make a program? We write human readable code which gets translated/compiled/linked/converted to machine code. Machine code is the 1's and 0's that the CPU reads (You'll see an example soon). 

Let's say you want to "print" something out to the screen, (Print is in quotes because it doesn't go through a printer, it get's sent to your screen via **stdout**). (stdout? see https://en.wikipedia.org/wiki/Standard_streams) when you tell the program to print, the cpu is told to run the print command, using the data that you sent it. Sample: `print("Hi")`

All programming behind the scenes is math and numbers, all the words you type get turned into 1's and 0's. (See binary/hex 101 below) Luckily, we don't have to work in binary, or even in numbers! How are things  really math and numbers? See this example below... (First in python, then assembly, then "binary")

Python below (High level language)
```python
print("Hi")
```

Assembly below (Low level language)
```assembly
global _start
section .data
    message db "Hi\0", 3

.text
_start:
    mov rax, 1       ; system call for write
    mov rdi, 1       ; file handle 1 is stdout
    mov rsi, message ; address of string to output
    mov rdx, 13      ; number of bytes
    syscall          ; invoke operating system to do the write
    mov rax, 60      ; system call for exit
    xor rdi, rdi     ; exit code 0
    syscall          ; invoke operating system to exit

```

Machine code (basically, the compiler translates the assembly directly into machine code, which is in hexadecimal numbers. e.g. mov eax, 'H' = b8 48)
```
b8	21 0a 00 00			#moving "!\n" into eax
a3	0c 10 00 06			#moving eax into first memory location
b8 	6f 72 6c 64			#moving "orld" into eax
a3	08 10 00 06			#moving eax into next memory location
b8 	6f 2c 20 57			#moving "o, W" into eax
a3	04 10 00 06			#moving eax into next memory location
b8 	48 65 6c 6c			#moving "Hell" into eax
a3	00 10 00 06			#moving eax into next memory location

b9  	00 10 00 06			#moving pointer to start of memory location into ecx
ba  	10 00 00 00			#moving string size into edx
bb  	01 00 00 00			#moving "stdout" number to ebx
b8  	04 00 00 00			#moving "print out" syscall number to eax
cd  	80			        #calling the linux kernel to execute our print to stdout
            
b8	01 00 00 00			#moving "sys_exit" call number to eax
cd	80			        #executing it via linux sys_call
```

Okay that was confusing and hard to read... Good news! We don't touch any of that stuff in python, so we can do the more fun (and useful) stuff in the following chapters.

Variables are the most useful part of programming. Sure you can "hard code" some numbers and strings (string of characters. e.g. "foo", i.e. words/sentenses) together and have some output, but if you want to make a useful program you're going to have to use variables. 


## Binary/Hexadecimal 101
> You may be better off googling this
- We just saw the machine code above in *hexadecimal*
    - Which looked like a3 04 6c 
    - Another way to represend hexadecimal numbers is 0x4a
- First we have to understand how we typically use numbers. We count up to 9 normally, then once we get to 10, we put a '1' in the 10's slot, and start over. So 12 is really 10 + 2. This is called "base 10"
- What's hexadecimal?    
    - Hexadecimal is base 16, which means it goes to 16 before we add another digit. Since we only have 10 digits, we use 6 letters to represent numbers past 10.
    
    **Table below**
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
    |:-:|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | a  | b  | c  | d  | e  | f  |
- Okay but what does 0x5b mean? What is that in base 10?
    - The 0x part is just stating that it's hexadecimal (see the x?)
    - 5a is going to be 16*5 + b which is 11
        - Total is 80 + 11 = 91
    - It's not super important to know how to do this, just understand the concept
- What's binary? Just 1's and 0's?
    - Same thing as above, but with base 2 instead
    - Can also be represented as 0b0101
    - This is easiest shown by table, or by looking at a different tutorial
    - https://www.mathsisfun.com/binary-number-system.html
    - https://en.wikipedia.org/wiki/Binary_number#Counting_in_binary
 
    | **Binary**|**Base 10**|
    |:-----:|:-----:|
    |0|0|
    |1|1|
    |10|2|
    |11|3|
    |100|4|
    |101|5|
    |110|6|
    |111|7|
    |1000|8|
    |1001|9|
    |1010|10|
    |1011|11|

## Learn data types
There's lots of ways to represent binary, even using words! In this section we'll go over simple data types that you need to know.

We'll break this down into a few sections
- Numbers
    - int (integer)
        - Whole numbers
        - e.g. 1,2,-45,2335
    - float (floating point numbers)
        - 32 bit decimal numbers (can only be 7 digits)
        - e.g. 4.2,6.9,-23.73457,3.14
    - double (double precision floating point numbers)
        - 64 bit decimal numbers (can be 15 digits) 
        - e.g. 1.00000000000004
- Strings/Characters
    - char
        - Single character, can be ASCII / UTF-8 / UTF-16 / etc
        - e.g. 'a', '7', '%', '\u1F60E', '😎'
    - string
        - a "string" of characters
        - e.g. "hi", "hey what's up"
    - Escape chars
        - You need to know how to "escape" a character. Let's say you want to add a line break. You hit "Enter", but that doesn't get put on the screen! You have to "escape" it. 
        - List of common escape chars below
            - \n - newline (Enter)
                - If you're on Windows, you'll have to use \r\n
            - \t - tab
            - \' - apostrophe
            - \" - quote
            - \\\ - back slash
- True/False
    - bool (boolean true/false)
        - Can be set to true or false
        - Equivelent to 1 or 0
- Lists
    - Everything previously was a "primitive" datatype in python. This means it's all built in and you can just set a variable equal to that data type
        - e.g. foo = "foo", bar = "-3.14", test = 't', cool = '😎'
    - list
        - A list of these primitive values
        - These are useful for keeping track of multiple useful things
        - e.g. groceries = ["apples","milk","bread","turkey"] 
            - This is a list of strings

## Learn how to run python programs
There are lots of ways to run python programs

- Command line
    - Open up a terminal, go to where your python file is, and run this
    - `python3 myfile.py`
- IDE
    - VS Code
        - Good for small projects
        - Code editor, you can setup debugging tools
        - Lightweight
    - PyCharm
        - Good for larger projects
        - More robust IDE features (better intellisense, highlighting, etc)
    - IDLE
        - Another option...
- Batch / Command / Script files
    - Create a .bat or .sh file to run the python program
        - e.g. *run.bat*
        ```batch
            python3 myfile.py some arg >> logfile.txt
        ```
        - e.g. *run.sh*
        ```sh
            python3 myfile.py some arg >> logfile.txt
        ```
## Create a "Hello, World!" application

Open up your editor of choice, and copy this below and run it.

**Python code**
```python
print("Hello, World!")
```
**Shell commands to make and run this**
```shell
ssafari@meshinprod12 ~/Desktop $ echo 'print("Hello, world!")' > hello.py
ssafari@meshinprod12 ~/Desktop $ python3.6 hello.py                      
Hello, world!
ssafari@meshinprod12 ~/Desktop $ 
```

## Done! You can move on to chapter 1