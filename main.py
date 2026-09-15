# --------------------------------
# Calculate Percentage
# --------------------------------

def calculate_percentage(total, number_of_subjects):

    maximum_marks = number_of_subjects * 100

    percentage = (total / maximum_marks) * 100

    return percentage


# --------------------------------
# Calculate Grade
# --------------------------------

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    elif percentage >= 40:
        return "E"

    else:
        return "F"


# --------------------------------
# Check Overall Result
# --------------------------------

def check_result(marks):

    for mark in marks:

        if mark < 40:
            return "FAIL"

    return "PASS"


# --------------------------------
# Display Report
# --------------------------------

def display_report(name, subjects, marks, total, percentage, overall_grade, result):

    print("\n========== REPORT CARD ==========")

    print("Student:", name)

    print("\nSubject         Marks      Grade      Status")
    print("--------------------------------------------")

    passed = 0
    failed = 0

    for i in range(len(subjects)):

        subject = subjects[i]
        mark = marks[i]

        subject_grade = calculate_grade(mark)

        if mark >= 40:

            status = "PASS"
            passed += 1

        else:

            status = "FAIL"
            failed += 1

        print(f"{subject:<15} {mark:<10} {subject_grade:<10} {status}")

    print("--------------------------------------------")

    print("Total:", total)
    print("Percentage:", percentage, "%")
    print("Overall Grade:", overall_grade)
    print("Result:", result)
    print("Passed:", passed)
    print("Failed:", failed)

    print("============================================")


# --------------------------------
# Save Result
# --------------------------------

def save_result(name, subjects, marks, total, percentage, overall_grade, result):

    with open("student_results.txt", "a") as file:

        file.write("\n========== STUDENT RESULT ==========\n")

        file.write(f"Student: {name}\n")

        for i in range(len(subjects)):

            subject = subjects[i]
            mark = marks[i]

            subject_grade = calculate_grade(mark)

            if mark >= 40:
                status = "PASS"
            else:
                status = "FAIL"

            file.write(
                f"{subject}: {mark} | Grade: {subject_grade} | {status}\n"
            )

        file.write(f"Total: {total}\n")
        file.write(f"Percentage: {percentage}%\n")
        file.write(f"Overall Grade: {overall_grade}\n")
        file.write(f"Result: {result}\n")

        file.write("====================================\n")


# --------------------------------
# View Saved Results
# --------------------------------

def view_saved_results():

    try:

        with open("student_results.txt", "r") as file:

            content = file.read()

            if content:

                print("\n========== SAVED RESULTS ==========")
                print(content)
                print("===================================")

            else:

                print("\nNo saved results found.")

    except FileNotFoundError:

        print("\nNo saved results found.")


# --------------------------------
# Add Student
# --------------------------------

def add_student():

    name = input("Enter student name: ")

    number_of_subjects = int(input("Enter number of subjects: "))

    subjects = []
    marks = []

    for i in range(number_of_subjects):

        subject = input(f"Enter subject {i + 1} name: ")

        while True:

            try:

                mark = int(input(f"Enter marks for {subject}: "))

                if 0 <= mark <= 100:
                    break

                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:

                print("Please enter a valid number.")

        subjects.append(subject)
        marks.append(mark)

    total = sum(marks)

    percentage = calculate_percentage(
        total,
        number_of_subjects
    )

    overall_grade = calculate_grade(percentage)

    result = check_result(marks)

    save_result(
        name,
        subjects,
        marks,
        total,
        percentage,
        overall_grade,
        result
    )

    display_report(
        name,
        subjects,
        marks,
        total,
        percentage,
        overall_grade,
        result
    )


# --------------------------------
# MAIN MENU
# --------------------------------

while True:

    print("\n================================")
    print("      STUDENT GRADE SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. View Instructions")
    print("3. View Saved Results")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        print("\n========== INSTRUCTIONS ==========")
        print("1. Enter the correct student name.")
        print("2. Enter the number of subjects.")
        print("3. Marks must be between 0 and 100.")
        print("4. Minimum passing mark is 40.")
        print("5. You can enter any number of subjects.")
        print("6. Grade is calculated based on percentage.")
        print("==================================")

    elif choice == "3":

        view_saved_results()

    elif choice == "4":

        print("\nThank you for using Student Grade System!")
        break

    else:

        print("\nInvalid choice! Please enter 1, 2, 3, or 4.")