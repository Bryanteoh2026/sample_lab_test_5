import csv

# -------------------------------------------------------
# Load employees.csv into a list of dictionaries
# -------------------------------------------------------
def load_employees(filename="employees.csv"):
    employees = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["hours_worked"] = float(row["hours_worked"])
            row["hourly_rate"]  = float(row["hourly_rate"])
            row["is_senior"]    = row["is_senior"].strip() == "True"
            employees.append(row)
    return employees


# -------------------------------------------------------
# Compute gross pay for one employee.
# Rules:
#   - First 40 hours: hourly_rate per hour
#   - Overtime (hours > 40): 1.5x hourly_rate per hour
#   - Senior bonus: add 10% of gross pay if is_senior == True
# -------------------------------------------------------
def calc_gross_pay(employee):
    regular_hours  = min(employee["hours_worked"], 40)
    overtime_hours = max(employee["hours_worked"] - 40, 0)
    gross = (regular_hours * employee["hourly_rate"]) + \
            (overtime_hours * employee["hourly_rate"] * 1.5)
    if employee["is_senior"]:
        gross *= 1.10
    return gross


# -------------------------------------------------------
# Display all records
# -------------------------------------------------------
def display_all_records(employees):
    print(f"\n{'ID':<6} {'Name':<15} {'Dept':<12} {'Hours':>6} {'Rate':>7} {'Senior':>7} {'Gross Pay':>10}")
    print("-" * 70)
    for e in employees:
        gross = calc_gross_pay(e)
        print(f"{e['id']:<6} {e['name']:<15} {e['department']:<12} {e['hours_worked']:>6.1f} "
              f"{e['hourly_rate']:>7.2f} {'Yes' if e['is_senior'] else 'No':>7} {gross:>10.2f}")


# -------------------------------------------------------
# REQ-01: Return list of employees in the given department
#         (case-insensitive). Return [] if none or empty.
# -------------------------------------------------------
def get_employees_by_department(employees, department):
    # TODO: Implement this function
    if not employees:
        return []
    employee_by_department = []
    for employee in employees:
        if employee["department"].lower() == department.lower():
            employee_by_department.append(employee)

    return employee_by_department



# -------------------------------------------------------
# REQ-02: Return the employee with the highest gross pay.
#         Return None if list is empty.
# -------------------------------------------------------
def get_highest_paid_employee(employees):
    # TODO: Implement this function
    if not employees:
        return None
    highest_emp = None
    highest_paid = -1
    for employee in employees:
        salary = calc_gross_pay(employee)
        if salary > highest_paid:
            highest_paid = salary
            highest_emp = employee

    return highest_emp



# -------------------------------------------------------
# REQ-03: Return the total payroll cost (sum of gross pay
#         for all employees). Return 0 if list is empty.
# -------------------------------------------------------
def calc_total_payroll(employees):
    # TODO: Implement this function
    if not employees:
        return 0
    total_payroll = 0
    for employee in employees:
        salary = calc_gross_pay(employee)
        total_payroll += salary

    return total_payroll

# -------------------------------------------------------
# REQ-04: Return a dict with the average gross pay per
#         department, e.g. {"Engineering": 1234.56, ...}
#         Departments with no employees are NOT included.
#         Return {} if list is empty.
# -------------------------------------------------------
def calc_avg_pay_by_department(employees):
    # TODO: Implement this function
    if not employees:
        return {}
    
    total = {}
    count = {}

    for employee in employees:
        dept = employee["department"]
        pay = calc_gross_pay(employee)

        if dept not in total:
            total[dept] = 0
            count[dept] = 0

        total[dept] += pay
        count[dept] += 1

    avg_by_dept = {}
    for dept in total:
        avg_by_dept[dept] = total[dept] / count[dept]

    return avg_by_dept

# -------------------------------------------------------
# Display statistics (calls REQ-03 and REQ-04)
# -------------------------------------------------------
def display_statistics(employees):
    total = calc_total_payroll(employees)
    avg_by_dept = calc_avg_pay_by_department(employees)
    print(f"\nTotal payroll cost : ${total:.2f}")
    print("\nAverage gross pay by department:")
    for dept, avg in avg_by_dept.items():
        print(f"  {dept:<15}: ${avg:.2f}")


# -------------------------------------------------------
# Display highest paid (calls REQ-02)
# -------------------------------------------------------
def display_highest_paid(employees):
    emp = get_highest_paid_employee(employees)
    if emp is None:
        print("\nNo records found.")
    else:
        gross = calc_gross_pay(emp)
        print(f"\nHighest paid employee:")
        print(f"  Name      : {emp['name']}")
        print(f"  Department: {emp['department']}")
        print(f"  Gross Pay : ${gross:.2f}")


# -------------------------------------------------------
# Display by department (calls REQ-01)
# -------------------------------------------------------
def display_by_department(employees):
    dept = input("Enter department: ").strip()
    results = get_employees_by_department(employees, dept)
    if not results:
        print(f"\nNo employees found in '{dept}'.")
    else:
        print(f"\nEmployees in '{dept}':")
        for e in results:
            print(f"  {e['name']} — Gross Pay: ${calc_gross_pay(e):.2f}")


# -------------------------------------------------------
# Main menu
# -------------------------------------------------------
def main():
    employees = load_employees()
    while True:
        print("\n" + "=" * 44)
        print("====== Employee Payroll System ======")
        print("=" * 44)
        print("Select option")
        print("1 - Display all records")
        print("2 - Display statistics")
        print("3 - Display highest paid employee")
        print("4 - Display employees by department")
        print("Q - Quit")
        print("=" * 44)
        choice = input("Enter selection => ").strip().upper()

        if choice == "1":
            display_all_records(employees)
        elif choice == "2":
            display_statistics(employees)
        elif choice == "3":
            display_highest_paid(employees)
        elif choice == "4":
            display_by_department(employees)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
