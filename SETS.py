# Set is an unordered collection of data types that is iterable,
#  mutable and has no duplicate elements

#Note: A set cannot have mutable elements like a list or dictionary, as it is mutable.
# A set contains only unique elements but at the time of set creation  

set1 = set()
print(set1)

set1 = set("programming")
print(set1)
# OUTPUT = {'g', 'p', 'i', 'm', 'o', 'n', 'r', 'a'} as you can see it only shows 
# the letters only one time, eventhough R and M are came twice.

set1 = set(["good", "morning","good"])
print(set1)
# output = {'morning', 'good'}

set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print(set1)
# output = {1, 2, 3, 4, 5, 6} as you can see set eliminated duplicate values

# Adding Elements to a Set
set1.add(8)
set1.add(9)
set1.add((6, 7))
print(set1)
# output = {1, 2, 3, 4, 5, 6, 8, 9, (6, 7)}

# using update method
set1 = set([1, 2, 3, 4, 5, 6, 8, 9, (6, 7)])
set1.update([18,99])
print(set1)
# output = {1, 2, 3, 4, 5, 6, 99, 8, 9, (6, 7), 18}

#                             Accessing a Set
st = set(["murali",97,65,87,"sun"])
print(st)
# output = {65, 97, 'murali', 87, 'sun'}

#  Removing elements from the Set
st = set(["murali",97,65,87,"sun"])
st.remove(97)
print(st)
# output = {65, 'sun', 'murali', 87} 
# as you can see the value 97 has been eliminated


# using pop() function
st.pop()
print(st)
# output = {'sun', 'murali', 87} here 65 is gone
 # wheter you have seen that even if you didnt mentions or 
# the list is empty it automatically removes the first element
st.pop()
print(st)
# output = {87, 'sun'}

# to remove all the elemnts from the set clear() method has been used
st.clear()
print(st)
# output = set() after removng all the elments in set it returns empty set.

#                            TYPECASTING

# converting list to set

list = [1,2,3,4,5,6]
set1 = set(list)
print(set1)
# output = {1, 2, 3, 4, 5, 6}

# converting str to set
str = "programming"
set2 = set("programming")
print(set2)
# output = {'n', 'o', 'r', 'a', 'i', 'p', 'm', 'g'}

# converting dict to set
dict = {1:"good", 2:"better", 3:"best"}
set3 = set(dict)
print(set3)
#output = {1, 2, 3}