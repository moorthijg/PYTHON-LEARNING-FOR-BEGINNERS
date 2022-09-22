name = "PYTHON PROGRAMMING"
print(name)
# output is "PYTHON PROGRAMMING"

name = "PYTHON PROGRAMMING"
print(name[1])
# output is "Y"

# REVERSING THE STRING
print(name[::-1])
# output is "GNIMMARGORP NOHTYP"

# DELETING ENTIRE STRING
del  name
print(name)


# FORMATTING IN THE STRING

person = {'name' : 'moorthi', 'age' : 26}
intro = 'my name is {0} and i am {1} years old'
a = 'murali'
b = 26
sentence = 'my name is {0} and i am {1} old'

#
print(sentence.format(a,b))
for i in range(1,100):
    a = 'the vallue is {:03}'
    print(a.format(i))

#
a = 22
b = 7
print(a / b)

#
pi = 3.142857142857143
b = 'value of pi is equal to {:.2f}'.format(pi)
print(b)

#
import datetime
date = 2022,9,5,15,44,56
b = datetime.datetime(2022,9,5,15,44,56)
print(b)