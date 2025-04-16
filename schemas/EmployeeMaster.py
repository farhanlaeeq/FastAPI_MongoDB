def EmployeeEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "firstName": item["firstName"],
        "lastName": item["lastName"],
        "dob": item["dob"],
        "departmentCode": item["departmentCode"],
        "designationCode": item["designationCode"],
        "address": item["address"],
        "isActive": item["isActive"],
    }
    
def EmployeeListEntity(items) -> list:
    return [EmployeeEntity(item) for item in items]