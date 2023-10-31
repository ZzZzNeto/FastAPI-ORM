from repository.sqlalchemy.signup import SignupRepository
from cqrs.commands import SignupCommand
from cqrs.handlers import ICommandHandler

class UpdateSignupCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: SignupRepository = SignupRepository()
    
    async def handle(self, command: SignupCommand, id : int) -> bool:
        result = await self.repo.update_signup(details=command.details, id=id)
        return result