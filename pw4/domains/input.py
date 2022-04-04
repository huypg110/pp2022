from datetime import datetime
import math 
import copy
import numpy as np

def studentCount(self):
        self.sCount = int (input ("Enter number of students: "))
        return self.sCount
students = []
def studentDetail(self):
        for s in range(self.sCount):
            print(f"### Student {s+1} entry ###")
            self.sID = input ("Student id: ")
            self.sName = input ("Student name: ")
            self.sDOB = input("Student's DOB: ")
            self.setDOB=datetime.strptime(self.sDOB, "%d/%m/%Y")
            self.students.append(copy.copy(self))

def courseCount(self):
        self.cCount = int (input ("Enter number of courses: "))
        return self.cCount
courses = []
def courseDetail(self):
        for c in range(self.cCount):
            print(f"### Course {c+1} entry ###")
            self.cID = input ("Course id: ")
            self.cName = input ("Course name: ")
            self.courses.append(copy.copy(self))
            
def studentMarkCount(self):
        self.smCount = int (input ("How many student marks/courses do you want to enter? "))
        return self.smCount
smList = []
marks = []           
def studentMarkDetail(self):
        for i in range(self.smCount):
            self.sName = input ("Student name: ")
            self.cID = input ("Course id: ")
            self.mark = math.floor(float(input("Enter marks: ")))
            self.marks.append(self.mark)
            self.smList.append((copy.copy(self)))
def getGPA(self):
        print("GPA: ")
        markLen = len(self.marks)
        gpa = []
        for i in range(self.sCount):
            average = np.average(self.marks[i:markLen:self.sCount])
            gpa.append(average)
        print(sorted(gpa, reverse=True))