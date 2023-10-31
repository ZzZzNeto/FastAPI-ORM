from repository.sqlalchemy.trainers import TrainerRepository
from cqrs.commands import ProfileTrainerCommand
from cqrs.handlers import ICommandHandler

class AddTrainerCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: TrainerRepository = TrainerRepository()
    
    async def handle(self, command: ProfileTrainerCommand) -> bool:
        result = await self.repo.insert_trainers(command.details)
        return result