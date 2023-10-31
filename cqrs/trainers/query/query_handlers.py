from repository.sqlalchemy.trainers import TrainerRepository
from cqrs.queries import ProfileTrainerListQuery
from cqrs.handlers import IQueryHandler

class ListTrainerQueryHandler(IQueryHandler):
    def __init__(self):
        self.repo: TrainerRepository = TrainerRepository()
        self.query: ProfileTrainerListQuery = ProfileTrainerListQuery()
    
    async def handle(self) -> ProfileTrainerListQuery:
        data = await self.repo.get_all_trainers()
        self.query.records = data
        return self.query
    
    async def handle_unique(self, id) -> ProfileTrainerListQuery:
        data = await self.repo.get_trainers(id=id)
        self.query.records = data
        return self.query
    
    async def handle_where(self, firstname) -> ProfileTrainerListQuery:
        data = await self.repo.get_all_trainers_where(firstname=firstname)
        self.query.records = data
        return self.query
    
    async def handle_desc(self) -> ProfileTrainerListQuery:
        data = await self.repo.get_all_trainers_sorted_desc()
        self.query.records = data
        return self.query