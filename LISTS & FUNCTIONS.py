from audioop import avg


a = [1,2,3,4,5,5,5,5]
print(a)

# output [1,2,3,4,5]

a = [1,2,3,4,5]
print(type(a))

# output <class 'list'>

a.append(1)
print(a)
# output [1, 2, 3, 4, 5, 1] 
# append is used to add the data in list

a.append("hello")
print(a)
# output [1, 2, 3, 4, 5, 1, 'hello']

a.append([9,8,7,6])
print(a)
# output [1, 2, 3, 4, 5, 1, 'hello', [9, 8, 7, 6]] 
# you can insert another list into list using append

a.pop()
print(a)
# output [1, 2, 3, 4, 5, 1, 'hello']
# pop function is used to delete the datas in the list
# when you didn't mention the data it automatically delete the last argument

a.pop()
print(a)
# output [1, 2, 3, 4, 5, 1]

a.pop(2)
print(a)
# output [1, 2, 4, 5, 1]
# there u see that the number 3 has been removed from the list
# when you define the place of the data in list pop function  
# will remove that data which is in place 
# of the list

# you can interchange the value of the datas in list by assiging values using 
a[2] = 5
print(a)
# output [1, 2, 9999, 5, 1]
# as you can see the value of the place a[2] has been changed from 4 to 9999.

# getting the sizeof list
print(len(a))
# output = 5

#reversing the list
# reverse()
a = [1,2,3,4,5,6,7,8]
a.reverse()
print(a)
# output = [8, 7, 6, 5, 4, 3, 2, 1]

#  Removing Elements from the List
#  remove() function
a.remove(6)
print(a)
# output [8, 7, 5, 4, 3, 2, 1]
# as you can see the value has been removed from the list


# another method to remove elements form list
a = [1,2,3,4,5,6,7,8]
for i in range (1,5):
    a.remove(i)
print(a)
# output  = [5, 6, 7, 8]

a = [1,2,3,4,5,6,7,8]
hum=sum(a)
print(hum)

# finding the average of the list
avg_of_a = sum(a)/len(a)
print(avg_of_a)
# output 4.5


#finding big number in list
A = max(a)
print(A)
# output is 8


