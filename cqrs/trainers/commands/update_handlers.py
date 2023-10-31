from repository.sqlalchemy.trainers import TrainerRepository
from cqrs.commands import ProfileTrainerCommand
from cqrs.handlers import ICommandHandler

class UpdateTrainerCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: TrainerRepository = TrainerRepository()
    
    async def handle(self, command: ProfileTrainerCommand, id : int) -> bool:
        result = await self.repo.update_trainers(details=command.details, id=id)
        return result