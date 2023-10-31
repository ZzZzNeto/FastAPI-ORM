from repository.sqlalchemy.login import LoginRepository
from cqrs.queries import LoginListQuery
from cqrs.handlers import IQueryHandler

class ListLoginQueryHandler(IQueryHandler):
    def __init__(self):
        self.repo: LoginRepository = LoginRepository()
        self.query: LoginListQuery = LoginListQuery()
    
    async def handle(self) -> LoginListQuery:
        data = await self.repo.get_all_login()
        self.query.records = data
        return self.query
    
    async def handle_unique(self, id) -> LoginListQuery:
        data = await self.repo.get_login(id=id)
        self.query.records = data
        return self.query
    
    async def handle_where(self, firstname) -> LoginListQuery:
        data = await self.repo.get_all_login(firstname=firstname)
        self.query.records = data
        return self.query