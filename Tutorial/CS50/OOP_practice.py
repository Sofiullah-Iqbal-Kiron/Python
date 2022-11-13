# Instructor: David J. Malan
# CS50P - Lecture 8 - Object-Oriented Programming (2022)
# Course link: https://youtu.be/e4fwY9ZsxPw
# "code student.py" command will create a file called student.py in the current working directory
# and then open it with vs-code.

def get_name():
    return input("Name: ")


def get_house():
    return input("House: ")


def get_student():
    # returning as a tuple. Tuples are immutable.
    return (input("Name: "), input("House: "))


def get_student_as_dict():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


def main():
    student = get_student_as_dict()
    print(f"{student['name']} from {student['house']}")


main()
