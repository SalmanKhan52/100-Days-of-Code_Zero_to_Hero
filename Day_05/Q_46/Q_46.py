# 46.  Write a Python program to convert days into  months,weeks & days.

days=int(input("Enter number of days: "))
months=days//30
week=(days%30)//7
remaining_days=days%7
print("Months:",months)
print("Weeks: ",week)
print("Days: ",remaining_days)
