#useful methods in string

name = "indrajeet"

print(len(name))
print(name.find("B"))#return index of B
print(name.capitalize())
print(name.lower())
print(name.isdigit())#return false as name is not digit
print(name.isalpha())# return false as it contain space. it will check only alphabet letters
print(name.count("o"))#return how many o are there
print(name.replace("o","a"))
print(name * 3)
