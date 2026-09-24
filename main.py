from fastapi import FastAPI
from datetime import date
emp = FastAPI()

employees = []

@emp.post("/employee")
def add_employee(employee_id: int, name: str, dob: date, salary: float):
    employee = {
        "employee_id": employee_id,
        "employee_name": name,
        "employee_dob": dob,
        "employee_salary": salary
    }

    employees.append(employee)

    return {
        "message": "Employee added successfully!",
        "employee": employee
    }

@emp.get("/employee/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee

    return {"message": "Employee not found!"}

@emp.get("/employee")
def get_all_employee():
    return employees

@emp.put("/employee/{employee_id}")
def update_employee(
    employee_id: int,
    name: str,
    dob: date,
    salary: float
):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            employee["employee_name"] = name
            employee["employee_dob"] = dob
            employee["employee_salary"] = salary

            return {
                "message": "Employee updated successfully!",
                "employee": employee
            }

    return {"message": "Employee not found!"}

@emp.delete("/employee/{employee_id}")
def delete_employee(employee_id: int):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            employees.remove(employee)

            return {
                "message": "Employee deleted successfully!"
            }

    return {"message": "Employee not found!"}