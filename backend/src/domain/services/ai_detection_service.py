from uuid import UUID

from domain.models.ai_detection import AIDetectionTask
from domain.models.balance import BalanceTransaction, BalanceTransactionType
from domain.repositories.ai_detection_task_repository import AIDetectionTaskRepository
from domain.repositories.balance_repository import BalanceRepository
from domain.repositories.user_repository import UserRepository
from domain.repositories.ai_detection_model_repository import AIDetectionModelRepository


class AIDetectionService:
    def __init__(
        self,
        task_repository: AIDetectionTaskRepository,
        user_repository: UserRepository,
        balance_repository: BalanceRepository,
        model_repository: AIDetectionModelRepository,
        prediction_cost: int = 1,
    ) -> None:
        self._task_repository = task_repository
        self._user_repository = user_repository
        self._balance_repository = balance_repository
        self._model_repository = model_repository

    def create_prediction(
        self, user_id: UUID, image_hash: str, image_url: str
    ) -> AIDetectionTask:
        try:
            user = self._user_repository.get_by_id(user_id)
            if user is None:
                raise ValueError(f"Пользователь с id {user_id} не найден")

            prediction_cost = self._model_repository.prediction_cost
            if not user.can_withdraw(prediction_cost):
                raise ValueError("Недостаточно средств")

            user.withdraw(prediction_cost)
            if not self._user_repository.update(user):
                raise ValueError("Не удалось списать средства с баланса")

            withdrawal_transaction = BalanceTransaction(
                user_id=user_id,
                type=BalanceTransactionType.WITHDRAWAL,
                amount=prediction_cost,
            )
            if not self._balance_repository.update_user_balance(withdrawal_transaction):
                raise ValueError("Не удалось сохранить транзакцию")

            task = AIDetectionTask(
                user_id=user_id, image_hash=image_hash, image_url=image_url
            )
            task = self._task_repository.create(task)

            result = self._model_repository.predict(image_url)
            task.complete_prediction(result)
            self._task_repository.update(task)

            return task
        except Exception as error:
            # Здесь будет логика по откату
            raise ValueError(f"Отмена операции: {str(error)}")
