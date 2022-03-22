from datetime import datetime

class StudentMark():
    class Student():
        def studentCount (student):
            student.count = int (input ("Enter number of students: "))
            return student.count

        def studentDetails (student):
            student.sID = input ("Student id: ")
            student.sname = input ("Student name: ")
            student.sdob = input("Student's DOB:")
            student.setDOB=datetime.strptime(student.sdob, "%d/%m/%Y")
            return student.sID, student.sname, student.setDOB
            
        def studentList(student):
            sdtList = []
            for i in range(student.count):
                sdtList.append ((student.sID, student.sname, student.setDOB))
                sdtList.sort()       
            for s in sdtList:
                print (f"Student id: {s[0]} Name: {s[1]} Date of birth: {s[2]}")      
            
    class Course():
        def courseCount (course):
            course.count = int (input ("Enter number of courses: "))

        def courseDetails (course):
            course.cID = input ("Course id: ")
            course.cname = input ("Course name: ")
            return course.cID, course.cname
            
        def courseList(course):
            crsList = []
            for i in range(course.count):
                crsList.append ((course.cID, course.cname))
                crsList.sort()       
            for c in crsList:
                print (f"Course id: {c[0]} Name: {c[1]}")                

    class StudentMark(Student,Course):            
        def StudentMarkCount(m):
            m.count = int (input ("How many student marks/courses do you want to enter? "))
                    
        def studentMark(m):
            m.courseDetails()
            m.studentDetails()
            m.mark = float(input("Enter marks: "))
            sml = []
            for i in range(m.count):
                sml.append((m.sname,m.mark))
                sml.sort()
            for l in sml:
                print(f"Student {l[0]} got {l[1]} points")
               

    
    std = Student()
    std.studentCount()
    std.studentDetails()
    std.studentList()
    
    crs = Course()
    crs.courseCount()
    crs.courseDetails()
    crs.courseList
    
    sm = StudentMark()
    sm.StudentMarkCount()
    sm.studentMark()
    
        