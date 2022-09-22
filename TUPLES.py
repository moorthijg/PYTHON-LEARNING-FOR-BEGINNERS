# tuples definition
# Tuple is a collection of Python objects much like a list.
# The sequence of values stored in a tuple can be of any type, and they are indexed by integers

# Creation of Python tuple without the use of parentheses () is known as Tuple Packing.  

tuple = ()
print(tuple)

tuple1 = ("java", "python","R")
print(tuple1)
# output = ('java', 'python', 'R')

print(type(tuple1))
# output  <class 'tuple'>

# Creating a Tuple with Mixed Datatypes.
a = (5,"murali","tree","sun",7.8)
print(a)
# output = (5, 'murali', 'tree', 'sun', 7.8)

# creating a tuple using with nested tuple
a1 = (1,2,3,4)
a2 = ("sun","moon","sea","tide")
a3 = (a1,a2)
print(a3)
# output = ((1, 2, 3, 4), ('sun', 'moon', 'sea', 'tide'))

# tuple repetition 
a4 = ("python",) * 6
print(a4)
# output = ('python', 'python', 'python', 'python', 'python', 'python')

# Creating a Tuple with the use of loop
b = 'basket'
n= 5

for i in range (int(n)):
    b = (b,)
    print(b)

# output ('Geeks',)
#        (('Geeks',),)
#        ((('Geeks',),),)
#        (((('Geeks',),),),)
#        ((((('Geeks',),),),),)

# accesing the tuple using indexing
a = ('programming')
print(a[3])
# output = g

# tuple unpacking
a = (5,"murali","tree","sun",7.8)
A,B,C,D,E = a
print(A)
print(B)
print(C)
print(D)
print(E)
#output =  5 murali tree sun 7.8

#Concatenation of Tuples
# IT MEANS THAT JOINING OF TWO TUPLES AND IT CAN BE DONE BY + OPERAATOR
# Only the same datatypes can be combined with concatenation, 
# an error arises if a list and a tuple are combined. 

a = ('5,murali,tree,sun,7.8' )
b = ('basket')
c = a + " " + b
print(c)
# output = 5,murali,tree,sun,7.8 basket

# slicing of tuples

a1 = ('programming')
print(a1[1:])
# output = rogramming

# getting specific part of tuple
print(a1[3:7])
# output = gram

# DELETING TUPLE
del a1
print(a1)


"""Similarities	Differences
Functions that can be used for both lists and tuples:

len(), max(), min(), sum(), any(), all(), sorted()

# Methods that cannot be used for tuples:

append(), insert(), remove(), pop(), clear(), sort(), reverse()

Methods that can be used for both lists and tuples:

count(), Index()

we generally use ‘tuples’ for heterogeneous (different) data types and 
‘lists’ for homogeneous (similar) data types.
Tuples can be stored in lists.	
Iterating through a ‘tuple’ is faster than in a ‘list’.
Lists can be stored in tuples.
‘Lists’ are mutable whereas ‘tuples’ are immutable.
Both ‘tuples’ and ‘lists’ can be nested.	
Tuples that contain immutable elements can be used as a key for a dictionary.
"""