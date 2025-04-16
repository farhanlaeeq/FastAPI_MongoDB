def DepartmentEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "departmentCode": item["departmentCode"],
        "departmentName": item["departmentName"],
        "departmentShortName": item["departmentShortName"],
        "isActive": item["isActive"],
    }
    
def DepartmentListEntity(items) -> list:
    return [DepartmentEntity(item) for item in items]