import pytest
from labsample5 import (
    calc_gross_pay,
    get_employees_by_department,
    get_highest_paid_employee,
    calc_total_payroll,
    calc_avg_pay_by_department,
)

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

# -------------------------------------------------------
# Tests for calc_gross_pay() [helper]
# -------------------------------------------------------
def test_calc_gross_pay_no_overtime_no_senior():
    # TODO: Bob Lim: 38hrs * $18.50, no OT, not senior
    # Expected: 38 * 18.50 = 703.00
    pass

def test_calc_gross_pay_with_overtime_no_senior():
    # TODO: Grace Ong: 40*19 + 8*(19*1.5), not senior
    # Expected: 760 + 228 = 988.00
    pass

def test_calc_gross_pay_no_overtime_senior():
    # TODO: Henry Sim: 40*21.50, senior (+10%)
    # Expected: 860 * 1.10 = 946.00
    pass

def test_calc_gross_pay_overtime_and_senior():
    # TODO: Alice Tan: 40*25 + 5*(25*1.5) = 1000+187.5 = 1187.5, then *1.10
    # Expected: 1187.50 * 1.10 = 1306.25
    pass

def test_calc_gross_pay_exactly_40hrs():
    # TODO: David Koh: exactly 40hrs, no OT, not senior → 40*20 = 800.00
    pass


# -------------------------------------------------------
# Tests for get_employees_by_department() [REQ-01]
# -------------------------------------------------------
def test_get_employees_by_department_engineering():
    # TODO: "Engineering" → 3 employees (Alice, Carol, Faris)
    pass

def test_get_employees_by_department_case_insensitive():
    # TODO: "engineering" → same 3 employees
    pass

def test_get_employees_by_department_not_found():
    # TODO: "Finance" → []
    pass

def test_get_employees_by_department_empty_list():
    # TODO: empty list → []
    pass


# -------------------------------------------------------
# Tests for get_highest_paid_employee() [REQ-02]
# -------------------------------------------------------
def test_get_highest_paid_employee():
    # TODO: Carol Ng has highest gross pay
    # Carol: 40*30 + 10*(30*1.5) = 1200+450=1650, *1.10 = 1815.00
    pass

def test_get_highest_paid_employee_empty():
    # TODO: empty list → None
    pass

def test_get_highest_paid_employee_single():
    # TODO: single employee list → that employee returned
    pass


# -------------------------------------------------------
# Tests for calc_total_payroll() [REQ-03]
# -------------------------------------------------------
def test_calc_total_payroll():
    # TODO: sum of all gross pays from SAMPLE_EMPLOYEES
    # Compute each manually and verify the total
    pass

def test_calc_total_payroll_empty():
    # TODO: empty list → 0
    pass


# -------------------------------------------------------
# Tests for calc_avg_pay_by_department() [REQ-04]
# -------------------------------------------------------
def test_calc_avg_pay_by_department_keys():
    # TODO: returned dict must contain exactly Engineering, Marketing, HR
    pass

def test_calc_avg_pay_by_department_engineering():
    # TODO: verify average gross pay for Engineering dept
    pass

def test_calc_avg_pay_by_department_empty():
    # TODO: empty list → {}
    pass
