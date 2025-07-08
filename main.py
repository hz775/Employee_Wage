from employee import Employee

# usecase1

emp1=Employee("E100","Hemanth",20,10)
emp1.check_attendance()

# usecase2
print(emp1.calculate_full_time_wage())

# usecase3
print(emp1.part_time_full_time())