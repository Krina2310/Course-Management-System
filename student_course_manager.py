from models import Student, Course

class StudentCourseManager:
    # Setting up the manager with empty lists for students and courses
    def __init__(self):
        self.students, self.courses = {}, {}
    
    # Adding a new student to the system
    def add_student(self, student_id, name, email):
        # Checking if student ID is already used
        if student_id in self.students:
            return print("Student exists!")
        # Creating and save the new student
        self.students[student_id] = Student(student_id, name, email)
        print("Student added!")
    
    # Adding a new course to the system
    def add_course(self, course_id, course_name, instructor):
        # Checking if course ID is already used
        if course_id in self.courses:
            return print("Course exists!")
        # Creating and save the new course
        self.courses[course_id] = Course(course_id, course_name, instructor)
        print("Course added!")
    
    # Putting a student in a course
    def enroll_student(self, student_id, course_id):
        # Getting the student and course
        s, c = self.students.get(student_id), self.courses.get(course_id)
        # Checking if both exist and add student to course
        if s and c and c.add_student(s):
            print(f"{s.name} enrolled!")
        else:
            print("Failed!")
    
    # Finding and return a student by their ID
    def get_student(self, sid):
        return self.students.get(sid)
    
    # Finding and return a course by its ID
    def get_course(self, cid):
        return self.courses.get(cid)
    
    # Showing all students in the system
    def view_all_students(self):
        print("\n=== STUDENTS ===")
        for s in self.students.values():
            print(f"{s.student_id}: {s.name}")
    
    # Showing all courses in the system
    def view_all_courses(self):
        print("\n=== COURSES ===")
        for c in self.courses.values():
            print(f"{c.course_id}: {c.course_name}")

