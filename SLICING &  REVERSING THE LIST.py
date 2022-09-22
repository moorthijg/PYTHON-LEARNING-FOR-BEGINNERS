my_list1 = ['apple', 'banana', 'orange', 'mango', 'cherry', 'watermelon']
my_list2 = [0,1,2,3,4,5,6,7,8,9]
# syntax foor python list
#listname[x:y:z]
# x = starting of the list
# y = ending of the list
# z = particular value from the list
# printing all the values in the list
print(my_list1[0:])
# output = ['apple', 'banana', 'orange', 'mango', 'cherry', 'watermelon']
print(my_list2[0:])
# output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# printing to the particular  values in the list
print(my_list1[0:5])
# output = ['apple', 'banana', 'orange', 'mango', 'cherry'] since you get till the cherry only.
# this is called list slicing
# printing the particular value's places in string
print(my_list2[0::2])
# output = [0, 2, 4, 6, 8]
# there you have seen a particular list values
print(my_list2[0::3])
# output = [0, 3, 6, 9]
#REVERSING THE LIST
my_list1 = ['apple', 'banana', 'orange', 'mango', 'cherry', 'watermelon']
my_list2 = [0,1,2,3,4,5,6,7,8,9]
#  if you want to reverse the list you need  to give the negative indexing
print(my_list1[-1::-1])
# output = ['watermelon', 'cherry', 'mango', 'orange', 'banana', 'apple']
# since you have reversed the list
print(my_list2[-1:0:-1])
# output = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# getting particular chars in list
print(my_list2[0:9:-2])
# if you give negative sign to the role value it obiviously only reverse the string
print(my_list2[-1:-9:-2])
# output = [9, 7, 5, 3]










