def pay_employee(employee, hours):
    if hours ==0: raise EmployeeDidntWorked
    if hours < 0: raise EmployeeWorkedNegatively
    if hours > 744: raise EmployeeWorkedTooMuch
    if abs(employee.pay) != employee.pay: raise PayIsNegative
    if employee.pay > 100: raise PayIsTooBig     
    salary = hours * employee.pay
    employee.receive_salary(salary)
class EmployeeDidntWorked(Exception):
    pass
class EmployeeWorkedNegatively(Exception):
    pass
class EmployeeWorkedTooMuch(Exception):
    pass
class PayIsNegative(Exception):
    pass
class PayIsTooBig(Exception):
    pass
