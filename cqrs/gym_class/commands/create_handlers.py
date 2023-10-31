from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.commands import GymClassCommand
from cqrs.handlers import ICommandHandler

class AddGymClassCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: GymClassRepository = GymClassRepository()
    
    async def handle(self, command: GymClassCommand) -> bool:
        result = await self.repo.insert_gym_classes(command.details)
        return result