class Student:
    def __init__(self, student_id, student_name, email, grades = None, courses = None):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else []
        pass

        def __str__(self):
            return f"Student ID: {self.student_id}, Name: {self.student_name}, Email: {self.email}, Courses: {', '.join(self.courses)}, Grades: {self.grades}"
        
class StudentRecords:
            def add_student(self, student_id, student_name, email):
                new_student = Student(student_id, student_name, email)
                self.students.append(new_student)
                return "Student added successfully"
        
            def delete_student(self, student_id):
                for student in self.students:
                    if student.student_id == student_id:
                        self.students.remove(student)
                        return "Student deleted successfully"
                return "Student not found"
            

            
