# **kwargs = parameter that will pack all arguments into a dictionary
#         = useful so that a function can accept a varying amount of keyword arguments


def hello(first,last):
  print("hello "+ first +" "+ last)

#hello(first = "bro", last = "code", middle= "dude") ----> this line will not work


def hello_1(**kwargs): # kwargs is not important, what is important **
  print("hello "+ kwargs["first"] +" "+ kwargs["last"])
  print("hello ", end="")
  for key,value in kwargs.items():
    print(value+" ",end="")

hello_1(title = "Mr." ,first = "bro", last = "code", middle= "dude")


