from repository.sqlalchemy.trainers import TrainerRepository
from cqrs.handlers import ICommandHandler

class DeleteTrainerCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: TrainerRepository = TrainerRepository()
    
    async def handle(self, id : int) -> bool:
        result = await self.repo.delete_trainers(id)
        return result