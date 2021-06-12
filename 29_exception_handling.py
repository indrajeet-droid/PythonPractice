# exception = events detected during execution that interrupt the flow of a program

try:
  numerator = int(input("Enter a number to divide: "))
  denominator = int(input("Enter a number to divide by: "))
  result = numerator / denominator
  
except  ZeroDivisionError as e:#we can write without e as well

  #it's not consider good practice to have single except block that will handle all Exception. it is much batter to first handle specific Exception when the occured. we can do so by creating addional except block 
  print(e)
  print("You can't divide by zero! idiot")
  
except ValueError as e:#5/pizza give you error as value error
   print(e)
   print("Enter only number plz")

except Exception as e:
  print(e)
  print("something went worng :( ")
else:
 print(result)

finally:
  print("this will always execute")
  
  
