try:
  number = int(input("Enter the number :"))
  print("Entered value is ", number)
except Exception as e:
  print("The error is ", e)
  print("made changes")
  
finally:
  print("I will be executed for ever")