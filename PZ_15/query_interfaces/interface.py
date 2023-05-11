from abc import abstractmethod
from sqlite3 import Cursor
from PZ_15.sql_types import SQLAbstractQuery


class QueryInterface:
    def __init__(self, cursor: Cursor):
        self.cursor = cursor

    @abstractmethod
    def execute_query(self, sql: SQLAbstractQuery) -> None:
        raise NotImplementedError
