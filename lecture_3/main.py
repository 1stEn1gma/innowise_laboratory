import re


class StudentsCollision(Exception):
    pass


class StudentIncorrectName(Exception):
    pass


class NoStudent(Exception):
    pass


def get_student_uppered_name() -> str:
    """
    Ask the user to enter a name and check it for correctness.

    Return the user's name in uppercase.
    """
    st_name = input("Enter student name: ")
    st_uppered_name = st_name.upper()

    if re.search(r"[^A-Z \-]", st_uppered_name):
        raise StudentIncorrectName

    return st_uppered_name


def get_average_grade(x: list[float]) -> float:
    """
    Get list of float.

    Return the arithmetic mean.
    """
    return sum(x) / len(x)


students: list[dict] = []

exit_bool = False

print("--- Student Grade Analyzer ---")

while not exit_bool:
    print("1. Add a new student\n"
          "2. Add a grades for a student\n"
          "3. Show report (all students)\n"
          "4. Find top performer\n"
          "5. Exit\n")

    user_choice = input("Enter your choice: ")
    clear_user_choice = re.sub(r"[\s.]", '', user_choice)

    # ------------------ OPTION 1 ------------------
    if clear_user_choice == "1":
        try:
            uppered_name = get_student_uppered_name()

            for student in students:
                if student["name"] == uppered_name:
                    raise StudentsCollision

            students.append({"name": uppered_name, "grades": []})

        except StudentIncorrectName:
            print("Incorrect name. A-Z, a-z, -, and space can be used")
        except StudentsCollision:
            print("Student already exist")

    # ------------------ OPTION 2 ------------------
    elif clear_user_choice == "2":
        try:
            uppered_name = get_student_uppered_name()

            current_student_index = -1

            for index, student in enumerate(students):
                if student["name"] == uppered_name:
                    current_student_index = index
                    break

            if current_student_index == -1:
                raise NoStudent

            current_student = students[current_student_index]

            while True:
                try:
                    grade_str = input("Enter a grade (or \'done\' to finish): ")

                    if grade_str.lower() == "done":
                        break

                    grade_int = int(grade_str)

                    if grade_int < 0 or grade_int > 100:
                        raise ValueError

                    current_student["grades"].append(grade_int)
                except ValueError:
                    print("Invalid value. (0-100)\n")
        except StudentIncorrectName:
            print("Incorrect name. A-Z, a-z, -, and space can be used\n")
        except NoStudent:
            print("There is no student with that name.\n")

    # ------------------ OPTION 3 ------------------
    elif clear_user_choice == "3":
        average_grades = []

        print("--- Student report ---")

        for student in students:
            student_name = student["name"]

            try:
                average_grade = get_average_grade(student["grades"])
                average_grades.append(average_grade)
                print(f"{student_name}\'s average grade is {average_grade}\n")
            except ZeroDivisionError:
                print(f"{student_name}\'s average grade is N/A\n")
        print("-----------------------------")

        try:
            overall_average = get_average_grade(average_grades)

            best_average_grade = max(average_grades)
            worst_average_grade = min(average_grades)

            print(f"Max average: {best_average_grade}\n"
                  f"Min average: {worst_average_grade}\n"
                  f"Overall average: {overall_average}\n")

        except ZeroDivisionError:
            print("No students or no grades\n")

    # ------------------ OPTION 4 ------------------
    elif clear_user_choice == "4":
        if students:
            best_student = max(students,
                               key=lambda student: get_average_grade(student["grades"]) if student["grades"] else -1)
            if not best_student["grades"]:
                print("No grades\n")
            else:
                max_average = get_average_grade(best_student["grades"])

                best_students = [
                    student["name"] for student in students
                    if student["grades"] and get_average_grade(student["grades"]) == max_average
                ]

                best_students_str = ", ".join(best_students)

                print(f"The student(s) with the highest average is(are) {best_students_str} "
                      f"with a grade of {max_average}\n")
        else:
            print("No students\n")

    # ------------------ OPTION 5 ------------------
    elif clear_user_choice == "5":
        exit_bool = True

    else:
        print("Incorrect input")
