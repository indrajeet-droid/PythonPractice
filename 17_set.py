#set = collection which is unordered, unindexed, no duplicate value

utensils = {"fork","spoon","knife","knife"} # no error but only on knife will be there 
print(utensils)

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()

dishes = {"bowl","plate","cup"}

dinner_table = utensils.union(dishes)
print(dinner_table)

utensils.update(dishes)
for x in utensils:
  print(x)

print(utensils.difference(dishes))

print(utensils.intersection(dishes))

