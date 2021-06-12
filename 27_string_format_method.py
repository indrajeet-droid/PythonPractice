#str.format() = optional method that gives user 
#              more control when displaying output


animal = "cow"
item = "moon"

print("the "+animal+" jumped over the "+item)
print("the {} jumped over the {}".format(animal,item))
print("the {0} jumped over the {1}".format(animal,item))#positional argument
print("the {animal} jumped over the {item}".format(animal=animal,item=item))#keyword argument


text = "the {} jumed over the {}"
print(text.format(animal,item))

print("======================")

name = "Bro"
print("Hello my name is {}".format(name))
print("Hello my name is {:10}. Nice to meet you".format(name))#can add some pedding
print("Hello my name is {:<10}. Nice to meet you".format(name))
print("Hello my name is {:>10}. Nice to meet you".format(name))
print("Hello my name is {:^10}. Nice to meet you".format(name))

print("==========================")

#positional and keyword arguments

print("Hello {name:10}".format(name="Indrajeet"))
print("Hello {0:10}".format("Indrajeet"))


print("=============")

number = 1000

print("the number pi is {:.2f}".format(number))#last two degit or 3 digit as per input
print("the number pi is {:,}".format(number))#give comma
print("the number pi is {:b}".format(number))#binary number
print("the number pi is {:o}".format(number))#octal number
print("the number pi is {:x}".format(number))#hexa decimal 
print("the number pi is {:X}".format(number))#hexa decimal upper
print("the number pi is {:E}".format(number))#scientific notation



