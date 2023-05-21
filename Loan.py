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

        return [Loan(1,date(2023,5,12), date(2023,5,19), Member(1), Book(1, "کتاب 1"))]