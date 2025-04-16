def RoleEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "roleName": item["roleName"],
        "isActive": item["isActive"],
    }
    
def RoleListEntity(items) -> list:
    return [RoleEntity(item) for item in items]