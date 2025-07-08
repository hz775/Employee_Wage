import random

class Employee:
    def __init__(self,name):
        self.name=name
    
    def check_attendance(self):
        attendance=random.randint(0,1)
        if attendance==1:
            print(f"{self.name} is Present")
        else:
            print(f"{self.name} is Absent")