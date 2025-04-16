from fastapi import APIRouter
from api.routes.EmployeeMaster import employeeMaster
from api.routes.DepartmentMaster import departmentMaster
from api.routes.RoleMaster import roleMaster

api_router = APIRouter()
api_router.include_router(employeeMaster)
api_router.include_router(departmentMaster)
api_router.include_router(roleMaster)