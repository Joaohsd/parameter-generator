from .database import Database

class ParameterDB(Database):
    def __init__(self, database, collection):
        super().__init__(database, collection)