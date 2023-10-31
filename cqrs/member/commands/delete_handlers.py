from repository.sqlalchemy.members import MembersRepository
from cqrs.handlers import ICommandHandler

class DeleteMemberCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: MembersRepository = MembersRepository()
    
    async def handle(self, id : int) -> bool:
        result = await self.repo.delete_members(id)
        return result