from repository.sqlalchemy.signup import SignupRepository
from cqrs.queries import SignupListQuery
from cqrs.handlers import IQueryHandler

class ListSignupQueryHandler(IQueryHandler):
    def __init__(self):
        self.repo: SignupRepository = SignupRepository()
        self.query: SignupListQuery = SignupListQuery()
    
    async def handle(self) -> SignupListQuery:
        data = await self.repo.get_all_signup()
        self.query.records = data
        return self.query
    
    async def handle_unique(self, id) -> SignupListQuery:
        data = await self.repo.get_signup(id=id)
        self.query.records = data
        return self.query
    
    async def handle_where(self, username) -> SignupListQuery:
        data = await self.repo.get_all_signup_where(username=username)
        self.query.records = data
        return self.query
    
    async def handle_desc(self) -> SignupListQuery:
        data = await self.repo.get_all_signup_sorted_desc()
        self.query.records = data
        return self.query