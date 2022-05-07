Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help()

Welcome to Python 3.5's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.5/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> FUNCTIONS
Functions
*********

Function objects are created by function definitions.  The only
operation on a function object is to call it: "func(argument-list)".

There are really two flavors of function objects: built-in functions
and user-defined functions.  Both support the same operation (to call
the function), but the implementation is different, hence the
different object types.

See *Function definitions* for more information.

Related help topics: def, TYPES

help> print
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

help> 
=============================== RESTART: Shell ===============================
>>> x=15.56
>>> int(x)
15
>>> num=15
>>> float(num)
15.0
>>> n=10
>>> complex(x)
(15.56+0j)
>>> a=10
>>> b=-5
>>> complex(a,b)
(10-5j)
>>> 
=============================== RESTART: Shell ===============================
>>> s1='this is first indian book"
SyntaxError: EOL while scanning string literal
>>> 
=============================== RESTART: Shell ===============================
>>> s1='this is the first indian book'
>>> s2="core python"
>>> s1='''this first indian book on core python exploring all important and useful features'''
>>> s2="""this first indian book on core python exploring all important and useful features"""
>>> 
=============================== RESTART: Shell ===============================
>>> a=15
>>> print(type(a))
<class 'int'>
>>> 
=============================== RESTART: Shell ===============================
>>> 13+5
18
>>> 13-5
8
>>> 13*5
65
>>> 13/5
2.6
>>> 13%5
3
>>> 13**5
371293
>>> 13//5
2
>>> d=(1+2)*3**2//2+3
>>> print(d)
16
>>> 
=============================== RESTART: Shell ===============================
>>> a=b=1
>>> print(a,b)
1 1
>>> a=1;b=2
>>> print(a,b)
1 2
>>> a,b=1,2
>>> print(a,b)
1 2
>>> 
=============================== RESTART: Shell ===============================
>>> a=1;b=2
>>> if (a>b):
	print("yes")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
=============================== RESTART: Shell ===============================
>>> a=1;b=2
>>> if (a>b):
	print("yes")
	else:
		
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> x=15
>>> 10<x<20
True
>>> 10>x<20
False
>>> 10<=x>20
False
>>> 
=============================== RESTART: Shell ===============================
>>> x=100
\
>>> 
=============================== RESTART: Shell ===============================
>>> x=100
>>> y=150
>>> print(x and y)
150
>>> print(x or y)
100
>>> print(not x)
False
>>> 
=============================== RESTART: Shell ===============================
>>> a=true
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a=true
NameError: name 'true' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> a=True
>>> b=False
>>> a and a
True
>>> a and b
False
>>> a or a
True
>>> a or b
True
>>> b or b
False
>>> not a
False
>>> not b
True
>>> 
=============================== RESTART: Shell ===============================
>>> if x=10,find the ~x value
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> if x=10
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> 
names=["Rani","Yamini","Sushmitha","Veena"]
>>> for name in names:
	print(name)

	
Rani

Yamini

Sushmitha
Veena
>>> 
=============================== RESTART: Shell ===============================
>>> a=25
>>> b=25
>>> if (a is b):
	print("a and b have same identity")

	
a and b have same identity
>>> else:
	
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> one=[1,2,3,4]
>>> two=[1,2,3,4]
>>> if ("one and two are same")
SyntaxError: invalid syntax
>>> if (one is two)
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> one=[1,2,3,4]
>>> two=[1,2,3,4]
>>> if (one is two):
	print("one and two are same")

	
>>> 
===================== RESTART: Y:\practice program 1.py =====================
10 is even number
>>> 
===================== RESTART: Y:/practice program 2.py =====================
enter a digit:5
five
>>> 
===================== RESTART: Y:/practice program 3.py =====================
1
2
3
4
5
6
7
8
9
10
>>> 
===================== RESTART: Y:/practice program 4.py =====================
100
102
104
106
108
110
112
114
116
118
120
122
124
126
128
130
132
134
136
138
140
142
144
146
148
150
152
154
156
158
160
162
164
166
168
170
172
174
176
178
180
182
184
186
188
190
192
194
196
198
200
>>> 
===================== RESTART: Y:/practice program 5.py =====================
h
e
l
l
o
>>> 
===================== RESTART: Y:/practice program 6.py =====================
1
3
5
7
9
>>> 
===================== RESTART: Y:/practice program 7.py =====================
10
9
8
7
6
5
4
3
2
1
>>> 
