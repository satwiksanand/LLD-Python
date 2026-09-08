# association refers to a "has a" relationship between classes, in this one object needs to know about the existence of
# the other objects which they are not tightly coupled.

# In a UML Diagram, association is represented using a solid line, it can have an arrow to represent directionality
# as in object 1 having or knowing about the existence of the another object.

# There are two properties of association that are important
# 1. Directionality -> associated classes may or may not have directional relationship
# 2. Multiplicity -> this is about how many objects are related, 1-1, 1-n, and so on are some of the examples.

"""
ASSOCIATION AND MULTIPLICITY EXAMPLES

Multiplicity notation:
1       = exactly one
0..1    = zero or one
*       = zero or many
1..*    = one or many
"""


# ============================================================
# 1. UNIDIRECTIONAL ASSOCIATION (1 -> 1)
# ============================================================
#
# Person --------> Passport
#    1                1
#
# Person knows about Passport.
# Passport does NOT know about Person.
#


class Passport:
    def __init__(self, passport_number):
        self.passport_number = passport_number


class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport


# ============================================================
# 2. UNIDIRECTIONAL ASSOCIATION (1 -> *)
# ============================================================
#
# Department --------> Employee
#      1                 *
#
# One Department can have many Employees.
# Department knows its employees.
# Employee does NOT know its department.
#


class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


# ============================================================
# 3. BIDIRECTIONAL ASSOCIATION (1 <-> 1)
# ============================================================
#
# Person <--------> Passport
#    1                 1
#
# Both objects know about each other.
#


class PersonBidirectional:
    def __init__(self, name):
        self.name = name
        self.passport = None

    def assign_passport(self, passport):
        self.passport = passport
        passport.owner = self


class PassportBidirectional:
    def __init__(self, passport_number):
        self.passport_number = passport_number
        self.owner = None


# ============================================================
# 4. BIDIRECTIONAL ASSOCIATION (1 <-> *)
# ============================================================
#
# Department <-------> Employee
#      1                  *
#
# Department knows all employees.
# Each Employee knows their department.
#


class EmployeeBidirectional:
    def __init__(self, name):
        self.name = name
        self.department = None


class DepartmentBidirectional:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        employee.department = self


# ============================================================
# 5. BIDIRECTIONAL ASSOCIATION (* <-> *)
# ============================================================
#
# Student <---------> Course
#    *                  *
#
# One student can take multiple courses.
# One course can have multiple students.
#


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)


# ============================================================
# DEMONSTRATION
# ============================================================

if __name__ == "__main__":

    print("\n--- Unidirectional 1 -> 1 ---")

    passport = Passport("IND123456")
    person = Person("Katsu", passport)

    print(f"{person.name}'s passport: {person.passport.passport_number}")

    # passport.owner  # Doesn't exist


    print("\n--- Unidirectional 1 -> * ---")

    engineering = Department("Engineering")

    emp1 = Employee("Alice")
    emp2 = Employee("Bob")

    engineering.add_employee(emp1)
    engineering.add_employee(emp2)

    print(
        f"{engineering.name} employees:",
        [employee.name for employee in engineering.employees]
    )


    print("\n--- Bidirectional 1 <-> 1 ---")

    person = PersonBidirectional("Katsu")
    passport = PassportBidirectional("IND999999")

    person.assign_passport(passport)

    print(f"Person: {person.name}")
    print(f"Passport owner: {passport.owner.name}")


    print("\n--- Bidirectional 1 <-> * ---")

    department = DepartmentBidirectional("Backend Team")

    emp1 = EmployeeBidirectional("Alice")
    emp2 = EmployeeBidirectional("Bob")

    department.add_employee(emp1)
    department.add_employee(emp2)

    print(
        f"Department employees:",
        [employee.name for employee in department.employees]
    )

    print(f"{emp1.name}'s department: {emp1.department.name}")


    print("\n--- Bidirectional * <-> * ---")

    python_course = Course("Python")
    system_design = Course("System Design")

    student1 = Student("Katsu")
    student2 = Student("Alex")

    student1.enroll(python_course)
    student1.enroll(system_design)

    student2.enroll(python_course)

    print(
        f"{student1.name}'s courses:",
        [course.name for course in student1.courses]
    )

    print(
        f"{python_course.name} students:",
        [student.name for student in python_course.students]
    )