import time
#for loop = a statement that will execute its block open
#           a limited amount of times
#
#           while loop = unlimited
#           for loop = limited

for i in range(10):
  print(i + 1)


for i in range(50,100): #start with 50 and take 50 value
  print(i)


for i in range(50,100+1):
  print(i)


for i in range(50,100,2):
  print(i)

for i in "Bro Code":
  print(i)


for seconds in range(10,0,-1):
  print(seconds)
  time.sleep(1)
print("happy new year!")