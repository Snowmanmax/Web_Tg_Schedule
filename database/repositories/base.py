from sqlalchemy.orm import Session
from typing import List, TypeVar, Type

T = TypeVar('T', bound='Base')

class BaseRepository:
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def get_all(self) -> List[T]:
        return self.session.query(self.model).all()

    def get_by_id(self, id) -> T:
        return self.session.query(self.model).filter(self.model.id == id).first()

    def add(self, entity: T) -> None:
        self.session.add(entity)
        self.session.commit()

    def remove(self, entity: T) -> None:
        self.session.delete(entity)
        self.session.commit()