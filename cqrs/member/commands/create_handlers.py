from repository.sqlalchemy.members import MembersRepository
from cqrs.commands import MembersCommand
from cqrs.handlers import ICommandHandler

class AddMemberCommandHandler(ICommandHandler):
    def __init__(self):
        self.repo: MembersRepository = MembersRepository()
    
    async def handle(self, command: MembersCommand) -> bool:
        result = await self.repo.insert_members(command.details)
        return result