# *args = parameter that will pack all arguments into a tuple   
#         useful so that a function can accept a varying amount of arguments 


def add(num1,num2):
  sum = num1 + num2
  return sum


#print(add(1,2,3)) --> give error sending 3 parameter

def add_1(*args): #args you can give any name
  sum = 0
  #args[0] = 0 --> will give error as 'tuple' object does not support item assignment -->immutable 
  #args = list(args) #covert and you can change as list are mutable
  #args[0] = 0
  for i in args:
    sum += i
  return sum


print(add_1(1,2,3,4,5,6))

