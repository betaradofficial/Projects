'''
Program Filename: simpleGPA.py
Author: Zackary Wilson
Date: 11-20-25
Description: Calculates the user's Grade Point Average 
Input: Grade Points, Credit Hours
Output: Grade Point Average
'''

# Function definitions   
'''
function name: gpaCalc
description: Calculates grade point average given the total grade points and total credits
Parameters: totalPoints, totalCredits
Pre-Conditions: param totalPoints has Type: float, param totalCredits has Type: int
Post-Conditions: Output has Type: float
'''
def gpaCalc(totalPoints: float, totalCredits: int) -> float:
    return round((totalPoints / totalCredits), 3)


def main():

    class color:
        red = "\033[31m"
        green = "\033[32m"
        cyan = "\033[36m"
        yellow = "\033[33m"
        underline = "\033[4m"
        end = "\033[0m"


    gradeList = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
    valueList = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]

    pointList = []
    creditList = []
    totalPoints = []
    grade = credits = 0
    classCount = 1

  
    while True:
            
        # Assign variable grade to user input
        grade = input("Input your " + color.underline + "letter grade" + color.end + " for " + color.cyan + f"class {classCount}" + color.end + ", or input " + color.green + "\"done\" " + color.end + "if you are finished: ").upper()
        if grade == "DONE":
            print("")
            break

        # Append point value of the corresponding letter grade to pointList
        elif grade in gradeList:
            pointList.append(valueList[gradeList.index(grade)])
            classCount += 1

        else:
            print(color.red + "\nInput must be a valid grade or the word " + color.green + "\"done\"" + color.red + ".\nPlease try again.\n" + color.end)

    for i in range(len(pointList)):

        # Assign variable credits to user input, re-prompt the user if there is invalid input
        while True:
            credits = input("Input credit hours for " + color.cyan + f"class {i + 1}" + color.end + " as a " + color.underline + "positive integer" + color.end + ": ")
            try:
                credits = int(credits)
            except ValueError:
                print(color.red + "\nInput must be a " + color.underline + "positive integer" + color.end + color.red + ". \nPlease try again.\n" + color.end)
            else:
                if credits < 0:
                    print(color.red + "\nInput must be a " + color.underline + "positive integer" + color.end + color.red + ". \nPlease try again.\n" + color.end)
                else:
                    creditList.append(credits)
                    break

        if i == len(pointList) - 1:
            print("")

    
    if sum(creditList) == 0:
        print(color.red + "Cannot divide by 0.\nPlease restart the program.\n" + color.end) 
    else:  
        totalPoints = sum([pointList[j] * creditList[j] for j in range(len(pointList))])
        gpa = gpaCalc(totalPoints, sum(creditList))
        print("Your gpa is " + color.yellow + f"{gpa}\n" + color.end)
    input("Press enter to exit...")

main()