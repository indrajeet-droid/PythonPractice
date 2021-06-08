#logical operator (and, or, not) = used to check if two or more conditional statements are true
#not operator flip the condition--> if true than flip the value to false

temp = int(input("what is temperature outside? : "))

if temp >= 0 and temp <=30:
  print("the temperature is good today!")
  print("go outside!")
elif temp < 0 or temp > 30:
  print("the temperature is bad today!")
  print("stay inside!")



if not(temp >= 0 and temp <=30):
  print("the temperature is good today!")
  print("go outside!")

  

