from fastapi import APIRouter, Request
from database import get_database

from models.DepartmentMaster import DepartmentMaster
from schemas.DepartmentMaster import DepartmentEntity, DepartmentListEntity
from utilities.customResponse import custom_Get_response, custom_Post_response

departmentMaster = APIRouter(prefix="/department", tags=["Department"])

@departmentMaster.get("/get-departments")
async def get_departments(request: Request):
    db = get_database(2)
    docs = db.DepartmentMaster.find()
    departments = DepartmentListEntity(docs)
    
    return custom_Get_response(True, 200, "Data Retrieved Successfully.", departments)


@departmentMaster.post("/insert-department")
async def insert_department(department: DepartmentMaster):
    db = get_database(2)
    new_department = db.DepartmentMaster.insert_one(dict(department))
    
    inserted_department = db.DepartmentMaster.find_one({"_id": new_department.inserted_id})
    new_inserted_department = DepartmentEntity(inserted_department)
    
    return custom_Post_response(True, 200, "New Department added Successfully.", new_inserted_department)
