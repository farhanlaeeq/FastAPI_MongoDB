from pymongo import MongoClient

MONGO_URI="mongodb+srv://farhanali27718:vuixmftX4Axf14FK@fastapi.rmchf.mongodb.net"

client  = MongoClient(MONGO_URI)

DATABASES = {
    1: client.fastapi_demo,
    2: client.ERP_Database
}

def get_database(index: int):
    db = DATABASES.get(index)
    if db is None:
        raise ValueError(f"No database configured for index {index}")
    return db