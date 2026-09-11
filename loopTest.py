#Match case statement in python

Day=input("Enter a day : ")
# fullweek=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

match Day:
    case "Monday":
        print("Workday 1")
    case "Tuesday":
        print("Workday 2")
    case "Wednesday":
        print("Workday 3")
    case "Thursday":
        print("Workday 4")
    case "Friday":
        print("Workday 5")
    case "Saturday":
        print("Weekend 1")
    case "Sunday":
        print("Weekend 2")

result=int(input("Enter your total marks: "))


match result:
    case _ if result > 100:
        print("Invalid marks")
    case _ if result >= 90:
        print("Golden A+")
    case _ if result >= 80:
        print("A+")
    case _ if result >= 70:
        print("A")
    case _ if result >= 60:
        print("A-")
    case _ if result >= 50:
        print("B")
    case _ if result >= 40:
        print("B-")
    case _ if result >= 30:
        print("C")
    case _ if result < 0:
        print("Invalid marks")
    case _:
        print("Fail")