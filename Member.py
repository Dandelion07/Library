from datetime import date
from Employee import Employee
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
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""
            SELECT [member_id], [first_name], [last_name], [phone], [address], [membership_date], [picture_path], [registered_by]
            FROM Member WHERE member_id = ? AND '1234' = ?
        """, username, password)
        res = cursor.fetchone()
        if not res:
            return (False, "کد عضویت یا رمز عبور نادرست است")
        return (True, Member(int(res[0]), res[1], res[2], res[3], res[4], date.fromisoformat(res[5]), res[6], Employee(int(res[7]))))
    
    @classmethod
    def get_all_members(cls) -> list['Member']:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT member_id, first_name, last_name, phone, address, membership_date, picture_path, registered_by FROM Member""")
        members = list()
        for item in cursor:
            members.append(Member(int(item[0]), item[1], item[2], item[3], item[4], date.fromisoformat(item[5]), item[6], Employee(int(item[7]))))
        return members
    
    @classmethod
    def delete_member(cls, member_id: int):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT loan_id FROM loan WHERE member_id = ?""", member_id)
        loans_id = [int(row[0]) for row in cursor.fetchall()]
        from Loan import Loan
        for loan_id in loans_id:
            Loan.delete_loan(loan_id)
        cursor.execute("""DELETE FROM member WHERE member_id = ?""", member_id)
        cursor.commit()
    
    @classmethod
    def add_member(cls, first_name: str, last_name: str, phone: str, address: str, employee_id: int):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""
            INSERT INTO member (first_name, last_name, phone, address, membership_date, registered_by)
            VALUES (?, ?, ?, ?, GETDATE(), ?)
        """, first_name, last_name, phone, address, employee_id)
        cursor.commit()    
    