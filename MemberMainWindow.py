from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QPushButton
from PyQt5.QtGui import QPixmap
from Ui_MemberMainWindow import Ui_MemberMainWindow
from Member import Member
from Loan import Loan
from MemberSearchDialog import MemberSearchDialog
from Book import Book, BookStatus
from QuestionDialog import QuestionDialog

class MemberMainWindow(Ui_MemberMainWindow, QWidget):
    def __init__(self, member: Member, parent = None):
        super(Ui_MemberMainWindow, self).__init__()
        super(QWidget, self).__init__(parent)
        self.setupUi(self)
        self.member = member
        self.lbl_member_id.setText(str(self.member.member_id))
        self.lbl_fname.setText(self.member.first_name)
        self.lbl_lname.setText(self.member.last_name)
        self.lbl_phone.setText(self.member.phone)
        self.lbl_register_date.setText(self.member.membership_date.isoformat())
        self.lbl_address.setText(self.member.address)
        if self.member.picture_path is not None:
            self.lbl_img.setPixmap(QPixmap(self.member.picture_path))

        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_back.clicked.connect(self.btn_back_clicked)

        self.loans = Loan.get_loans_by_member(self.member.member_id)
        self.fill_loan_table(self.loans)

    def fill_loan_table(self, loans: list[Loan]) -> None:
        self.tbl_loaned_books.setRowCount(0)
        i = 0
        for l in loans:
            self.tbl_loaned_books.insertRow(i)
            self.tbl_loaned_books.setItem(i, 0, QTableWidgetItem(str(l.book.book_id)))
            self.tbl_loaned_books.setItem(i, 1, QTableWidgetItem(l.book.name))
            self.tbl_loaned_books.setItem(i, 2, QTableWidgetItem(l.borrow_date.isoformat()))
            self.tbl_loaned_books.setItem(i, 3, QTableWidgetItem(l.return_date.isoformat()))
            self.tbl_loaned_books.setItem(i, 4, QTableWidgetItem(str(l.penalty)))
            i += 1

    def fill_search_table(self, books: list[Book]) -> None:
        self.tbl_searched_books.setRowCount(0)
        i = 0
        for b in books:
            self.tbl_searched_books.insertRow(i)
            self.tbl_searched_books.setItem(i, 0, QTableWidgetItem(str(b.book_id)))
            self.tbl_searched_books.setItem(i, 1, QTableWidgetItem(b.name))
            self.tbl_searched_books.setItem(i, 2, QTableWidgetItem(b.authors))
            self.tbl_searched_books.setItem(i, 3, QTableWidgetItem(b.status.value))

            if b.status == BookStatus.Loaned:
                btn_reserve = QPushButton("رزرو")
                btn_reserve.adjustSize()
                btn_reserve.clicked.connect(lambda: self.btn_reserve_clicked(b.book_id, self.member.member_id))
                self.tbl_searched_books.setCellWidget(i, 4, btn_reserve)
            elif b.status == BookStatus.Available:
                btn_loan = QPushButton("امانت")
                btn_loan.adjustSize()
                btn_loan.clicked.connect(lambda: self.btn_loan_clicked(b.book_id, self.member.member_id))
                self.tbl_searched_books.setCellWidget(i, 4, btn_loan)
            i += 1

    def btn_search_clicked(self):
        search_dlg = MemberSearchDialog(self)
        res, self.search_results = search_dlg.exec()
        if res == search_dlg.Accepted:
            self.fill_search_table(self.search_results)

    def btn_back_clicked(self):
        self.close()

    def btn_loan_clicked(self, book_id: int, member_id: int):
        res, message = Loan.request_loan(book_id, member_id)
        QuestionDialog(self, message).exec()
        if res:
            self.loans = Loan.get_loans_by_member(self.member.member_id)
            self.fill_loan_table(self.loans)

    def btn_reserve_clicked(self, book_id: int, member_id: int):
        res, message = Loan.reserve(book_id, member_id)
        QuestionDialog(self, message).exec()