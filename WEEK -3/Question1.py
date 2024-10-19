'''
Grade Calculator:
Prompt for marks in 5 subjects.
Calculate the average mark.
Determine and display the grade based on the average.
'''
marks1 = int(input("ENter the marks for 1st subject : "))
marks2 = int(input("ENter the marks for 2nd subject : "))
marks3 = int(input("ENter the marks for 3rd subject : "))
marks4 = int(input("ENter the marks for 4th subject : "))
marks5 = int(input("ENter the marks for 5th subject : "))

average = ((marks1+marks2+marks3+marks4+marks4+marks5)/5)

if average >= 75:
  print("You are pass, You got 'A' Grade")
elif average >= 65:
  print("You are pass, You got 'B' Grade")
elif average >= 50:
  print("You are pass, You got 'C' Grade")
elif average >= 35:
  print("You are pass, You got 'S' Grade")
else :
  print("YOu are fail")
  
