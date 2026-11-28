# Joshua Soriano Rosario
# IV BSIT B
# P1
# 11/27/2026

grades = []

# Accept Student's Grades
def enter_grade():

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
                grade = float(input("Enter grade: "))

                # zero-based grading
                if grade >= 0 and grade <= 100:
                    grades.append(grade)
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
def average(grade_list):
    return sum(grade_list) / len(grade_list)

# test the average is right
# grades = enter_grade()
# result = average(grades)
# print (result)
