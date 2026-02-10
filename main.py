
# Course Management System

from student_course_manager import StudentCourseManager
from assessment_grade_manager import AssessmentGradeManager
from attendance_reporting import AttendanceReporting

# Creating the three managers we need
scm = StudentCourseManager()
agm = AssessmentGradeManager(scm)
ar = AttendanceReporting(scm, agm)

# Keep running until user exits
while True:
    # Showing the menu
    print("\n" + "="*40)
    print("COURSE MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Student       9. View Grades")
    print("2. Add Course        10. View Attendance")
    print("3. Enroll Student    11. Course Rankings")
    print("4. Add Assessment    12. Overall Rankings")
    print("5. Record Grade      13. Plot Grades")
    print("6. Mark Attendance   14. Save Data")
    print("7. View Students     15. Load Data")
    print("8. View Courses      0. Exit")
    print("="*40)
    
    # Getting what the user wants to do
    choice = input("\nChoice: ").strip()
    
    # Adding a new student
    if choice == "1":
        scm.add_student(input("ID: "), input("Name: "), input("Email: "))

    # Adding a new course
    elif choice == "2":
        scm.add_course(input("ID: "), input("Name: "), input("Instructor: "))

    # Putting a student in a course
    elif choice == "3":
        scm.enroll_student(input("Student ID: "), input("Course ID: "))

    # Adding a new test or assignment
    elif choice == "4":
        aid = input("Assessment ID: ")
        cid = input("Course ID: ")
        name = input("Name: ")
        max_score = int(input("Max Score: "))

        # Asking what type of assessment it is
        print("\nType: 1=Exam, 2=Quiz, 3=Assignment, 4=Project")
        type_choice = input("Choose (press Enter for Exam): ").strip()

        # Matching the number to the type
        types = {
            "1": "Exam",
            "2": "Quiz", 
            "3": "Assignment",
            "4": "Project",
            "": "Exam" # Use Exam if nothing is entered
        }
        atype = types.get(type_choice, "Exam")
        agm.add_assessment(aid, cid, name, max_score, atype)

    # Giving a student a grade    
    elif choice == "5":
        agm.add_grade(input("Student ID: "), input("Assessment ID: "), float(input("Score: ")))

    # Mark if student was present or absent
    elif choice == "6":
        ar.mark_attendance(input("Student ID: "), input("Course ID: "), 
                          input("Date (DD-MM-YYYY): "), input("Status (Present/Absent): "))
    
    # Showing all students
    elif choice == "7":
        scm.view_all_students()

    # Showing all courses
    elif choice == "8":
        scm.view_all_courses()
    
    # Showing grades for one student
    elif choice == "9":
        agm.view_student_grades(input("Student ID: "))

    # Showing attendance for one student
    elif choice == "10":
        ar.view_attendance(input("Student ID: "))

    # Showing grade rankings for one course
    elif choice == "11":
        ar.display_course_rankings(input("Course ID: "))
    
    # Showing grade rankings for all courses
    elif choice == "12":
        ar.display_overall_rankings()

    # Showing a graph of grades for one course
    elif choice == "13":
        ar.plot_grades(input("Course ID: "))

    # Saving everything to a file
    elif choice == "14":
        ar.save_to_file()

    # Loading everything from a file
    elif choice == "15":
        ar.load_from_file()
    
    # Exiting the program
    elif choice == "0":
        print("Goodbye!")
        break

    # User entered something wrong
    else:
        print("Invalid choice!")
