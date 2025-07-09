from employee import Employee
from company import Company
from multiple_company import Multiple_Company

if __name__ == "__main__":


    multiple_companies = Multiple_Company()

   
    multiple_companies.add_company("TCS", wage_per_hour=25, max_days=20, max_hours=100)
    multiple_companies.add_company("Infosys", wage_per_hour=30, max_days=22, max_hours=120)

    
    tcs = multiple_companies.get_company_by_name("TCS")
    if tcs:
        tcs.add_employee("T101", "Hemanth", work_time=9)
        tcs.add_employee("T102", "Rohan", work_time=8)

    
    infy = multiple_companies.get_company_by_name("Infosys")
    if infy:
        infy.add_employee("I101", "Ravi", work_time=8)
        infy.add_employee("I102", "Anusha", work_time=9)

    
    multiple_companies.calculate_all_wages()
