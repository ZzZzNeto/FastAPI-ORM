from repository.sqlalchemy.login import LoginRepository
from cqrs.commands import LoginCommand
from cqrs.handlers import ICommandHandler

class UpdateLoginCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: LoginRepository = LoginRepository()
    
    async def handle(self, command: LoginCommand, id : int) -> bool:
        result = await self.repo.update_login(details=command.details, id=id)
        return result