# This program will teach children basic math skills by
# presenting them with simple addition and subtraction problems

import random

# Function to present an addition problem to the child
def present_addition_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Print the problem to the child
    print(f"What is {num1} + {num2}?")
    
    # Get the child's answer
    answer = int(input())
    
    # Check the answer and give feedback
    if answer == num1 + num2:
        print("Correct! Great job!")
    else:
        print(f"Incorrect. The correct answer is {num1 + num2}.")

# Function to present a subtraction problem to the child
def present_subtraction_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Make sure num1 is larger than num2
    if num1 < num2:
        num1, num2 = num2, num1
    
    # Print the problem to the child
    print(f"What is {num1} - {num2}?")
    
    # Get the child's answer
    answer = int(input())
    
    # Check the answer and give feedback
    if answer == num1 - num2:
        print("Correct! Great job!")
    else:
        print(f"Incorrect. The correct answer is {num1 - num2}.")

# Main function to run the program
def main():
    # Present 10 addition problems to the child
    for i in range(10):
        present_addition_problem()
        
    # Present 10 subtraction problems to the child
    for i in range(10):
        present_subtraction_problem()

# Run the main function
main()
