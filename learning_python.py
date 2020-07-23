https://www.learnpython.org/

#CONTENTS:





#/////GUIDE/////




#/////FUNCTIONS/////
>print() = print content to console
>.append() = adds value to a list
>len() = finds the length of a string, array, list, tuple, dictionary, etc.
>.count() = returns the number of elements with the specified value.



#/////DATA TYPES/////
>Numbers (int, float)
>Strings (str)



#/////FORMAT SPECIFIERS/////
When printing a variable to the console, use a format specifier denoted by a %_ followed by the variable name. 
e.g.
print("The second name on the names list is %s" % second_name)

%d : integer values 
%f : floating values 
%s : string values



#/////HELLO WORLD/////
-note, Python uses indentation for blocks instead of curly braces. 
-The standard indentation is four spaces.
e.g.
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

#Hello World:
print("Hello, World!")



#/////Variables and Types/////
note - You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

Python supports two types of numbers - integers and floating point numbers.
#define an int:
e.g.
myint = 7
print(myint)

#define a float:
e.g.
myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

#Strings:
Strings are defined either with a single quote or double quotes.
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

note - The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the 
string if using single quotes)

*Assignments can be done on more than one variable "simultaneously" on the same line.
e.g. 
a, b = 3, 4
print(a,b)

#operators executed on strings and numbers:
Simple operators like +, -, *, / can be executed on numbers and strings.
e.g.
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

NOTE: mixing operators between numbers and strings is not supported:
# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)

#Data type example:
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


#/////Lists/////
Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also
be iterated over in a very simple manner.

#define a list:
e.g.
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out every value in myList so: 1,2,3
for x in mylist:
    print(x)


#list example code block:
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append('hello')
strings.append('world')


second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)



#/////BASIC OPERATORS/////
Arithmetic Operators:
+
-
/
*

e.g.
number = 1 + 2 * 3 / 4.0
print(number)

#power relationships:
Using two multiplication symbols (**) creates a power relationship.
e.g.
#essentially, number after ** will be how many times you multiply first number with itself. So, for below, 7*7, 2*2*2, etc.
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#modulo operator:
Returns the integer remainder of the division.
e.g.
remainder = 11 % 3
print(remainder)

#Using operators with strings:
Python supports concatenating strings using the addition operator.
e.g.
helloworld = "hello" + " " + "world"
print(helloworld)

note - Python also supports multiplying strings to form a string with a repeating sequence.
e.g.
#prints hello ten times:
lotsofhellos = "hello" * 10
print(lotsofhellos)

#Using Operators with Lists:
Lists can be joined by using the addition operators.
e.g.
#will print [2, 4, 6, 8, 1, 3, 5, 7]
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

note - you can also form new lists with a repeating sequence using the multiplication operator. This does not create new separate lists but 
extends the list.
e.g.
#prints [1, 2, 3, 1, 2, 3, 1, 2, 3] 
print([1,2,3] * 3)

#list and operators example:
x = object()
y = object()

x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")













