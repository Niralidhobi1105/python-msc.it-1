from datetime import datetime


class Course:
    def __init__(self, code, day, start, end):
        self.code = code
        self.day = day
        self.start = datetime.strptime(start, "%H:%M")
        self.end = datetime.strptime(end, "%H:%M")

        if self.start >= self.end:
            raise ValueError("End time must be greater than start time")

    def __str__(self):
        return f"{self.code} - {self.day} ({self.start.strftime('%H:%M')} - {self.end.strftime('%H:%M')})"


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        result = f"\nStudent ID: {self.student_id}\n"
        result += f"Student Name: {self.name}\n"
        result += f"Total Courses: {len(self.courses)}\n"

        for course in self.courses:
            result += str(course) + "\n"

        return result


# Main program

try:
    n = int(input("Enter number of students: "))

    if n <= 0:
        raise ValueError("Number of students must be greater than 0")

    students = []

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")

        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")

        student = Student(student_id, name)

        course_count = int(input("Enter number of courses: "))

        if course_count < 0:
            raise ValueError("Course count cannot be negative")

        for j in range(course_count):
            print(f"\nCourse {j + 1}")

            code = input("Enter Course Code: ")
            day = input("Enter Day: ")
            start = input("Enter Start Time (HH:MM): ")
            end = input("Enter End Time (HH:MM): ")

            course = Course(code, day, start, end)
            student.add_course(course)

        students.append(student)

    # Display results
    for student in students:

        print("\n==============================")
        print(student)

        conflicts = []

        # Check course conflicts
        for i in range(len(student.courses)):
            for j in range(i + 1, len(student.courses)):

                c1 = student.courses[i]
                c2 = student.courses[j]

                if c1.day.lower() == c2.day.lower():

                    if c1.start < c2.end and c2.start < c1.end:
                        conflicts.append((c1, c2))

        if conflicts:
            print("Conflicting Course Pairs:")

            for c1, c2 in conflicts:
                print(f"{c1.code} <--> {c2.code}")
        else:
            print("No conflict exists.")
            print("Student Timetable:")

            for course in student.courses:
                print(course)

except ValueError as e:
    print("Invalid input:", e)

except Exception as e:
    print("Error:", e)
    