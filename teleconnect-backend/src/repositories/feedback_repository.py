from typing import List
from mongoengine import *
from entities.feedback import Feedback
from models.feedback_model import FeedbackModel
from models.user_model import UserModel  # Para buscar o nome do usuário

class FeedbackRepository:
    def save(self, feedback: Feedback) -> None:
        feedback_model = FeedbackModel()
        feedback_dict = feedback.model_dump()

        for k in FeedbackModel.get_normal_fields():
            if k not in feedback_dict:
                continue
            feedback_model[k] = feedback_dict[k]

        feedback_model.save()


    def get_feedback_by_id(self, feedback_id: str) -> dict:
        feedback = FeedbackModel.objects(id=feedback_id).first()
        if not feedback:
            return None
        feedback_dict = feedback.to_mongo().to_dict()
        feedback_dict["_id"] = str(feedback_dict["_id"])
        return feedback_dict

    def create_feedback(self, user_id: str, feedback_text: str, stars: int) -> str:
        feedback = FeedbackModel(user_id=user_id, feedback_text=feedback_text, stars=stars)
        feedback.save()
        return str(feedback.id)

    def get_feedbacks(self) -> List[dict]:
        try:
            feedbacks = FeedbackModel.objects()
            feedbacks_list = [
                {
                    "_id": str(feedback.id),
                    "feedback_text": feedback.feedback_text,
                    "stars": feedback.stars
                }
                for feedback in feedbacks
            ]
            return feedbacks_list
        except Exception as e:
            raise Exception(f"Erro ao buscar feedbacks: {str(e)}")