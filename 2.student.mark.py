from datetime import datetime

class StudentMark():
    class Student():
        def studentCount(student):
            student.count = int (input ("Enter number of students: "))
            return student.count

        def studentDetail(student):
            student.sID = input ("Student id: ")
            student.sName = input ("Student name: ")
            student.sDOB = input("Student's DOB:")
            student.setDOB=datetime.strptime(student.sDOB, "%d/%m/%Y")
            return student.sID, student.sName, student.setDOB
            
        def studentList(student):
            sList = []
            for i in range(student.count):
                sList.append ((student.sID, student.sName, student.setDOB))
                sList.sort()       
            for s in sList:
                print (f"Student id: {s[0]} Name: {s[1]} Date of birth: {s[2]}")      
            
    class Course():
        def courseCount(course):
            course.count = int (input ("Enter number of courses: "))
            return course.count

        def courseDetail(course):
            course.cID = input ("Course id: ")
            course.cName = input ("Course name: ")
            return course.cID, course.cName
            
        def courseList(course):
            cList = []
            for i in range(course.count):
                cList.append ((course.cID, course.cName))
                cList.sort()       
            for c in cList:
                print (f"Course id: {c[0]} Name: {c[1]}")                

    class StudentMarkList(Student,Course):             
        def studentMarkCount(m):
            m.count = int (input ("How many student marks/courses do you want to enter? "))
            return m.count
                    
        def markList(m):
            m.courseDetail()
            m.studentDetail()
            
            mark = float(input("Enter marks: "))
            smList = []
            for i in range(m.count):
                smList.append((m.sName,mark))
                smList.sort()
            for l in smList:
                print(f"Student {l[0]} got {l[1]} points")
               

    
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
    sm.markList()
    
        