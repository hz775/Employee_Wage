import random

class Employee:
    def __init__(self,emp_id,name,wage_per_hour,work_per_hour):
        self.name=name
        self.wage_per_hour=wage_per_hour
        self.work_per_hour=work_per_hour
        self.emp_id=emp_id
    
    def check_attendance(self):
        attendance=random.randint(0,1)
        if attendance==1:
            return f"Present"
        else:
            return f"Absent"

    def calculate_full_time_wage(self):
        daily_wage=0
        if self.check_attendance():
            daily_wage = self.work_per_hour * self.wage_per_hour
            return f"Employee id:{self.emp_id}\n{self.name} is Present\nDaily Wage: Rs.{daily_wage}"
        else:
            return f"Employee id:{self.emp_id}\n{self.name} is Absent\nDaily Wage: Rs.0"

    
        

    

    