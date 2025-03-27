from database.repositories.base import BaseRepository
from models.rooms import Room

class RoomsRepository(BaseRepository):
    def get_rooms_by_capacity(self, min_capacity):
        query = """
            SELECT r.ID, r.ROOM_NAME, r.CAPACITY
            FROM Schedule.ROOMS r
            WHERE r.CAPACITY >= %s
        """
        result = self.fetch_all(query, (min_capacity,))
        rooms = [Room(*row) for row in result]
        return rooms
