from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.commands import GymClassCommand
from cqrs.handlers import ICommandHandler

class UpdateGymClassCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: GymClassRepository = GymClassRepository()
    
    async def handle(self, command: GymClassCommand, id : int) -> bool:
        result = await self.repo.update_gym_classes(details=command.details, id=id)
        return result