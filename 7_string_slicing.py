#slicing = create a substring by extracting elements from another string 
#               indexing[] or slice()
#               [start:stop:step]
# start -> from where to start ---->empty means start from 0 [:8]---> start from zero and take 8 characters
# stop -> how many characters  --->empty means end of string ---[2:] --> start from 2 and take all
#step -> is optional --> how much increasing  index between starting and stoping...default value is one

name = "Bro Code"

first_name = name[0]
first_name = name[4]
print(first_name)

first_name = name[0:3] #start with 0 index and take 3 characters
print(first_name)
first_name = name[:3] # means starting from 0 -> python assume start value is 0
print(first_name)

last_name = name[4:8]
print(last_name)

last_name = name[4:] #every characters starting from index 4 
print(last_name)

funky_name = name[::3]
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)



#part -2  slicing

website1 = "http://google.com"
website2 = "http://facebook.com"

#[start:stop:step] in parameter pass same but seprated with comma
#0...n positive index which start from left
#-1...n negative index which start from right

slice = slice(7,-4) #slice object

print(website1[slice])
print(website2[slice])


