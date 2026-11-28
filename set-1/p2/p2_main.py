# Joshua Soriano Rosario
# IV BSIT B
# P2
# 11/28/2026

# import module
import student_utils

# from module import name
from student_utils import average
from student_utils import grade_status
from student_utils import highest_grade
from student_utils import lowest_grade
from datetime import datetime

# global varable
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
                print("Lowest Grade:",lowest_grade(grades))
                print("Status:", grade_status(grades))

                 # display report date and time
                print("Report Generated:", datetime.now().strftime("%B %d, %Y %I:%M %p"))

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
 