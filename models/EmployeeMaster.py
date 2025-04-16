from pydantic import BaseModel

class EmployeeMaster (BaseModel):
    firstName: str
    lastName: str
    dob: str
    departmentCode: str
    designationCode: str
    address: str
    isActive: bool