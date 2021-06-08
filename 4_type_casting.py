#type casting = convert the data type of a value to another data type 

x = 1 #int
y = 2.0 #float
z = "3" # string

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#convert y & z to int

print(x)
print(int(y))#this is not permanent change. if you want, you need to reassign as below
print(int(z))#this is not permanent change. if you want, you need to reassign as below

#permanent change
y = int(y)
z = int(z)

print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))


x= float(x)

print(x)

#why we need to convert 
# for example suppose you want to display x value is + str(x)----we can't display string and int together

print("x value is "+ str(x))