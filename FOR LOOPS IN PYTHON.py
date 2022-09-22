"""syntax for loop in python"""

# for var in iterable
# statements

# example of simple for loop

a = "python programming"
for i in a:
    print(i) 

# OUTPUT  = p y t h o n p r o g r a m m i n g

# FOR LOOP CONTINUE STATEMNT
# printing all letters except 'o' and 'g'
for letter in 'python programming':
    if letter == 'o' or letter == 'g':
        continue
    print("current letter:", letter) 
# as you can see for loop continues the iteration while seeiing the word o or g as soon as possible
# and it leaves the words "o" and "g" and continues the iiteration

# Python For Loop with Break Statement
for i in 'python programming':
    if i == 't' or i == 'y':
        break
    print("current letter:", i)

# output = current letter: p
# as you can see for loop breaks the iteration while seeiing the word y as soon as possible

# Python For Loop with Pass Statement

a = "python programming"
for i in a:
    pass
print(i)
# output = g
# since the pass statemment shows only last word of the string