# 📚 Course Management System

> A lightweight Python-based system for managing students, courses, grades, attendance, and academic rankings with visualization support.

## 📖 Description

The **Course Management System** is a simple yet powerful command-line application designed to help educators and administrators manage academic data efficiently. Built with Python, it provides an intuitive interface for tracking student performance, recording attendance, generating rankings, and visualizing grade distributions.

This project was developed as a modular system where three developers can work on separate components simultaneously, making it ideal for collaborative learning or small educational institutions.

---

## ✨ Features

### Core Functionality
- 👥 **Student Management** - Add, view, and manage student records
- 📖 **Course Management** - Create and organize courses with instructor information
- 📝 **Enrollment System** - Enroll students in multiple courses
- 📊 **Assessment Tracking** - Create various types of assessments (exams, quizzes, assignments)
- 🎯 **Grade Recording** - Record and view student grades linked to specific assessments
- 📅 **Attendance Tracking** - Mark and view attendance records by date

### Additional Features
- 🏆 **Student Rankings** - Automatic ranking system with medal indicators (🥇🥈🥉)
  - Course-specific rankings
  - Overall cross-course rankings
- 📈 **Grade Visualization** - Interactive bar charts showing grade distributions
  - Color-coded by performance level (A-F grades)
- 💾 **Data Persistence** - Save and load all data using JSON format
- 🎨 **User-Friendly Interface** - Clean command-line menu system

---

## 🚀 How to run the code

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/course-management-system.git
   cd course-management-system
   ```

2. **Install required dependencies**
   ```bash
   pip install matplotlib
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

---

## 📁 Project Structure

```
course-management-system/
│
├── models.py                      # Data models (Student, Course, Assessment, Grade, Attendance)
├── student_course_manager.py     # Student & course operations 
├── assessment_grade_manager.py   # Assessment & grade operations 
├── attendance_reporting.py       # Attendance, rankings, visualization 
├── main.py                        # Main application entry point
├── data.json                      # Auto-generated data file (after first save)
└── README.md                      # Project documentation
```

## 🎮 Usage Guide

### Main Menu Options

```
========================================
COURSE MANAGEMENT SYSTEM
========================================
1. Add Student       9. View Grades
2. Add Course        10. View Attendance
3. Enroll Student    11. Course Rankings
4. Add Assessment    12. Overall Rankings
5. Record Grade      13. Plot Grades
6. Mark Attendance   14. Save Data
7. View Students     15. Load Data
8. View Courses      0. Exit
========================================
```

### Quick Start Example

```bash
# 1. Add a student
Choice: 1
ID: S001
Name: Luke
Email: luke@email.com

# 2. Add a course
Choice: 2
ID: CS101
Name: Introduction to Programming
Instructor: Dr. Smith

# 3. Enroll student in course
Choice: 3
Student ID: S001
Course ID: CS101

# 4. Create an assessment
Choice: 4
Assessment ID: A001
Course ID: CS101
Name: Midterm Exam
Max Score: 100
Type: Exam

# 5. Record a grade
Choice: 5
Student ID: S001
Assessment ID: A001
Score: 85

# 6. Mark attendance
Choice: 6
Student ID: S001
Course ID: CS101
Date (YYYY-MM-DD): 2026-01-20
Status (Present/Absent): Present

# 7. View rankings
Choice: 11
Course ID: CS101

=== RANKINGS: Introduction to Programming ===
🥇#1 Luke: 85.0%

# 8. Visualize grades
Choice: 13
Course ID: CS101
[Opens interactive chart window]

# 9. Save your work
Choice: 14
✓ Saved!
```

---

## 📊 Features in Detail

### Rankings System

The system automatically calculates student rankings based on their overall performance:

- **Course Rankings**: Rank students within a specific course
- **Overall Rankings**: Rank students across all enrolled courses
- **Medal System**: Top 3 students receive medal indicators (🥇🥈🥉)
- **Percentage Display**: Shows exact performance percentage

Example output:
```
=== RANKINGS: Introduction to Programming ===
🥇#1 Luke: 92.5%
🥈#2 Tony Stark: 87.3%
🥉#3 Bruce Wayne: 84.1%
#4 Peter Parker: 78.9%
```

### Grade Visualization

Interactive matplotlib charts showing:
- **Bar Chart**: Individual student performance
- **Color Coding**:
  - 🟢 Dark Green: A (90-100%)
  - 🟢 Light Green: B (80-89%)
  - 🟡 Gold: C (70-79%)
  - 🟠 Orange: D (60-69%)
  - 🔴 Red: F (below 60%)

### Data Persistence

All data is saved in JSON format (`data.json`), including:
- Student records
- Course information
- Assessments
- Grades
- Attendance records

Simply use option 14 to save and option 15 to load your data anytime!

---

## 🛠️ Development

**Ishan: Student & Course Management**
- Implement `student_course_manager.py`
- Handle student/course CRUD operations
- Manage enrollment

**Krina: Assessment & Grade Management**
- Implement `assessment_grade_manager.py`
- Create an assessment system
- Record and manage grades

**Iméne: Attendance & Reporting**
- Implement `attendance_reporting.py`
- Track attendance
- Build a ranking system
- Create visualizations
- Handle file I/O

---

## 📝 Assessment Types

The system supports various assessment types:
- **Exam** - Midterms, finals, tests
- **Quiz** - Short assessments
- **Assignment** - Homework, projects
- **Project** - Major coursework
- **Lab** - Practical work
- **Participation** - Class engagement

---

## 👥 Authors

- **Ishan Fernandes** - *Student and Course Management* - [scn01](https://github.com/scn01)
- **Krina Patel** - *Assessment / Grade Manager* - [krina2310](https://github.com/Krina2310)
- **Iméne Kadri** - *Attendance Management* - [imenekadri006-cmd](https://github.com/imenekadri006-cmd)
