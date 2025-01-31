# use_cases/user/feedback/list_feedbacks.py
from fastapi import APIRouter
from repositories.feedback_repository import FeedbackRepository
from .list_feedbacks_use_case import ListFeedbacksUseCase

router = APIRouter()
feedback_repo = FeedbackRepository()
list_use_case = ListFeedbacksUseCase(feedback_repo)

@router.get("/user/feedback")
def list_feedbacks():
    result = list_use_case.execute()
    return result
