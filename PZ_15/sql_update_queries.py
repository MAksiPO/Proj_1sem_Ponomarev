from sql_types import SQLUpdateQuery, SQLUpdateQuerySequence, SQLAbstractQuery

_upd1: SQLUpdateQuery = SQLUpdateQuery(SQLAbstractQuery("""
UPDATE faculties SET name='Новый факультет' WHERE id=1
"""))
_upd2: SQLUpdateQuery = SQLUpdateQuery(SQLAbstractQuery("""
UPDATE departments SET title='Новая кафедра' WHERE id=2
"""))
_upd3: SQLUpdateQuery = SQLUpdateQuery(SQLAbstractQuery("""
UPDATE specialties SET title='Новая специальность' WHERE id=3
"""))
_upd4: SQLUpdateQuery = SQLUpdateQuery(SQLAbstractQuery("""
UPDATE subject SET title='Новый предмет' WHERE id=4
"""))
_upd5: SQLUpdateQuery = SQLUpdateQuery(SQLAbstractQuery("""
UPDATE subject_pass_form SET title='Новая форма сдачи' WHERE id=5
"""))
_upd6: SQLUpdateQuery = SQLUpdateQuery(SQLAbstractQuery("""
UPDATE сurriculum SET lecture_hours=30 WHERE id=6
"""))
_upd7: SQLUpdateQuery = SQLUpdateQuery(SQLAbstractQuery("""
UPDATE сurriculum SET lecture_hours=78 WHERE lecture_hours > 30
"""))
_upd8: SQLUpdateQuery = SQLUpdateQuery(SQLAbstractQuery("""
UPDATE applicants SET first_name='Милана', last_name='Хаметова' WHERE id = 7
"""))
_upd9: SQLUpdateQuery = SQLUpdateQuery(SQLAbstractQuery("""
UPDATE departments SET title='Кафедра теории Каламбета' WHERE id=1
"""))
_upd10: SQLUpdateQuery = SQLUpdateQuery(SQLAbstractQuery("""
UPDATE specialties SET title='Физика, информатика и Каламбет' WHERE id=2
"""))
update_sequence: SQLUpdateQuerySequence = [_upd1, _upd2, _upd3, _upd4, _upd5, _upd6, _upd7, _upd8, _upd9, _upd10]
