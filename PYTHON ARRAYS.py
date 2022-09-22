# what is array?
"""An array is a collection of items stored at contiguous memory locations"""

#                                  Creating a Array                              #



# output is The new array is :  1 2 3 4 5 6 7 8 9 11 

# Adding Elements to a Array
import array as arr
b = arr.array('i', [4,9,16,25])
print("the array is:", end=" ")
for i in range (0,2):
    print (b[i],  end=" ")
print()
b.insert(64,121) # insert function takes exactly two arrguments as a input output = the array is: 4 9 16 25 121 49
b.append(49)     # append function takes exactly one argument as a input output = the array is: 4 9 16 25 49 
print("the array is:", end=" ")
for i in (b):
    print(i,end=" ")
print()
