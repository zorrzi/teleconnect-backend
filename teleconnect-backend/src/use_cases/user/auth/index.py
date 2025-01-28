from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from entities.user import User
from repositories.user_repository import create_user, get_user_by_email
from utils.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: User):
    created_user = create_user(user)
    return created_user

# Modelo para login
class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    user = get_user_by_email(request.email)
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=400, detail="Email ou senha incorretos")
    
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
