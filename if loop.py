name=input("ENTER NAME: ")#we are getting the name and the age of the candidate
age=int(input("ENTER AGE: "))
if age>=18:#here we are giving a condition to check if the candidate is eligible to vote or not
    print(name, "ELIGIBLE TO VOTE AGE IS :", age)
else:
    print(name, " NOT ELIGIBLE TO VOTE AGE IS :", age)
