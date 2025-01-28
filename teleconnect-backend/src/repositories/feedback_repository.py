from typing import List
from mongoengine import *
from entities.feedback import Feedback
from models.feedback_model import FeedbackModel

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

    def list_all_feedbacks(self) -> List[dict]:
        feedbacks = FeedbackModel.objects()
        return [
            {
                **feedback.to_mongo().to_dict(),
                "_id": str(feedback.id)
            }
            for feedback in feedbacks
        ]

    def delete_feedback(self, feedback_id: str) -> None:
        feedback = FeedbackModel.objects(id=feedback_id).first()
        if not feedback:
            raise ValueError("Feedback não encontrado para exclusão.")
        feedback.delete()
