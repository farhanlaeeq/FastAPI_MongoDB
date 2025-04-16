from fastapi import APIRouter, Request
from database import get_database

from models.EmployeeMaster import EmployeeMaster
from schemas.EmployeeMaster import EmployeeEntity, EmployeeListEntity
from utilities.customResponse import custom_Get_response, custom_Post_response

employeeMaster = APIRouter(prefix="/employee", tags=["Employee"])

@employeeMaster.get("/get-employees")
async def get_employees(request: Request):
    db = get_database(2)
    docs = db.EmployeeMaster.aggregate([
        # stage 1: only fetch active employees
        {
            "$match": {"isActive": True}
        },
        {
            "$addFields": 
            {
                "roleIDObj": {"$toObjectId": "$roleID"}
            }
        },
        {
            "$lookup":
            {
                "from": "DepartmentMaster",
                "localField": "departmentCode",
                "foreignField": "departmentCode",
                "as": "departmentDetails"
            }
        },
        {
            "$lookup":
            {
                "from": "RoleMaster",
                "localField": "roleIDObj",
                "foreignField": "_id",
                "as": "roleDetails"
            }
        },
        {
            "$addFields": 
            {
                "departmentName": {"$arrayElemAt": ["$departmentDetails.departmentName", 0]},
                "roleName": {"$arrayElemAt": ["$roleDetails.roleName", 0]}
            }
        },
        {
            "$project": 
            {
                "_id": 1,
                "firstName": 1,
                "lastName": 1,
                "dob": 1,
                "departmentCode": 1,
                "departmentName": 1,
                "roleID": 1,
                "roleName": 1,
                "designationCode": 1,
                "address": 1,
            }
        }
    ])
    employees = EmployeeListEntity(docs)
    
    return custom_Get_response(True, 200, "Data Retrieved Successfully.", employees)


@employeeMaster.post("/insert-employee")
async def insert_employee(employee: EmployeeMaster):
    db = get_database(2)
    new_employee = db.EmployeeMaster.insert_one(dict(employee))
    
    inserted_employee = db.EmployeeMaster.find_one({"_id": new_employee.inserted_id})
    new_inserted_employee = EmployeeEntity(inserted_employee)
    
    return custom_Post_response(True, 200, "New Employee added Successfully.", new_inserted_employee)
