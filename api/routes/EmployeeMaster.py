from fastapi import APIRouter, Request
from database import get_database

from models.EmployeeMaster import EmployeeMaster
from schemas.EmployeeMaster import EmployeeEntity, EmployeeListEntity
from utilities.customResponse import custom_Get_response, custom_Post_response

employeeMaster = APIRouter(prefix="/employee", tags=["Employee"])

@employeeMaster.get("/get-employees")
async def get_employees(request: Request):
    db = get_database(2)
    docs = db.EmployeeMaster.find()
    employees = EmployeeListEntity(docs)
    
    return custom_Get_response(True, 200, "Data Retrieved Successfully.", employees)


@employeeMaster.post("/insert-employee")
async def insert_employee(employee: EmployeeMaster):
    db = get_database(2)
    new_employee = db.EmployeeMaster.insert_one(dict(employee))
    
    inserted_employee = db.EmployeeMaster.find_one({"_id": new_employee.inserted_id})
    new_inserted_employee = EmployeeEntity(inserted_employee)
    
    return custom_Post_response(True, 200, "New Employee added Successfully.", new_inserted_employee)
