from repositories.feedback_repository import FeedbackRepository
from entities.feedback import Feedback
from use_cases.user.create_feedback.create_feedback_dto import CreateFeedbackDTO
from fastapi import Response

class CreateFeedbackUseCase:
    def __init__(self, feedback_repository: FeedbackRepository):
        self.feedback_repository = feedback_repository

    def execute(self, create_feedback_dto: CreateFeedbackDTO, response: Response):
        try:
            feedback = Feedback(
                _id="",
                user_name=create_feedback_dto.user_name,
                message=create_feedback_dto.message,
                stars=create_feedback_dto.stars
            )

            self.feedback_repository.save(feedback)
            response.status_code = 201
            return {"status": "success", "message": "Feedback criado com sucesso."}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": f"Erro ao salvar o feedback: {str(e)}"}
