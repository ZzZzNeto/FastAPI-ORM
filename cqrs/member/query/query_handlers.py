from repository.sqlalchemy.members import MembersRepository
from cqrs.queries import SignupListQuery
from cqrs.handlers import IQueryHandler

class ListMemberQueryHandler(IQueryHandler):
    def __init__(self):
        self.repo: MembersRepository = MembersRepository()
        self.query: SignupListQuery = SignupListQuery()
    
    async def handle(self) -> SignupListQuery:
        data = await self.repo.get_all_members()
        self.query.records = data
        return self.query
    
    async def handle_unique(self, id) -> SignupListQuery:
        data = await self.repo.get_members(id=id)
        self.query.records = data
        return self.query
    
    async def handle_where(self, firstname) -> SignupListQuery:
        data = await self.repo.get_all_members_where(firstname=firstname)
        self.query.records = data
        return self.query
    
    async def handle_desc(self) -> SignupListQuery:
        data = await self.repo.get_all_members_sorted_desc()
        self.query.records = data
        return self.query