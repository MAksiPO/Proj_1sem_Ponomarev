import time
from sqlite3 import Cursor
from sql_instance import SQL
from insert_data import sql_queries
from queries import UpdateQuery
from queries import SelectQuery
from sql_update_queries import update_sequence
from sql_select_queries import select_sequence
SQL_PATH = 'pz.sqlite3'


def _get_sql_instance(sql_path: str) -> SQL:
    return SQL(sql_path)


def _get_update_query_instance(cursor: Cursor) -> UpdateQuery:
    return UpdateQuery(cursor)


def _get_select_query_instance(cursor: Cursor) -> SelectQuery:
    return SelectQuery(cursor)


def initial_create_table() -> None:
    sql = _get_sql_instance(SQL_PATH)
    sql.create_tables()


def insert_data() -> None:
    cursor = _get_sql_instance(SQL_PATH).get_cursor()

    for query in sql_queries:
        cursor.executescript(query)


def main() -> None:
    upd = _get_update_query_instance(cursor=_get_sql_instance(SQL_PATH).get_cursor())
    select = _get_select_query_instance(cursor=_get_sql_instance(SQL_PATH).get_cursor())

    for update_query in update_sequence:
        upd.execute_query(update_query)

    time.sleep(5)

    for select_query in select_sequence:
        select.execute_query(select_query)

if __name__ == "__main__":
    # initial_create_table()
    # insert_data()
    main()
