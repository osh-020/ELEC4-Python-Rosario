# Joshua Soriano Rosario
# IV BSIT B
# P1
# 11/27/2026

# Accept Student's Grades
def grade():
    grades = []

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
# return number
# count = grades()
# print(count)

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
                    print("Grade must be atleast 0 to 1000")
                        
            except ValueError:
                print("Invalid Input. Enter a number")

    return grades

# to test  if the input grade works
# result = grade()
# print(result)

#calculate average
def average(grades):
    return sum(grades) / len(grades)

# test the average is right
# test = grade()
# result = average(test)
# print (result)

