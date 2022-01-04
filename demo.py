Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=red
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=red
NameError: name 'red' is not defined
let
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    let
NameError: name 'let' is not defined. Did you mean: 'len'?
int a,b
SyntaxError: invalid syntax
inta
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    inta
NameError: name 'inta' is not defined. Did you mean: 'int'?
int a
SyntaxError: invalid syntax
a
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a
NameError: name 'a' is not defined
print
<built-in function print>
a
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a
NameError: name 'a' is not defined
a = "red"
b='blue'
print('a+b')
a+b
print("so",a+b)
so redblue
