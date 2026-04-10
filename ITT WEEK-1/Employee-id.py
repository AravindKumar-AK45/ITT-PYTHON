
     

emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter Employee Name: ")
emp_designation = input("Enter Designation: ")


if emp_designation == "Manager":
    min_pay = 50000
    max_pay = 80000
elif emp_designation == "Developer":
    min_pay = 30000
    max_pay = 50000
elif emp_designation == "Intern":

    min_pay = 10000
    max_pay = 20000
else:
    min_pay = 20000
    max_pay = 40000

basic_salary = float(input("Enter Basic Salary: "))


if basic_salary < min_pay or basic_salary > max_pay:
    print("Invalid Basic Salary! It must be between", min_pay, "and", max_pay)
else:

    hra = 0.20 * basic_salary
    da = 0.10 * basic_salary
    pf = 0.12 * basic_salary
    gross_salary = basic_salary + hra + da
    net_salary = gross_salary - pf
    print("\n\t===Employee Payroll Details===")
    print("\tEmployee ID   :", emp_id)
    print("\tEmployee Name :", emp_name)
    print("\tDesignation   :", emp_designation)
    print("\tBasic Salary  :", basic_salary)
    print("\tHRA:", hra)
    print("\tDA:", da)
    print("\tPF:", pf)
    print("\tGross Salary  :", gross_salary)
    print("\tNet Salary    :", net_salary)
    print(" ")





