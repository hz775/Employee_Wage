import random

class Employee:
    def __init__(self,emp_id,name,wage_per_hour,work_per_hour):
        self.name=name
        self.wage_per_hour=wage_per_hour
        self.work_per_hour=work_per_hour
        self.emp_id=emp_id
    
    def check_attendance(self):
        return random.randint(0, 1)  

    def check_attendance(self):
        self.attendance = random.randint(0, 1)

    def calculate_full_time_wage(self):
        self.check_attendance()
        if self.attendance == 1:
            self.daily_wage = self.work_per_hour * self.wage_per_hour
            return f"Employee id: {self.emp_id}\n{self.name} is Present"
        else:
            self.daily_wage = 0
            return f"Employee id: {self.emp_id}\n{self.name} is Absent\nDaily Wage: Rs.0"

    def part_time_full_time(self):
        if self.attendance != 1:
                    return ""

        match self.work_per_hour:               #here workperhour binds to hours
            case hours if hours > 8:
                return f"{self.name} is Full time\nFull time wage: Rs.{self.daily_wage}"
            case hours if hours <= 8:
                return f"{self.name} is Part time\nPart time wage: Rs.{self.daily_wage}"

            
    def calculate_monthly_wage(self):
        total_wage = 0
        total_present = 0
        print(f"Employee ID: {self.emp_id}, Name: {self.name}\n")

        for day in range(1, 21):
            self.check_attendance()
            if self.attendance == 1:
                self.daily_wage = self.work_per_hour * self.wage_per_hour
                total_wage += self.daily_wage
                total_present += 1

                if self.work_per_hour > 8:
                    work_type = "Full time"
                else:
                    work_type = "Part time"

                print(f"Day {day} -> Present, {work_type}, Work Time: {self.work_per_hour}, Daily Wage: {self.daily_wage}")
            else:
                self.daily_wage = 0
                print(f"Day {day} -> Absent, Work Time: {self.work_per_hour}, Daily Wage: 0")

        print(f"\nTotal Present Days: {total_present}")
        return  f"Total Monthly Wage: {total_wage}"
        

