from repository.sqlalchemy.signup import SignupRepository
from cqrs.handlers import ICommandHandler

class DeleteSignupCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: SignupRepository = SignupRepository()
    
    async def handle(self, id : int) -> bool:
        result = await self.repo.delete_signup(id)
        return result