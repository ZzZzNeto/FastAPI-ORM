from repository.sqlalchemy.members import MembersRepository
from cqrs.commands import MembersCommand
from cqrs.handlers import ICommandHandler

class UpdateMemberCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: MembersRepository = MembersRepository()
    
    async def handle(self, command: MembersCommand, id : int) -> bool:
        result = await self.repo.update_members(details=command.details, id=id)
        return result