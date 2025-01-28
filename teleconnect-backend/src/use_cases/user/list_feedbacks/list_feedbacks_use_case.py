from repositories.feedback_repository import FeedbackRepository

class ListFeedbacksUseCase:
    def __init__(self, feedback_repository: FeedbackRepository):
        self.feedback_repository = feedback_repository

    def execute(self):
        try:
            feedbacks = self.feedback_repository.list_all_feedbacks()
            return {"status": "success", "feedbacks": feedbacks}
        except Exception as e:
            return {"status": "error", "message": f"Erro ao listar feedbacks: {str(e)}"}
