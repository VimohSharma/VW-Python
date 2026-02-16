class Company:
    def __init__(self,name,location):
        self.name=name
        self.location=location

    def show_details(self):
        print(f"Company's Name: {self.name}, Location: {self.location}")

class Employee:
    def __init__(self,emp_id,emp_name,designation):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.designation=designation
    
    def show_details(self):
        print(f"Employee Data: ID: {self.emp_id}, Name: {self.emp_name}, Designation: {self.designation}")


class CompanyAcquisition(Company):
    def __init__(self, name, location):
        super().__init__(name,location)
        self.employees=[]
    
    def add_employee(self,emp):
        self.employees.append(emp)
    
    def show_details(self):
        super().show_details()
        print("Merged Final Employee Data")
        for emp in self.employees:
            emp.show_details()
            print("----------------------------")

class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation,joining_date,previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date=joining_date
        self.previous_company=previous_company

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")

class Manager(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size=team_size

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")

class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, policies_handled):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.policies_handled=policies_handled
    
    def show_details(self):
        super().show_details()
        print(f"Policies Handled: {self.policies_handled}")

class Developer(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, programming_languages):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.programming_languages=programming_languages
    
    def show_details(self):
        super().show_details()
        print(f"Programming Languages: {', '.join(self.programming_languages)}")

class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, duration):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.duration=duration

    def show_details(self):
        super().show_details()
        print(f"Duration: {self.duration}")

class HRManager(Manager, HR):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size, policies_handled):
        # Initialize NewEmployee directly (same as DeveloperIntern!)
        NewEmployee.__init__(self, emp_id, emp_name, designation, joining_date, previous_company)
        
        # Set attributes manually
        self.team_size = team_size
        self.policies_handled = policies_handled

    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Team Size: {self.team_size}")
        print(f"Policies Handled: {self.policies_handled}")
        

class DeveloperIntern(Developer, Intern):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, programming_languages, duration):

        NewEmployee.__init__(self, emp_id, emp_name, designation, joining_date, previous_company)
        
        self.programming_languages = programming_languages
        self.duration = duration

    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Programming Languages: {', '.join(self.programming_languages)}")
        print(f"Internship Duration: {self.duration}")

class ManagerNew(HR, NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, policies_handled,team_size):
        NewEmployee.__init__(self, emp_id, emp_name, designation,
                    joining_date, previous_company)
        self.team_size = team_size
        self.policies_handled = policies_handled

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")

if __name__ == "__main__":
    company = CompanyAcquisition("TechIndia", "Bangalore")
    manager = Manager(10101, "Vips", "Manager", "15:01:2023", "TechHoola", 5)
    hr = HR(20202, "Rose", "HR Exec", "12:07:2025", "TechJoe", 10)
    developer = Developer(10201, "Vimoh", "SDE-1", "24:11:2025", "None", ["Python", "Java", "R"])
    intern = Intern(102, "Dave", "SDET", "01:02:2026", "None", "6 Months")
    dev_intern = DeveloperIntern(103, "Alara", "Dev_Intern", "12:09:2025", "TechAloha", ["C++, C, C#, Go"], "5 Months")
    hr_manager = HRManager(100, "Carter", "Head HR", "09:08:2024", "TechSure", 5, 10)
    mangern = ManagerNew(101203, "Jazi", "Executive", "19:09:2024", "TechMyth", 10, 20)
    
    company.add_employee(manager)
    company.add_employee(hr)
    company.add_employee(developer)
    company.add_employee(intern)
    company.add_employee(dev_intern)
    company.add_employee(hr_manager)
    company.add_employee(mangern)
    
    company.show_details()
