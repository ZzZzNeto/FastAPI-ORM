from repository.sqlalchemy.signup import SignupRepository
from cqrs.commands import SignupCommand
from cqrs.handlers import ICommandHandler

class AddSignupCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: SignupRepository = SignupRepository()
    
    async def handle(self, command: SignupCommand) -> bool:
        result = await self.repo.insert_signup(command.details)
        return result