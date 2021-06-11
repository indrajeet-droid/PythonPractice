# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a varible can be created

name = "Bro" #global scope (availabe inside & outside fuctions)

def display_name():
  name = "code" # local scope (available only inside this function)
  print(name)

#print(name) - no access as this is local 
display_name()
print(name)

