import os

path = "C:\\Users\\indra\\OneDrive\\Desktop\\excel_learner"

if os.path.exists(path):#check path is path exists
  print("That location exists")
  if os.path.isfile(path):#check is file or Folder
    print("that is a file")
  elif os.path.isdir(path):
    print("that is a folder")
else:
  print("that location doesn't exists!")


#os.path.isdir(path)
#  
  