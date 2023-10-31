from typing import List
from domain.data.sqlalchemy_models import Profile_Trainers, Signup, Profile_Members, Login, Gym_Class

class ProfileTrainerListQuery:
    def __init__(self):
        self._records: List[Profile_Trainers] = list()
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records

class SignupListQuery:
    def __init__(self):
        self._records: List[Signup] = list()
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records

class MembersListQuery:
    def __init__(self):
        self._records: List[Profile_Members] = list()
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records

class LoginListQuery:
    def __init__(self):
        self._records: List[Login] = list()
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records

class GymClassListQuery:
    def __init__(self):
        self._records: List[Gym_Class] = list()
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records