from fastapi import APIRouter, Response
from use_cases.user.create_feedback.create_feedback_use_case import CreateFeedbackUseCase
from use_cases.user.create_feedback.create_feedback_dto import CreateFeedbackDTO
from repositories.feedback_repository import FeedbackRepository

router = APIRouter()

# Inicializa o repositório e o caso de uso
create_feedback_use_case = CreateFeedbackUseCase(FeedbackRepository())

@router.post("/user/create-feedback")
def create_feedback(create_feedback_dto: CreateFeedbackDTO, response: Response):
    return create_feedback_use_case.execute(create_feedback_dto, response)
