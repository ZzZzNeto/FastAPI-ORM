from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.queries import GymClassListQuery
from cqrs.handlers import IQueryHandler

class ListGymClassQueryHandler(IQueryHandler):
    def __init__(self):
        self.repo: GymClassRepository = GymClassRepository()
        self.query: GymClassListQuery = GymClassListQuery()
    
    async def handle(self) -> GymClassListQuery:
        data = await self.repo.get_all_gym_classes()
        self.query.records = data
        return self.query
    
    async def handle_unique(self, id) -> GymClassListQuery:
        data = await self.repo.get_gym_classes(id=id)
        self.query.records = data
        return self.query
    
    async def handle_where(self, name) -> GymClassListQuery:
        data = await self.repo.get_all_gym_classes_where(name=name)
        self.query.records = data
        return self.query
    
    async def handle_desc(self) -> GymClassListQuery:
        data = await self.repo.get_all_gym_classes_sorted_desc()
        self.query.records = data
        return self.query