from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Gym_Class
from typing import Dict, Any
from sqlalchemy import desc

class GymClassRepository:

    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_gym_classes(self, gym_class: Gym_Class) -> bool:
        try:
            self.sess.add(gym_class)
            self.sess.commit()
            print(gym_class.id)
        except:
            return False
        return True

    def update_gym_classes(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Gym_Class).filter(Gym_Class.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    def delete_gym_classes(self, id: int) -> bool:
        try:
            trainer = self.sess.query(Gym_Class).filter(Gym_Class.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_gym_classes(self):
        return self.sess.query(Gym_Class).all()

    def get_all_gym_classes_where(self, name: str):
        return self.sess.query(Gym_Class).filter(Gym_Class.name == name).all()

    def get_all_gym_classes_sorted_desc(self):
        return self.sess.query(Gym_Class).order_by(desc(Gym_Class.name)).all()

    def get_gym_classes(self, id: int):
        return self.sess.query(Gym_Class).filter(Gym_Class.id == id).one_or_none()
