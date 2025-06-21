from fastapi import APIRouter
from app.db import db
from bson import ObjectId

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/users")
def get_users():
    users = list(db.users.find({}, {"_id": 0}))
    return {"users": users}

@router.post("/users")
def create_user(user: dict):
    result = db.users.insert_one(user)
    # Busca o usuário criado
    created_user = db.users.find_one({"_id": result.inserted_id})
    # Converte _id para string para não dar erro no JSON
    created_user["_id"] = str(created_user["_id"])
    return {"message": "User created", "user": created_user}
