#######################################################################
# Program Filename: assignment3.py
# Author: Zackary Wilson
# Date: 02-04-2026
# Description: Calculates the sample average and whether average
# is between upper and lower bounds
# Input: 5 sample values, goal average, goal standard deviation
# Output: Average of sample values, upper and lower bounds of an
# expected range, and if the average is between upper and lower bounds
#######################################################################
import math


#######################################################################
# Function: bound_calc
# Description: Calculates lower and upper bounds of an expected range
# Parameters: goal_avg, goal_stdev
# Return values: lower_bound, upper_bound
# Pre-Conditions: inputs are floats
# Post-Conditions: returns floats
#######################################################################
def bound_calc(goal_avg: float, goal_stdev: float) -> float:

    lower_bound = goal_avg - (3 * goal_stdev) / math.sqrt(5)
    upper_bound = goal_avg + (3 * goal_stdev) / math.sqrt(5)

    return lower_bound, upper_bound


#######################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: Prints the sample average and whether that average
# is between upper and lower bounds
#######################################################################
def main():

    class Color:
        GREEN = "\033[92m"
        BLUE = "\033[94m"
        CYAN = "\033[96m"
        WARNING = "\033[93m"
        UNDERLINE = "\033[4m"
        END = "\033[0m"

    ERROR_MESSAGE = (
        f"\n{Color.WARNING}Please input a valid number "
        f"{Color.UNDERLINE}greater than 0{Color.END} \n"
    )
    i = 1
    sample_total = 0

    # sample total section
    while i <= 5:

        try:
            sample = float(
                input(
                    f"Enter {Color.GREEN}{Color.UNDERLINE}sample {i}"
                    f"{Color.END} as a {Color.UNDERLINE}number greater"
                    f" than 0{Color.END}: "
                )
            )
        except ValueError:
            print(ERROR_MESSAGE)
            continue

        if sample <= 0:
            print(ERROR_MESSAGE)
            continue
        else:
            sample_total += sample
            i += 1

    # goal average section
    while True:
        try:
            goal_avg = float(
                input(
                    f"Enter {Color.GREEN}{Color.UNDERLINE}goal average"
                    f"{Color.END} as a number {Color.UNDERLINE}greater"
                    f" than 0{Color.END}: "
                )
            )
        except ValueError:
            print(ERROR_MESSAGE)
            continue

        if goal_avg <= 0:
            print(ERROR_MESSAGE)
            continue
        else:
            break

    # goal standard deviation
    while True:
        try:
            goal_stdev = float(
                input(
                    f"Enter {Color.GREEN}{Color.UNDERLINE}goal standard "
                    f"deviation{Color.END} as a number {Color.UNDERLINE}"
                    f"greater than 0{Color.END}: "
                )
            )
        except ValueError:
            print(ERROR_MESSAGE)
            continue

        if goal_stdev <= 0:
            print(ERROR_MESSAGE)
            continue
        else:
            break

    # calculations
    sample_avg = sample_total / 5
    lower_bound, upper_bound = bound_calc(goal_avg, goal_stdev)

    # outputs
    print(
        f"\nThe {Color.CYAN}{Color.UNDERLINE}sample average{Color.END} is "
        f"{Color.BLUE}{sample_avg:.2f}{Color.END} \n"
        f"The {Color.CYAN}{Color.UNDERLINE}lower bound{Color.END} is "
        f"{Color.BLUE}{lower_bound:.2f}{Color.END} \n"
        f"The {Color.CYAN}{Color.UNDERLINE}upper bound{Color.END} is "
        f"{Color.BLUE}{upper_bound:.2f}{Color.END} \n"
    )

    if sample_avg >= lower_bound and sample_avg <= upper_bound:
        print("Sample average is within bounds. ^_^")
    elif sample_avg > upper_bound:
        print("Sample average is greater than upper bound. :(")
    else:
        print("Sample average is lesser than lower bound. (")


main()
