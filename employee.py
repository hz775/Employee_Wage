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
        total_hours = 0
        total_days = 0

        print(f"Employee ID: {self.emp_id}, Name: {self.name}\n")

        while total_days < 20 and total_hours + self.work_per_hour <= 100:
            total_days += 1
            self.check_attendance()

            if self.attendance == 1:
                self.daily_wage = self.work_per_hour * self.wage_per_hour
                total_wage += self.daily_wage
                total_present += 1
                total_hours += self.work_per_hour

                work_type = "Full time" if self.work_per_hour > 8 else "Part time"
                print(f"Day {total_days} -> Present, {work_type}, Work Time: {self.work_per_hour}, Daily Wage: Rs.{self.daily_wage}")
            else:
                self.daily_wage = 0
                print(f"Day {total_days} -> Absent, Work Time: {self.work_per_hour}, Daily Wage: Rs.0")

        print(f"\nTotal Present Days: {total_present}")
        print(f"Total Hours Worked: {total_hours}")
        return f"Total Monthly Wage: Rs.{total_wage}"
            

