from fastapi import APIRouter, Request
from database import get_database

from models.RoleMaster import RoleMaster
from schemas.RoleMaster import RoleEntity, RoleListEntity
from utilities.customResponse import custom_Get_response, custom_Post_response

roleMaster = APIRouter(prefix="/role", tags=["Role"])

@roleMaster.get("/get-roles")
async def get_roles(request: Request):
    db = get_database(2)
    docs = db.RoleMaster.find()
    roles = RoleListEntity(docs)
    
    return custom_Get_response(True, 200, "Data Retrieved Successfully.", roles)


@roleMaster.post("/insert-role")
async def insert_role(role: RoleMaster):
    db = get_database(2)
    new_role = db.RoleMaster.insert_one(dict(role))
    
    inserted_role = db.RoleMaster.find_one({"_id": new_role.inserted_id})
    new_inserted_role = RoleEntity(inserted_role)
    
    return custom_Post_response(True, 200, "New Role added Successfully.", new_inserted_role)
