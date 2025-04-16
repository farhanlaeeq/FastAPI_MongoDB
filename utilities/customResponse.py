from pydantic import BaseModel

class CustomGetResponse(BaseModel):
    status: bool
    status_code: int
    message: str
    data: list

    class Config:
        schema_extra = {
            "example": {
                "status": True,
                "status_code": 200,
                "message": "Success",
                "data": []
            }
        }

def custom_Get_response(status: bool, status_code: int, message: str, data: list):
    return CustomGetResponse(status=status, status_code=status_code, message=message, data=data)


class CustomPostResponse(BaseModel):
    status: bool
    status_code: int
    message: str
    data: object | None

    class Config:
        schema_extra = {
            "example": {
                "status": True,
                "status_code": 200,
                "message": "Success",
                "data": {}
            }
        }

def custom_Post_response(status: bool, status_code: int, message: str, data: object | None):
    return CustomPostResponse(status=status, status_code=status_code, message=message, data=data)