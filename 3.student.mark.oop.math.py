from datetime import datetime
import math 
import copy
import numpy as np

class StudentMark():
    class Student():
        students = []

        def studentCount(student):
            student.count = int (input ("Enter number of students: "))
            return student.count

        def studentDetail(student):
            for s in range(student.count):
                print(f"### Student {s+1} entry ###")
                student.sID = input ("Student id: ")
                student.sName = input ("Student name: ")
                student.sDOB = input("Student's DOB: ")
                student.setDOB=datetime.strptime(student.sDOB, "%d/%m/%Y")
                student.students.append(copy.copy(student))
            
        def studentList(student):
            for s in student.students:
                print (f"Student id: {s.sID} Name: {s.sName} Date of birth: {s.sDOB}")     
            
    class Course():
        courses = []

        def courseCount(course):
            course.count = int (input ("Enter number of courses: "))
            return course.count

        def courseDetail(course):
            for c in range(course.count):
                print(f"### Course {c+1} entry ###")
                course.cID = input ("Course id: ")
                course.cName = input ("Course name: ")
                course.courses.append(copy.copy(course))
            
        def courseList(course):
            for c in course.courses:
                print (f"Course id: {c.cID} Name: {c.cName} ")     
                
    class StudentMarkList(Student,Course):   
        smList = []
        def studentMarkCount(m):
            m.count = int (input ("How many student marks/courses do you want to enter? "))
            return m.count

        def getMark(m):
            m.mark = math.floor(float(input("Enter marks: ")))
            return m.mark
        
        def studentMarkDetail(m):
            for i in range(m.count):
                m.sName = input ("Student name: ")
                m.cID = input ("Course id: ")
                m.getMark()
                m.smList.append((copy.copy(m)))

        def markList(m):
            for l in m.smList:
                print(f"Student {l.sName} got {l.mark} points")
            gpa = np.average(m.smList)
               

    
    std = Student()
    std.studentCount()
    std.studentDetail()
    std.studentList()
    
    crs = Course()
    crs.courseCount()
    crs.courseDetail()
    crs.courseList()
    
    sm = StudentMarkList()
    sm.studentMarkCount()
    sm.studentMarkDetail()
    sm.markList()
    
        