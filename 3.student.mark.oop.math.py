from datetime import datetime
import math 
import copy
import numpy as np
import curses
from curses import wrapper  

class StudentMark():
    students = []
        
    def studentCount(self):
        self.sCount = int (input ("Enter number of students: "))
        return self.sCount
    def studentDetail(self):
        for s in range(self.sCount):
            print(f"### Student {s+1} entry ###")
            self.sID = input ("Student id: ")
            self.sName = input ("Student name: ")
            self.sDOB = input("Student's DOB: ")
            self.setDOB=datetime.strptime(self.sDOB, "%d/%m/%Y")
            self.students.append(copy.copy(self))
    def studentList(self):
        for s in self.students:
            print (f"Student id: {s.sID} Name: {s.sName} Date of birth: {s.sDOB}")

    courses = []

    def courseCount(self):
        self.cCount = int (input ("Enter number of courses: "))
        return self.cCount

    def courseDetail(self):
        for c in range(self.cCount):
            print(f"### Course {c+1} entry ###")
            self.cID = input ("Course id: ")
            self.cName = input ("Course name: ")
            self.courses.append(copy.copy(self))
            
    def courseList(self):
        for c in self.courses:
            print (f"Course id: {c.cID} Name: {c.cName} ")     
        
    smList = []
    def studentMarkCount(self):
        self.smCount = int (input ("How many student marks/courses do you want to enter? "))
        return self.smCount
    marks = []
    def studentMarkDetail(self):
        for i in range(self.smCount):
            self.sName = input ("Student name: ")
            self.cID = input ("Course id: ")
            self.mark = math.floor(float(input("Enter marks: ")))
            self.marks.append(self.mark)
            self.smList.append((copy.copy(self)))
        

    def markList(self):
        for l in self.smList:
            print(f"Student {l.sName} got {l.mark} points")
    
    def getGPA(self):
        print("GPA: ")
        markLen = len(self.marks)
        gpa = []
        for i in range(self.sCount):
            average = np.average(self.marks[i:markLen:self.sCount])
            gpa.append(average)
        print(sorted(gpa, reverse=True))

stm = StudentMark()
stm.studentCount()
stm.studentDetail()
stm.studentList()
stm.courseCount()
stm.courseDetail()
stm.courseList()
stm.studentMarkCount()
stm.studentMarkDetail()
stm.markList()
stm.getGPA()
    