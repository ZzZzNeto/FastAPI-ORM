from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Profile_Members
from typing import Dict, Any
from sqlalchemy import desc

class MembersRepository:

    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_members(self, profile_members: Profile_Members) -> bool:
        try:
            self.sess.add(profile_members)
            self.sess.commit()
            print(profile_members.id)
        except:
            return False
        return True

    def update_members(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Profile_Members).filter(Profile_Members.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    def delete_members(self, id: int) -> bool:
        try:
            trainer = self.sess.query(Profile_Members).filter(Profile_Members.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_members(self):
        return self.sess.query(Profile_Members).all()

    def get_all_members_where(self, firstname: str):
        return self.sess.query(Profile_Members).filter(Profile_Members.firstname == firstname).all()

    def get_all_members_sorted_desc(self):
        return self.sess.query(Profile_Members).order_by(desc(Profile_Members.firstname)).all()

    def get_members(self, id: int):
        return self.sess.query(Profile_Members).filter(Profile_Members.id == id).one_or_none()
