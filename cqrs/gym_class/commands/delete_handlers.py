from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.handlers import ICommandHandler

class DeleteGymClassCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: GymClassRepository = GymClassRepository()
    
    async def handle(self, id : int) -> bool:
        result = await self.repo.delete_gym_classes(id)
        return result