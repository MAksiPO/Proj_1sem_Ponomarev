from sql_types import SQLSelectQuery, SQLSelectQuerySequence, SQLAbstractQuery

_select1: SQLSelectQuery = SQLSelectQuery(SQLAbstractQuery("""
SELECT first_name, middle_name, last_name, group_title FROM applicants INNER JOIN study_card ON study_card.id_student = applicants.id
"""))
_select2: SQLSelectQuery = SQLSelectQuery(SQLAbstractQuery(f"""
SELECT specialties.title, COUNT(study_card.id_student) FROM specialties INNER JOIN departments ON specialties.department_id = departments.id INNER JOIN faculties ON departments.faculty_id = faculties.id LEFT OUTER JOIN study_card ON study_card.specialization = specialties.id WHERE faculties.name='{input("Введите факультет (например: Факультет прикладной информатики): ")}'
"""))
_select3: SQLSelectQuery = SQLSelectQuery(SQLAbstractQuery(f"""
SELECT departments.title, COUNT(study_card.id_student) FROM departments INNER JOIN faculties ON departments.faculty_id = faculties.id INNER JOIN specialties ON specialties.department_id = departments.id LEFT OUTER JOIN study_card ON study_card.specialization = specialties.id GROUP BY departments.title HAVING faculties.name = '{input("Введите факультет (например: Факультет прикладной информатики): ")}'
"""))
_select4: SQLSelectQuery = SQLSelectQuery(SQLAbstractQuery("""
SELECT subject.title, (сurriculum.lecture_hours + сurriculum.practical_hours + сurriculum.lab_hours) FROM subject INNER JOIN сurriculum ON сurriculum.subject_id = subject.id GROUP BY subject.title
"""))
_select5: SQLSelectQuery = SQLSelectQuery(SQLAbstractQuery("""
SELECT first_name, middle_name, last_name FROM applicants INNER JOIN study_card ON study_card.id_student = applicants.id WHERE grade<4
"""))
_select6: SQLSelectQuery = SQLSelectQuery(SQLAbstractQuery("""
SELECT DISTINCT subject.title FROM subject INNER JOIN study_card ON study_card.subject = subject.id WHERE study_card.group_title = 'Группа 1'
"""))
_select7: SQLSelectQuery = SQLSelectQuery(SQLAbstractQuery("""
SELECT first_name, middle_name, last_name FROM applicants INNER JOIN study_card ON applicants.id = study_card.id_student INNER JOIN subject_pass_form ON study_card.subject_pass_form = subject_pass_form.id WHERE subject_pass_form.title ='Курсовая работа'
"""))
_select8: SQLSelectQuery = SQLSelectQuery(SQLAbstractQuery("""
SELECT first_name, middle_name, last_name FROM applicants INNER JOIN specialties ON applicants.specialization = specialties.id  WHERE specialties.title = "Информатика и вычислительная техника"
"""))
_select9: SQLSelectQuery = SQLSelectQuery(SQLAbstractQuery("""
SELECT DISTINCT subject.title FROM subject INNER JOIN study_card ON study_card.subject = subject.id WHERE group_title='101'
"""))
_select10: SQLSelectQuery = SQLSelectQuery(SQLAbstractQuery("""
SELECT first_name, middle_name, last_name, grade FROM applicants INNER JOIN specialties ON applicants.specialization = specialties.id INNER JOIN study_card ON study_card.id_student = applicants.id WHERE specialties.title = 'Программная инженерия'
"""))
select_sequence: SQLSelectQuerySequence = [_select1, _select2,_select3,_select4, _select5, _select6, _select7,
                                           _select8, _select9, _select10]
