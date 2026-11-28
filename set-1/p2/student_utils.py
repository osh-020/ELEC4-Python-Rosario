# Joshua Soriano Rosario
# IV BSIT B
# P2
# 11/28/2026

# #calculate average
def average(grades):
    return sum(grades) / len(grades)

# grade status if fail or pass
def grade_status(grades):
    if average(grades) >= 75:
        return "PASSED"
    else:
        return "Failed"

# get higest grad
def highest_grade(grades):
    return max(grades) 

# get lowest grade
def lowest_grade(grades):
    return min(grades) 
