"""
Name: Xiangyi Zhu
UCINetID: 85965253
"""

class NoStaircaseSizeException(Exception):
    pass

class IntegerOutOfRangeException(Exception):
    pass

''' This functions asks the user for the number of steps
they want to climb, gets the value provided by the user
and returns it to the calling function. This function will
raise any exceptions related to none integer user inputs.'''
def getUserInput():
    value = input("How many steps do you want to move?\n")
    if value == "DONE":
        return "DONE"
    try:
        return int(value)
    except ValueError:
        raise ValueError

''' This function takes the number of steps as an input parameter,
creates a string that contains the entire steps based on the user input
and returns the steps string to the calling function. This function will raise
any exceptions resulting from invalid integer values.
'''
def createSteps(stepCount):
    if stepCount == 0:
        raise NoStaircaseSizeException
    elif 0 < stepCount < 1000:
        steps = "  "*(stepCount-1)+"+-+\n" + "  "*(stepCount-1)+"| |\n"
        for i in range(stepCount-2,-1,-1):
            steps += "  "*i+"+-"*2+"+\n"
            steps += "  "*i+"| |\n"
        steps = steps+"+-+"
        return steps.rstrip("\n")
    else:
        raise IntegerOutOfRangeException


'''This function kicks off the running of your program. Once it starts
it will continuously run your program until the user explicitly chooses to
end the running of the program based on the requirements. This function returns
the string "Done Executing" when it ends. Additionally, all exceptions will be
handled (caught) within this function.'''
def runProgram():
    while True:
        try:
            user_input = getUserInput()
            if user_input == "DONE":
                return "Done Executing"
                break
            try:
                print(createSteps(user_input))
            except NoStaircaseSizeException:
                print("I cannot draw a staircase with no steps.")
            except IntegerOutOfRangeException:
                print("That staircase size is out of range.")
        except ValueError:
            print("Invalid staircase value entered.")


'''Within this condition statement you are to write the code that kicks off
your program. When testing your code the code below this
should be the only code not in a function and must be within the if
statement. I will explain this if statement later in the course.'''
if __name__ == "__main__": 
    runProgram()
