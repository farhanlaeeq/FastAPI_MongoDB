from pydantic import BaseModel

class EmployeeMaster (BaseModel):
    firstName: str
    lastName: str
    dob: str
    departmentCode: str
    designationCode: str
    roleID: str
    address: str
    isActive: bool