# range() function in Python
"""The range() function is used to generate a sequence of numbers"""

# start: integer starting from which the sequence of integers is to be returned
# stop: integer before which the sequence of integers is to be returned. 
# The range of integers end at stop – 1.
# step: integer value which determines the increment between each integer in 
#       the sequence 

for i in range(1,20):
    print(i,end=" ")

sum = 0
for i in range(0, 20):
    sum = sum + i
    print(sum, end = " ")

# output = 1 3 6 10 15 21 28 36 45 55 66 78 91 105 120 136 153 171 190

#  For loop in Python with else & range function
for i in range(1, 8):
    print(i, end = " ")
else:
    print("GOOD BYE", end = " ")

# OUTPUT = 1 2 3 4 5 6 7 GOOD BYE
# Here it sshows that for loop with else means that it will print the else statement for 
# the last range in for loop iteration.