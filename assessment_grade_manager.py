from models import Assessment, Grade

class AssessmentGradeManager:
    # Setting up the manager with empty lists for assessments and grades
    def __init__(self, scm):
        self.scm, self.assessments, self.grades = scm, {}, []
    
    # Adding a new assessment to a course
    def add_assessment(self, aid, cid, name, max_score, atype="Exam"):
        # Checking if course exists and assessment ID is not already used
        c = self.scm.get_course(cid)
        if not c or aid in self.assessments:
            return print("Failed!")
        # Creating and saving the new assessment
        self.assessments[aid] = Assessment(aid, c, name, max_score, atype)
        print("Assessment added!")
    
    # Giving a grade to a student for an assessment
    def add_grade(self, sid, aid, score):
        # Getting the student and assessment
        s, a = self.scm.get_student(sid), self.assessments.get(aid)
        # Checking if student and assessment exist, and score is valid
        if not s or not a or score < 0 or score > a.max_score:
            return print("Invalid!")
        # Saving the grade
        self.grades.append(Grade(s, a, score))
        print(f"Grade: {score}/{a.max_score}")
    
    # Showing all grades for a student
    def view_student_grades(self, sid):
        # Finding the student
        s = self.scm.get_student(sid)
        if not s:
            return print("Not found!")
        
        # Printing header
        print(f"\n{'='*50}")
        print(f"GRADES FOR: {s.name}")
        print(f"{'='*50}")
        
        # Checking if student is enrolled in any courses
        if not s.enrolled_courses:
            print("Not enrolled in any courses.")
            return
        
        # Tracking total points across all courses
        overall_total = 0
        overall_max = 0
        
        # Going through each course the student is enrolled in
        for course in s.enrolled_courses:
            print(f"\n {course.course_name}")
            print("-" * 50)
            
            # Getting all grades for this student in this course
            grades = [g for g in self.grades if g.student == s and g.assessment.course == course]
            
            # If there are grades, show them
            if grades:
                # Tracking points for this course
                course_total = 0
                course_max = 0
                
                # Showing each grade
                for g in grades:
                    # Calculating percentage
                    pct = (g.score / g.assessment.max_score) * 100
                    print(f"  • {g.assessment.name}: {g.score}/{g.assessment.max_score} ({pct:.1f}%)")
                    course_total += g.score
                    course_max += g.assessment.max_score
                
                # Calculating and showing course average
                course_pct = (course_total / course_max) * 100
                grade_letter = self._get_letter(course_pct)
                print(f"\n  Course Total: {course_total}/{course_max} ({course_pct:.2f}%) - Grade: {grade_letter}")
                
                # Adding to overall totals
                overall_total += course_total
                overall_max += course_max
            else:
                print("No grades yet.")
        
        # Showing overall grade across all courses
        if overall_max > 0:
            overall_pct = (overall_total / overall_max) * 100
            overall_letter = self._get_letter(overall_pct)
            print(f"\n{'='*50}")
            print(f"OVERALL: {overall_total}/{overall_max} ({overall_pct:.2f}%) - Grade: {overall_letter}")
            print(f"{'='*50}\n")
    
    # Turning a percentage into a letter grade
    def _get_letter(self, percentage):
        if percentage >= 90: return "A"
        elif percentage >= 80: return "B"
        elif percentage >= 70: return "C"
        elif percentage >= 60: return "D"
        else: return "F"
