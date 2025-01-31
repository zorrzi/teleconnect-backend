from fastapi import APIRouter, HTTPException
from repositories.feedback_repository import FeedbackRepository

router = APIRouter()
feedback_repository = FeedbackRepository()

@router.get("/user/feedback")
def get_feedbacks():
    """
    Retorna todos os feedbacks registrados.
    """
    try:
        feedbacks = feedback_repository.get_feedbacks()
        return {"status": "success", "feedbacks": feedbacks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter feedbacks: {str(e)}")
