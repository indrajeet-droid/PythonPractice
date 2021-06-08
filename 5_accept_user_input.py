#accept user input using input() function

input("what is your name : ")
name = input("what is your name : ")

print("Hello "+ name)#always accept series of characters i.e string 
print(name)

age = int(input("How old are you : ")) #if user type float value it will genrate error as loss of data
height = float(input("what is your height : "))
print("you are "+str(age)+" years old")
print("you are "+str(height)+" cm tall")