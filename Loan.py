from datetime import date
from Member import Member
from Book import Book, BookStatus
from DatabaseManager import DatabaseManager

class Loan:
    def __init__(self, loan_id: int,
                 borrow_date: date,
                 return_date: date,
                 member: Member,
                 book: Book,
                 penalty: int = 0) -> None:
        self.loan_id: int = loan_id
        self.borrow_date: date = borrow_date
        self.return_date: date = return_date
        self.member: Member = member
        self.book: Book = book
        self.penalty: int = penalty

    @classmethod
    def get_loans_by_member(cls, member_id: int) -> list['Loan']:
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""
        #     SELECT l.loan_id, l.borrow_date, l.return_date, b.book_id, b.name, 
        #     FROM book AS b
        #     INNER JOIN loan AS l ON l.book_id = b.book_id
        #     INNER JOIN member AS m ON l.member_id = m.member_id
        #     WHERE m.member_id = ? AND b.status = '?'
        # """, member_id, BookStatus.Loaned)
        # loans = list()
        # for item in cursor:
        #     loan = Loan(item[0], date.fromisoformat(item[1]), date.fromisoformat(item[2]), Member(member_id), Book(int(item[3]), item[4]))
        #     loan.penalty = max((date.today() - loan.return_date).days, 0) * 5000
        #     loans.append(loan)

        # return loans

        return [Loan(1,date(2023,5,12), date(2023,5,19), Member(1), Book(1, "کتاب  1 کتاب 1 کتاب 1 کتاب 1 کتاب 1 کتاب 1 کتاب 1 کتاب 1"), 10000)]
    
    @classmethod
    def request_loan(cls, book_id: int, member_id: int):
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""SELECT COUNT(*) FROM loan WHERE member_id = ? AND returned = 0""", member_id)
        # loan_count = int(cursor.fetchone()[0])
        # if loan_count >= 5:
        #     return (False, "حداکثر تعداد مجاز امانت کتاب 5 مورد می‌باشد")
        
        # cursor.execute("""INSERT INTO loan([borrow_date], [return_date], [penalty], [member_id], [book_id], [returned], [confirmed])
        #                     VALUES
        #                     (GETDATE(), DATEADD(day, 7, GETDATE()), 0, ?, ?, 0, 0)""", member_id, book_id)
        # cursor.commit()
        # return (True, "درخواست امانت با موفقیت ثبت شد. منتظر تایید مسئول بخش باشید.")

        return (True, "درخواست امانت با موفقیت ثبت شد. منتظر تایید مسئول بخش باشید.")
        
    @classmethod
    def reserve(cls, book_id: int, member_id: int):
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""SELECT reserved_by FROM book WHERE book_id = ?""", book_id)
        # _id = cursor.fetchone()[0]
        # if _id is None:
        #     return (False, "کتاب توسط شخص دیگری رزرو شده است")
        # cursor.execute("""UPDATE book SET reserved_by = ? WHERE book_id = ?""", member_id, book_id)
        # cursor.commit()
        # return (True, "کتاب با موفقیت رزرو شد.")

        return (True, "کتاب با موفقیت رزرو شد.")

    @classmethod
    def get_unconfirmed_loans(cls, section_id: int) -> list['Loan']:
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""
        # SELECT l.loan_id, l.borrow_date, l.return_date, l.member_id, l.book_id, b.name
        # FROM loan AS l
        # INNER JOIN book AS b ON l.book_id = b.book_id
        # INNER JOIN section AS s ON b.section_id = s.section_id
        # WHERE s.section_id = ?
        # """, section_id)

        # loans = list()
        # for item in cursor:
        #     loans.append(Loan(int(item[0]), date.fromisoformat(item[1]), date.fromisoformat(item[2]), Member(int(item[3])), Book(int(item[4]), item[5])))

        # return loans

        return [Loan(1, date(2023,5,22), date(2023,5,29), Member(1), Book(1, "کتاب1")),
                Loan(2, date(2023,5,22), date(2023,5,29), Member(2), Book(1, "کتاب2")),
                Loan(3, date(2023,5,22), date(2023,5,29), Member(3), Book(1, "کتاب3"))]

    @classmethod
    def confirm_loan(cls, loan_id: int) -> None:
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""UPDATE loan SET confirmed = 1 WHERE loan_id = ?""", loan_id)
        # cursor.commit()
        return

    @classmethod
    def reject_loan(cls, loan_id: int) -> None:
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""DELETE FROM loan WHERE loan_id = ?""", loan_id)
        # cursor.commit()
        return
    
    @classmethod
    def get_loan_stats_by_sections(cls) -> list[tuple]:
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""
        #     SELECT s.section_id, s.name, COUNT(l.loan_id) AS loan_count
        #     FROM loan AS l
        #     INNER JOIN book AS b ON l.book_id = l.book_id
        #     INNER JOIN section AS s ON s.section_id = b.section_id
        #     GROUP BY s.section_id
        #     ORDER BY loan_count DESC
        # """)
        # result = list()
        # for item in cursor:
        #     result.append((int(item[0]), item[1], int(item[2])))
        # return result

        return [(1, "رمان", 78), (2, "تاریخی", 60), (3, "ادبیات", 58), (4, "علمی", 50), (5, "تخیلی", 37)]

    @classmethod
    def get_loan_stats_by_members(cls) -> list[tuple]:
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""
        #     SELECT l.member_id, m.first_name, m.last_name, COUNT(l.loan_id) AS loan_count
        #     FROM loan AS l
        #     INNER JOIN member AS m ON l.member_id = l.member_id
        #     GROUP BY l.member_id, m.first_name, m.last_name
        #     ORDER BY loan_count DESC
        # """)
        # result = list()
        # for item in cursor:
        #     result.append((int(item[0]), item[1], item[2], int(item[3])))
        # return result

        return [(1, "علیرضا", "آقابابایی", 7),
                (2, "پریسا", "عمادی", 6),
                (3, "فاطمه", "آقابابایی", 4)]