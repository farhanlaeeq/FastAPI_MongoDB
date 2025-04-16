from pydantic import BaseModel

class RoleMaster (BaseModel):
    roleName: str
    isActive: bool