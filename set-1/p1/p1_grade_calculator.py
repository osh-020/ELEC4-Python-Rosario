# Joshua Soriano Rosario
# IV BSIT B
# P1
# 11/27/2026

grades = []

# Accept Student's Grades
def enter_grade():
    # to reset the grades if i want to calculate again
    grades.clear() 

    # Prompt hpw many grade to input?
    while True:
        try:
            number = int(input("Enter the number of grades you want to calculate: "))

            if number > 1:
                break
            else: 
                print ("Please enter at least 2 numbers")

        except ValueError:
            print("Invalid Input. Enter a whole number")

# to test  if the input number of grades works
#     return number
# test =  enter_grade()
# print(test)

    # lets loop
    for i in range(number):
        while True:
            try:
                input_grade = float(input("Enter grade: "))

                # zero-based grading
                if input_grade >= 0 and input_grade <= 100:
                    grades.append(input_grade)
                    break
                else:
                    print("Grade must be atleast 0 to 100")
                        
            except ValueError:
                print("Invalid Input. Enter a number")

    return grades

# # to test  if the input grade works
# result = enter_grade()
# print(result)

# #calculate average
def average(grades):
    return sum(grades) / len(grades)

# test the average is right
# grades = enter_grade()
# result = average(grades)
# print (result)

# get higest grad
def highest_grade(grades):
    return max(grades) 

# grade_list = grade()
# test = highest_grade(grades)
# print(test)

# get lowest grade
def lowest_grade(grades):
    return min(grades) 

# grade_list = grade()
# test = lowest_grade(grades)
# print(test)

# grade status if fail or pass
def grade_status(grades):
    if average(grades) >= 75:
        return "PASSED"
    else:
        return "Failed"

# test everything
# grades = grade()
# test1 = average(grades)
# test2 = highest_grade(grades)
# test3 = lowest_grade(grades)
# test4 = grade_status(grades)
# print (test1, test2, test3, test4)

def main():
    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("\nPick where you want to proceed")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter your selected choice to proceed: ")

        if choice == "1":
            enter_grade()
            print("Grades successfully entered!")

        elif choice == "2":
            if len(grades) == 0:
                print("Please enter grades first.")
            else:
                print("\n===== GRADE RESULTS =====")
                print("Grades:", grades)
                print("Average:", round(average(grades), 2))
                print("Highest Grade:", highest_grade(grades))
                print("Lowest Grade:", lowest_grade(grades))
                print("Status:", grade_status(grades))

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


main()

# Difference between Local and Global variable
# A local variable is a variable that is declared inside a function 
# and is only accessible inside the function.
# A global variable is a variable declared outside a function,
# where it can be accessed or used throughtout the program.
# Here at my program, number and input_grade are local variables 
# because they are declared inside enter_grade(), while grades[] which is at
# line 6 is global sincce its not enclosed by any functions 
# and, as you can read the program, I used it in every functions we have.