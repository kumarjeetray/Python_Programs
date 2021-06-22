class Employee:
    def __init__(self, name, age, dob, job_description):
        self.name = name
        self.age = age
        self.dob = dob
        self.job_description = job_description

    def get_salary(self):
        print("SALARY= $400")


class Manager(Employee):
    def __init__(self,  name, age, dob, job_description, department, employees):
        super().__init__(name, age, dob, job_description)
        self.department = department
        self.employees = employees

# super or parent class name can be used to initialize parent attributes


class Assistant(Employee):
    def __init__(self, name, age, dob, job_description, managers, working_hours):
        Employee.__init__(self, name, age, dob, job_description)
        self.managers = managers
        self.working_hours = working_hours


manager = Manager("kim", 27, "23-8-2000",
                  "manages every thing", "Engineering", 87)
manager.get_salary()