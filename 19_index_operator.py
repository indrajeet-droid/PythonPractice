#index operator [] = gives access to a sequence's element(str, list, tuple)

name = "bro code"

if(name[0].islower()):
  name = name.capitalize()

print(name)

first_name = name[0:3].upper()
first_name = name[0:3].upper()# both are same

last_name = name[4:]
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)
