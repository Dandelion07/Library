from Section import Section
from DatabaseManager import DatabaseManager
from datetime import date

class Employee:
    def __init__(self, employee_id: int,
                 first_name: str,
                 last_name: str,
                 phone: str = None,
                 section: Section = None,
                 is_manager: bool = False) -> None:
        self.employee_id: int = employee_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.phone: str = phone
        self.section: Section = section
        self.is_manager = is_manager

    @classmethod
    def Login(self, username: int, password: str):
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""SELECT e.employee_id, e.first_name, e.last_name, e.phone, s.section_id, s.name, IIF(m.manager_id = NULL, 0, 1) AS is_manager
        #   FROM employee as e
        #   INNER JOIN section as s ON s.section_id = e.section_id
        #   LEFT JOIN manager as m ON e.employee_id = m.manager_id
        #   WHERE e.employee_id = 1""", username, password)
        # res = cursor.fetchone()
        # if not res:
        #     return (False, "کد پرسنلی یا رمز عبور نادرست است")
        # return (True, Employee(res[0], res[1], res[2], res[3], Section(res[4], res[5]), res[5]))

        return (True, Employee(1, "فاطمه", "آقابابایی", "09131234567", Section(1, "رمان"), True))
    
    @classmethod
    def get_all_employees(cls) -> list['Employee']:
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""
        #     SELECT e.employee_id, e.first_name, e.last_name, e.phone, s.section_id, s.name, IIF(m.manager_id = NULL, 0, 1) AS is_manager
        #     FROM employee as e
        #     INNER JOIN section as s ON s.section_id = e.section_id
        #     LEFT JOIN manager as m ON e.employee_id = m.manager_id
        # """)
        # employees = list()
        # for item in cursor:
        #     employees.append(Employee(int(item[0]), item[1], item[2], item[3], Section(int(item[4]), item[5]), bool(item[6])))
        # return employees

        return [Employee(1, "فاطمه", "آقابابایی", "09123456789", Section(1, "رمان"), True),
                Employee(2, "علیرضا", "محمدی", "09123456789", Section(2, "تاریخی"), False),
                Employee(3, "پریسا", "عمادی", "09123456789", Section(3, "علمی"), False)]