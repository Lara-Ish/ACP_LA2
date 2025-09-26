class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name) # Tuple of (ID, Name)
        self.email = email # String email address
        self.grades = grades or {} # Dictionary of subject and grade
        self.courses = set(courses or []) # Set of unique courses

    def __str__(self): # String representation of the student
        courses_str = str(self.courses) if self.courses else "None"
        return (f"ID      : {self.id_name[0]}\n"
                f"Name    : {self.id_name[1]}\n"
                f"Email   : {self.email}\n"
                f"Courses : {courses_str}\n"
                f"Grades  : {self.grades}\n")

    def calculate_gpa(self): # Calculate GPA based on grades
        if not self.grades:
            return 0.0
        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        total_points = 0
        for grade in self.grades.values():
            total_points += grade_points.get(grade, 0.0)

class StudentRecords:
    def __init__(self):
        self.students = []

    #add a student
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        if self.find_student(student_id):
            return "Student with this ID already exists."
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return "Student added successfully."

    #find a student by ID
    def find_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return student
        return None
    
    #update student information
    def update_student(self, student_id, email=None, grades=None, courses=None):
        student = self.find_student(student_id)
        if not student:
            return "Student not found."
        if email:
            student.email = email
        if grades:
            student.grades.update(grades)
        if courses:
            student.courses.update(courses)
        return "Student information updated successfully."

    #delete a student by ID
    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if not student:
            return "Student not found."
        self.students.remove(student)
        return "Student deleted successfully."

    #enroll a student in a course
    def enroll_course(self, student_id, course):
        student = self.find_student(student_id)
        if not student:
            return "Student not found."
        student.courses.add(course)
        return f"Student enrolled in {course}."

    #search for a student by ID
    def search_student(self, student_id):
        student = self.find_student(student_id)
        return str(student) if student else "Student not found."

    #search for students by name 
    def search_by_name(self, name):
        results = [str(s) for s in self.students if name.lower() in s.id_name[1].lower()]
        return results if results else "No students found with that name."

    #view all student records
    def view_all_students(self):
        if not self.students:
            return "No student records available."
        return '\n'.join(str(s) for s in self.students)

records = StudentRecords()

print(records.add_student(1, "Acer Martinez", "acerM@gmail.com", {'Math': 'A', 'History': 'B'}, ['Math', 'History']))
print(records.add_student(2, "Macey De Villa", "maceydevilla@gmail.com"))
print(records.add_student(3, "Art Valdez", "artxvaldez@gmail.com"))

print("\nRecords: ")
print(records.view_all_students())

print("\n")
print(records.enroll_course(2, "Science"))

print("\nNew Records of Student 1: ")
print(records.update_student(2, courses=['Science'], grades={'Science': 'A'}))

print("\nSearch by name 'Lili':")
print(records.search_by_name("bob"))

print(records.delete_student(3))

print(records.add_student(3, "Carl Mercado", "carlM@gmail.com", {'Math': 'C', 'History': 'B'}, ['Math', 'History']))
print(records.add_student(4, "Stacey Marie Fernandez", "staceymarie@gmail.com", {'Math': 'A', 'History': 'A', 'Science': 'A'}, ['Math', 'History', 'Science']))

print("\nUpdated Records: ")
print(records.view_all_students())
