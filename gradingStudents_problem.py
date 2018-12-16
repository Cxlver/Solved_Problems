
def gradingStudents(grades):

    finalGrades = []

    for i in range(len(grades)):
        if grades[i] >= 38:
            nextMultOfFive = int(5 * round(float(grades[i]) / 5))
            if nextMultOfFive - grades[i] < 3 and nextMultOfFive > grades[i]:
                grade = grades[i] + (nextMultOfFive - grades[i])
                finalGrades.append(grade)
            else:
                finalGrades.append(grades[i])
        else:
            finalGrades.append(grades[i])

    return finalGrades

if __name__ == '__main__':

    n = int(input("Number of students: "))

    grades = []

    for _ in range(n):
        grades_item = int(input("Grade: "))
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

