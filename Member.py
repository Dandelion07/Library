from datetime import date
from Employee import Employee
import pyodbc
from DatabaseManager import DatabaseManager

class Member:
    def __init__(self, member_id: int,
                 first_name: str = None,
                 last_name: str = None,
                 phone: str = None,
                 address: str = None,
                 membership_date: date = None,
                 picture_path: str = None,
                 registered_by: Employee = None) -> None:
        self.member_id: int = member_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.phone: str = phone
        self.address: str = address
        self.membership_date: date = membership_date
        self.picture_path: str = picture_path
        self.registered_by: Employee = registered_by

    @classmethod
    def Login(cls, username: int, password: str):
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""SELECT * FROM Member WHERE member_id = ? '1234' = ?""", username, password)
        # res = cursor.fetchone()
        # if not res:
        #     return (False, "کد عضویت یا رمز عبور نادرست است")
        # return (True, Member(res[0], res[1], res[2], res[3], res[4], date(res[5]), res[6]))

        return (True, Member(1, "فاطمه", "آقابابایی", "09131234567", "اصفهان", date.fromisoformat("2020-05-22")))