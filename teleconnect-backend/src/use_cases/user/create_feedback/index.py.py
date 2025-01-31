# use_cases/user/feedback/create_feedback.py

import os
import jwt
from fastapi import APIRouter, Request, Response
from pydantic import BaseModel
from repositories.feedback_repository import FeedbackRepository
from repositories.user_repository import UserRepository

router = APIRouter()
feedback_repository = FeedbackRepository()
user_repository = UserRepository()

class CreateFeedbackRequest(BaseModel):
    feedback_text: str
    stars: int

@router.post("/user/feedback")
def create_feedback(
    data: CreateFeedbackRequest,
    request: Request,
    response: Response,
):
    """
    Cria um feedback para o usuário logado. Verifica o token no cookie.
    """
    # Obtém o token do cookie
    token_cookie = request.cookies.get("user_auth_token")
    if not token_cookie:
        response.status_code = 401
        return {"status": "error", "message": "Token ausente ou usuário não autenticado"}

    try:
        token_str = token_cookie.replace("Bearer ", "")
        payload = jwt.decode(token_str, os.getenv("USER_JWT_SECRET"), algorithms=["HS256"])
        user_id = payload.get("id") or payload.get("sub")
    except (jwt.DecodeError, IndexError, AttributeError):
        response.status_code = 401
        return {"status": "error", "message": "Token inválido ou corrompido"}

    if not user_id:
        response.status_code = 401
        return {"status": "error", "message": "ID do usuário não encontrado no token"}

    # Verifica se o usuário existe
    user = user_repository.find_by_id(user_id)
    if not user:
        response.status_code = 404
        return {"status": "error", "message": "Usuário não encontrado"}

    # Cria o feedback
    feedback_id = feedback_repository.create_feedback(user_id, data.feedback_text, data.stars)
    if not feedback_id:
        response.status_code = 500
        return {"status": "error", "message": "Erro ao criar feedback"}

    return {"status": "success", "message": "Feedback criado com sucesso", "feedback_id": str(feedback_id)}
