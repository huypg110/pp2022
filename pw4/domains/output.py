import curses
from curses import wrapper 
students = []
def studentList(self):
        for s in self.students:
            print (f"Student id: {s.sID} Name: {s.sName} Date of birth: {s.sDOB}")
courses = []
def courseList(self):
        for c in self.courses:
            print (f"Course id: {c.cID} Name: {c.cName} ")  
smList = []        
def markList(self):
        for l in self.smList:
            print(f"Student {l.sName} got {l.mark} points")
            
