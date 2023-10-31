from repository.sqlalchemy.login import LoginRepository
from cqrs.handlers import ICommandHandler

class DeleteLoginCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: LoginRepository = LoginRepository()
    
    async def handle(self, id : int) -> bool:
        result = await self.repo.delete_login(id)
        return result