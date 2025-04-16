from pydantic import BaseModel

class DepartmentMaster (BaseModel):
    departmentCode: str
    departmentName: str
    departmentShortName: str
    isActive: bool