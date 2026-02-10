# All Classes

# Represents a student in the system
class Student:
    # Creating a new student with ID, name, and email
    def __init__(self, student_id, name, email):
        self.student_id, self.name, self.email = student_id, name, email
        self.enrolled_courses = []  # List of courses this student is taking
    
    # Converting student data to a dictionary for saving to file
    def to_dict(self):
        return {'student_id': self.student_id, 'name': self.name, 'email': self.email}

# Represents a course in the system
class Course:
    # Creating a new course with ID, name, and instructor
    def __init__(self, course_id, course_name, instructor):
        self.course_id, self.course_name, self.instructor = course_id, course_name, instructor
        self.enrolled_students = []  # List of students taking this course
    
    # Adding a student to this course
    def add_student(self, student):
        # Checking if student is not already enrolled
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)  # Adding student to course
            student.enrolled_courses.append(self)  # Adding course to student's list
            return True
        return False
    
    # Converting course data to a dictionary for saving to file
    def to_dict(self):
        return {'course_id': self.course_id, 'course_name': self.course_name, 'instructor': self.instructor}

# Representing an assessment (test, quiz, assignment, etc.)
class Assessment:
    # Creating a new assessment with ID, course, name, max score, and type
    def __init__(self, assessment_id, course, name, max_score, assessment_type):
        self.assessment_id, self.course, self.name = assessment_id, course, name
        self.max_score, self.assessment_type = max_score, assessment_type
    
    # Converting assessment data to a dictionary for saving to file
    def to_dict(self):
        return {'assessment_id': self.assessment_id, 'course_id': self.course.course_id,
                'name': self.name, 'max_score': self.max_score, 'assessment_type': self.assessment_type}

# Representing a grade for a student on an assessment
class Grade:
    # Creating a new grade linking student, assessment, and score
    def __init__(self, student, assessment, score):
        self.student, self.assessment, self.score = student, assessment, score
    
    # Converting grade data to a dictionary for saving to file
    def to_dict(self):
        return {'student_id': self.student.student_id, 'assessment_id': self.assessment.assessment_id, 'score': self.score}

# Represents an attendance record for a student in a course
class Attendance:
    # Creating a new attendance record with student, course, date, and status
    def __init__(self, student, course, date, status):
        self.student, self.course, self.date, self.status = student, course, date, status
    
    # Converting attendance data to a dictionary for saving to file
    def to_dict(self):
        return {'student_id': self.student.student_id, 'course_id': self.course.course_id, 'date': self.date, 'status': self.status}
