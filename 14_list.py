#list = used to store multiple items in single varible

food = ["pizza","hamburger","hotdog","spaghetti"]

print(food)
print(food[0])

#update value

food[0] = "pani puri"
food.append("ice cream")
food.remove("hotdog")
food.pop()#it will remove value ....no para than it will remove last value
food.insert(0,"cake")
food.sort()
food.clear()


for x in food:
  print(x)


