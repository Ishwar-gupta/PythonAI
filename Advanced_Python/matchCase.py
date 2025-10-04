"""***************   Match Statement *******************************
This statement is similar to the switch statement found in other language
The basic syntax of the match statement involves matching a varaible against several cases
using the case keyword.

"""
def weeks(days:int)->int:
    match days:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Invalid !!! Please enter day's number between 1 to 7"
day=int(input("Enter number for finding corresponding days:"))
print(f"The corresponding days is {weeks(day)}")