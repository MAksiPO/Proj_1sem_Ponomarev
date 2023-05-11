from PZ_15.query_interfaces import QueryInterface
from sqlite3 import Cursor
from PZ_15.sql_types import SQLUpdateQuery


class UpdateQuery(QueryInterface):
    def __init__(self, cursor: Cursor):
        super(UpdateQuery, self).__init__(cursor)

    def execute_query(self, sql: SQLUpdateQuery) -> None:
        self.cursor.executescript(sql)
        print('успешно обновил')

