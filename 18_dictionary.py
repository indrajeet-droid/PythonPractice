#dictionary = a changeble, unordered collection of unique key:value pairs
#             fast because they use hashing, allow us to access a value quickly


capitals = {
                "india":"New Delhi",
                "usa":"washington DC",
                "China":"Beijing",
                "Russia":"Moscow"

            }

print(capitals["india"]);    

#print(capitals["Germany"]) #not safe
print(capitals.get("Germany"))#return None safe method
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({"Germany":"Berlin"})
capitals.update({"usa":"Las Vegas"})
capitals.pop("China")
capitals.clear()




for key,value in capitals.items():
  print(key,value)


