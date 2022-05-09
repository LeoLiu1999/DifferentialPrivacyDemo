import csv
import names
import random


def generate_data(num_entries = 10000):
    """
    Generates a mock dataset of employees, their department, age, and their
    salary.
    
    `Gender` simulates a binomial attribute
    `Departments` simulates a more general categorical attribute
    `Age` simulates a bounded numerical attribute
    `Salaries` simulates an unbounded numerical attribute
    `Name` simulates a sparse attribute
    """
    NUM_OF_ENTRIES = 10000
    GENDER = ["male", "female"]
    DEPARTMENTS = ["Applied Physics", 
                   "Biomedical Engineering",
                   "Center for Urban Science and Progress",
                   "Chemical and Biomolecular Engineering",
                   "Civil and Urban Engineering",
                   "Computer Science and Engineering",
                   "Electrical and Computer Engineering",
                   "Finance and Risk Engineering",
                   "Mathematics",
                   "Mechanical and Aerospace Engineering",
                   "Technology, Culture and Society",
                   "Technology Management and Innovation"]
    DEPARTMENT_WEIGHTS = [77, 5, 67, 41, 25, 6, 21, 87, 55, 83, 14, 69]
    AGE_MIN = 18
    AGE_MAX = 80
    SALARY_MEAN = 100_000
    SALARY_STD_DEV = 50_000
    SALARY_MIN = 30_000

    for i in range(NUM_OF_ENTRIES):
        id = i
        gender = random.choice(GENDER)
        first_name = names.get_first_name(gender=gender)
        last_name = names.get_last_name()
        department = random.choices(DEPARTMENTS, weights=DEPARTMENT_WEIGHTS)[0]
        age = random.randint(AGE_MIN, AGE_MAX)
        salary = 0
        while salary < SALARY_MIN:
            salary = int(random.gauss(SALARY_MEAN, SALARY_STD_DEV))
        
        yield [id, first_name, last_name, gender, department, age, salary]
        

def generate_csv(filename = "employees.csv"):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "first_name", "last_name", "gender", 
                         "department", "age", "salary"])
        for employee in generate_data():
            writer.writerow(employee)


if __name__ == "__main__":
    generate_csv()