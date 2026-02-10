from models import Attendance
import json
import matplotlib.pyplot as plt

class AttendanceReporting:
    # Setting up the reporting system with empty attendance list
    def __init__(self, scm, agm):
        self.scm, self.agm, self.attendance_records = scm, agm, []
    
    # Marking if a student was present or absent for a class
    def mark_attendance(self, sid, cid, date, status):
        # Getting the student and course
        s, c = self.scm.get_student(sid), self.scm.get_course(cid)
        if not s or not c:
            return print("Invalid!")
        # Checking if status is valid
        if status not in ["Present", "Absent"]:
            return print("Status must be Present or Absent!")
        
        # Checking if date is in correct format (DD-MM-YYYY)
        try:
            parts = date.split('-')
            # Making sure format is correct: 2 digits, 2 digits, 4 digits
            if len(parts) != 3 or len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
                return print("Use DD-MM-YYYY format (e.g., 20-01-2026)!")
            # Checking if day and month are valid numbers
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
            if not (1 <= day <= 31 and 1 <= month <= 12):
                return print("Invalid date!")
        except:
            return print("Use DD-MM-YYYY format (e.g., 20-01-2026)!")
        
        # Saving the attendance record
        self.attendance_records.append(Attendance(s, c, date, status))
        print(f" {status}")
    
    # Showing all attendance records for a student
    def view_attendance(self, sid):
        # Finding the student
        s = self.scm.get_student(sid)
        if not s:
            return print("Not found!")
        # Printing all their attendance records
        print(f"\n=== ATTENDANCE: {s.name} ===")
        for a in [a for a in self.attendance_records if a.student == s]:
            print(f"{a.course.course_name} - {a.date}: {a.status}")
    
    # Showing student rankings for one course based on grades
    def display_course_rankings(self, cid):
        # Finding the course
        c = self.scm.get_course(cid)
        if not c:
            return print("Not found!")
        
        # Calculating average grade for each student in this course
        ranks = []
        for s in c.enrolled_students:
            # Getting all grades for this student in this course
            gs = [g for g in self.agm.grades if g.student == s and g.assessment.course == c]
            if gs:
                # Calculating percentage
                pct = (sum(g.score for g in gs) / sum(g.assessment.max_score for g in gs)) * 100
                ranks.append({'s': s, 'pct': pct})
        
        # Sorting students from highest to lowest grade
        ranks.sort(key=lambda x: x['pct'], reverse=True)
        
        # Printing the rankings
        print(f"\n=== RANKINGS: {c.course_name} ===")
        for i, r in enumerate(ranks, 1):
            # Adding medals for top 3 students
            m = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else ""
            print(f"{m}#{i} {r['s'].name}: {r['pct']:.1f}%")
    
    # Showing student rankings across all courses
    def display_overall_rankings(self):
        # Calculating average grade for each student across all courses
        ranks = []
        for s in self.scm.students.values():
            # Getting all grades for this student
            gs = [g for g in self.agm.grades if g.student == s]
            if gs:
                # Calculating overall percentage
                pct = (sum(g.score for g in gs) / sum(g.assessment.max_score for g in gs)) * 100
                ranks.append({'s': s, 'pct': pct})
        
        # Sorting students from highest to lowest grade
        ranks.sort(key=lambda x: x['pct'], reverse=True)
        # Printing the rankings
        print("\n=== OVERALL RANKINGS ===")
        for i, r in enumerate(ranks, 1):
            # Adding medals for top 3 students
            m = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else ""
            print(f"{m}#{i} {r['s'].name}: {r['pct']:.1f}%")
    
    # Showing a bar chart of grades for a course
    def plot_grades(self, cid):
        # Finding the course
        c = self.scm.get_course(cid)
        if not c:
            return
        
        # Getting grade data for each student
        data = []
        for s in c.enrolled_students:
            gs = [g for g in self.agm.grades if g.student == s and g.assessment.course == c]
            if gs:
                # Calculating percentage
                pct = (sum(g.score for g in gs) / sum(g.assessment.max_score for g in gs)) * 100
                data.append((s.name, pct))
        
        # Checking if there's any data to plot
        if not data:
            return print("No data!")
        
        # Separating names and percentages
        names, pcts = zip(*data)
        # Creating the bar chart
        plt.figure(figsize=(8, 5))
        bars = plt.bar(names, pcts)
        # Color bars based on grade level
        for i, b in enumerate(bars):
            p = pcts[i]
            # Green for A, light green for B, gold for C, orange for D, red for F
            b.set_color('darkgreen' if p >= 90 else 'lightgreen' if p >= 80 else 'gold' if p >= 70 else 'orange' if p >= 60 else 'red')
        # Adding labels and title
        plt.ylabel('Grade %')
        plt.title(f'{c.course_name} - Grades')
        plt.ylim(0, 100)
        plt.tight_layout()
        # Showing the chart
        plt.show()
    
    # Saving all data to a file
    def save_to_file(self, filename="data.json"):
        # Putting all data into one dictionary
        data = {
            'students': [s.to_dict() for s in self.scm.students.values()],
            'courses': [c.to_dict() for c in self.scm.courses.values()],
            'assessments': [a.to_dict() for a in self.agm.assessments.values()],
            'grades': [g.to_dict() for g in self.agm.grades],
            'attendance': [a.to_dict() for a in self.attendance_records]
        }
        # Write to file
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Saved!")
    
    # Load all data from a file
    def load_from_file(self, filename="data.json"):
        try:
            # Read the file
            with open(filename) as f:
                d = json.load(f)
            # Add all students
            for s in d.get('students', []):
                self.scm.add_student(s['student_id'], s['name'], s['email'])
            # Add all courses
            for c in d.get('courses', []):
                self.scm.add_course(c['course_id'], c['course_name'], c['instructor'])
            # Add all assessments
            for a in d.get('assessments', []):
                self.agm.add_assessment(a['assessment_id'], a['course_id'], a['name'], a['max_score'], a['assessment_type'])
            # Add all grades
            for g in d.get('grades', []):
                self.agm.add_grade(g['student_id'], g['assessment_id'], g['score'])
            # Add all attendance records
            for a in d.get('attendance', []):
                self.mark_attendance(a['student_id'], a['course_id'], a['date'], a['status'])
            print("Loaded!")
        except:
            print("File not found!")
