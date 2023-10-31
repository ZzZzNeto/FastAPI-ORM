from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Profile_Trainers
from typing import Dict, Any
from sqlalchemy import desc

class TrainerRepository:

    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_trainers(self, profile_trainers: Profile_Trainers) -> bool:
        try:
            self.sess.add(profile_trainers)
            self.sess.commit()
            print(profile_trainers.id)
        except:
            return False
        return True

    def update_trainers(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Profile_Trainers).filter(Profile_Trainers.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    def delete_trainers(self, id: int) -> bool:
        try:
            trainer = self.sess.query(Profile_Trainers).filter(Profile_Trainers.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_trainers(self):
        return self.sess.query(Profile_Trainers).all()

    def get_all_trainers_where(self, firstname: str):
        return self.sess.query(Profile_Trainers).filter(Profile_Trainers.firstname == firstname).all()

    def get_all_trainers_sorted_desc(self):
        return self.sess.query(Profile_Trainers).order_by(desc(Profile_Trainers.firstname)).all()

    def get_trainers(self, id: int):
        return self.sess.query(Profile_Trainers).filter(Profile_Trainers.id == id).one_or_none()
