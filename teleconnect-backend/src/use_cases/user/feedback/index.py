# use_cases/user/feedback/index.py
from fastapi import APIRouter
from use_cases.user.feedback.create_feedback import router as create_feedback_router
from use_cases.user.feedback.get_feedback import router as get_feedbacks_router

router = APIRouter()
router.include_router(create_feedback_router, tags=["Feedback"])
router.include_router(get_feedbacks_router, tags=["User Feedback"])
