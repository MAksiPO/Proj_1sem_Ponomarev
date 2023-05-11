from sqlite3 import Cursor, connect


class SQL:
    def __init__(self, sql_path: str):
        self.sql_path: str = sql_path

    def get_cursor(self) -> Cursor:
        with connect(self.sql_path) as con:
            return con.cursor()

    def create_tables(self) -> None:
        cursor = self.get_cursor()
        print('создаю таблицу...')
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS faculties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR
            );
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR,
                faculty_id INT,
                FOREIGN KEY (faculty_id) REFERENCES faculties(id) ON DELETE CASCADE
                );  

            CREATE TABLE IF NOT EXISTS specialties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR,
                department_id INT,
                FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE CASCADE
                );

            CREATE TABLE IF NOT EXISTS subject (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title VARCHAR
                );

            CREATE TABLE IF NOT EXISTS subject_pass_form (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title VARCHAR
                );

            CREATE TABLE IF NOT EXISTS сurriculum (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                specialization_id INTEGER,
                subject_id INTEGER,
                subject_pass_form_id INTEGER,
                lecture_hours INTEGER,
                practical_hours INTEGER,
                lab_hours INTEGER,
                coursework_required BOOL,
                FOREIGN KEY (specialization_id) REFERENCES specialties(id) ON DELETE CASCADE,
                FOREIGN KEY (subject_id) REFERENCES subject(id) ON DELETE CASCADE,
                FOREIGN KEY (subject_pass_form_id) REFERENCES subject_pass_form(id) ON DELETE CASCADE
                );

            CREATE TABLE IF NOT EXISTS applicants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                last_name VARCHAR,
                first_name VARCHAR,
                middle_name VARCHAR,
                sex VARCHAR,
                date_of_birth DATETIME,
                address VARCHAR,
                phone VARCHAR,
                email VARCHAR,
                enrollment_date DATETIME,
                specialization INTEGER, 
                FOREIGN KEY (specialization) REFERENCES specialties(id) ON DELETE CASCADE
                );   

            CREATE TABLE IF NOT EXISTS study_card (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_student INTEGER,
                group_title TEXT,
                specialization INTEGER,
                subject INTEGER,
                subject_pass_form INTEGER,
                grade INTEGER,
                FOREIGN KEY (specialization) REFERENCES specialties(id) ON DELETE CASCADE,
                FOREIGN KEY (subject) REFERENCES subject(id) ON DELETE CASCADE,
                FOREIGN KEY (subject_pass_form) REFERENCES subject_pass_form(id) ON DELETE CASCADE,
                FOREIGN KEY (id_student) REFERENCES applicants(id) ON DELETE CASCADE
                );
            """)
