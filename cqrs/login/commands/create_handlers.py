from repository.sqlalchemy.login import LoginRepository
from cqrs.commands import LoginCommand
from cqrs.handlers import ICommandHandler

class AddLoginCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: LoginRepository = LoginRepository()
    
    async def handle(self, command: LoginCommand) -> bool:
        result = await self.repo.insert_login(command.details)
        return result