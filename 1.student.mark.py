from datetime import datetime

def studentCount ():
    return int (input ("Enter number of students: "))
    
def studentDetails ():
    studentId = input ("Student id: ")
    studentName = input ("Student name: ")
    if True:
       studentDOB = input ("Student's DOB: ")
       setDOB=datetime.strptime(studentDOB, "%d/%m/%Y")
            
    dob = str(setDOB.day) + "/" + str(setDOB.month) + "/" + str(setDOB.year)
    return studentId, studentName, dob
    
def courseCount ():
    return int (input ("Enter number of courses: "))
    
def courseDetails ():
    courseId = input ("Course id: ")
    courseName = input ("Course name: ")
    return courseId, courseName
    
students = studentCount ()
studentList = []
for i in range (students):
    studentId, studentName, setDOB = studentDetails ()
    studentList.append ((studentId, studentName, setDOB))
    studentList.sort() 

courses = courseCount ()
courseList = []
for i in range (courses):
    courseId, courseName = courseDetails ()
    courseList.append ((courseId, courseName))
    courseList.sort() 
    
l = {}
number = int (input ("How many student marks/courses do you want to enter? "))
  
for i in range (number):
    while True:
          studentId = input ("Student id: ")
          courseId = input ("Course id: ")
          if studentId not in [student [0] for student in studentList] :
              print ("Invalid id")
              continue 
          if courseId not in [course [0] for course in courseList]:
              print ("Invalid id")
              continue 
          break
    marks = float (input ("Enter marks: "))
      
    if courseId in l:
          l [courseId].append((studentId, marks))
    else:
          l [courseId] = [(studentId, marks)]
          
print ("\nStudent list")
for s in studentList:
    print (f"Student id: {s[0]} Name: {s[1]} Date of birth: {s[2]}")

print ("\nCourse list")
for c in courseList:
    print (f"Course id: {c[0]} Name: {c[1]}")
    
courseId = input ("\nWhich course id do you choose to see student marks? ")
if courseId in l:
    for tups in l [courseId]:
        print (f"Student {tups[0]} got {tups [1]} points")