import pytest

'''
SAMPLE_EMPLOYEES = [
    {"id": "E001", "name": "Alice Tan",   "department": "Engineering", "hours_worked": 45.0, "hourly_rate": 25.00, "is_senior": True},
    {"id": "E002", "name": "Bob Lim",     "department": "Marketing",   "hours_worked": 38.0, "hourly_rate": 18.50, "is_senior": False},
    {"id": "E003", "name": "Carol Ng",    "department": "Engineering", "hours_worked": 50.0, "hourly_rate": 30.00, "is_senior": True},
    {"id": "E004", "name": "David Koh",   "department": "HR",          "hours_worked": 40.0, "hourly_rate": 20.00, "is_senior": False},
    {"id": "E005", "name": "Emma Wee",    "department": "Marketing",   "hours_worked": 42.0, "hourly_rate": 22.00, "is_senior": True},
    {"id": "E006", "name": "Faris Ahmad", "department": "Engineering", "hours_worked": 35.0, "hourly_rate": 28.00, "is_senior": False},
    {"id": "E007", "name": "Grace Ong",   "department": "HR",          "hours_worked": 48.0, "hourly_rate": 19.00, "is_senior": False},
    {"id": "E008", "name": "Henry Sim",   "department": "Marketing",   "hours_worked": 40.0, "hourly_rate": 21.50, "is_senior": True},
]
'''
# -------------------------------------------------------
# Tests for get_employees_by_department() [REQ-01]
# -------------------------------------------------------
def test_get_employees_by_department_engineering():
    # TODO: "Engineering" → 3 employees (Alice, Carol, Faris)
    pass

# -------------------------------------------------------
# Tests for get_highest_paid_employee() [REQ-02]
# -------------------------------------------------------
def test_get_highest_paid_employee():
    # TODO: Carol Ng has highest gross pay
    # Carol: 40*30 + 10*(30*1.5) = 1200+450=1650, *1.10 = 1815.00
    pass
# -------------------------------------------------------
# Tests for calc_total_payroll() [REQ-03]
# -------------------------------------------------------
def test_calc_total_payroll():
    # TODO: sum of all gross pays from SAMPLE_EMPLOYEES
    # Compute each manually and verify the total
    pass
# -------------------------------------------------------
# Tests for calc_avg_pay_by_department() [REQ-04]
# -------------------------------------------------------
def test_calc_avg_pay_by_department_keys():
    # TODO: returned dict must contain exactly Engineering, Marketing, HR
    pass