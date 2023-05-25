from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QHeaderView, QMainWindow
from PyQt5.QtGui import QPixmap
from Ui_MemberMainWindow import Ui_MemberMainWindow
from Member import Member
from Loan import Loan
from MemberSearchDialog import MemberSearchDialog
from Book import Book, BookStatus
from QuestionDialog import QuestionDialog
import jdatetime
from datetime import date

class MemberMainWindow(Ui_MemberMainWindow, QWidget):
    def __init__(self, member: Member, parent: QMainWindow = None):
        super(Ui_MemberMainWindow, self).__init__()
        super(QWidget, self).__init__()
        self.parent_window = parent
        self.setupUi(self)
        self.member = member
        self.lbl_member_id.setText(str(self.member.member_id))
        self.lbl_fname.setText(self.member.first_name)
        self.lbl_lname.setText(self.member.last_name)
        self.lbl_phone.setText(self.member.phone)
        self.lbl_register_date.setText(jdatetime.date.fromgregorian(date = self.member.membership_date).strftime('%Y/%m/%d'))
        self.lbl_address.setText(self.member.address)
        if self.member.picture_path is not None:
            self.lbl_img.setPixmap(QPixmap(self.member.picture_path))

        self.tbl_loaned_books.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_loaned_books.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tbl_loaned_books.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        self.tbl_searched_books.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_searched_books.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tbl_searched_books.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

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
            self.tbl_loaned_books.setItem(i, 2, QTableWidgetItem(jdatetime.date.fromgregorian(date = l.borrow_date).strftime("%Y/%m/%d")))
            self.tbl_loaned_books.setItem(i, 3, QTableWidgetItem(jdatetime.date.fromgregorian(date = l.return_date).strftime("%Y/%m/%d")))
            self.tbl_loaned_books.setItem(i, 4, QTableWidgetItem("بله" if l.confirmed else "خیر"))
            self.tbl_loaned_books.setItem(i, 5, QTableWidgetItem(str(l.penalty) + " تومان"))
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

            loaned_books_id = [l.book.book_id for l in self.loans]

            if b.status == BookStatus.Loaned and not b.book_id in loaned_books_id:
                self.tbl_searched_books.setCellWidget(i, 4, self.create_reserve_button(b.book_id, self.member.member_id))
            elif b.status == BookStatus.Available:
                self.tbl_searched_books.setCellWidget(i, 4, self.create_loan_button(b.book_id, self.member.member_id))
            i += 1

    def create_reserve_button(self, book_id: int, member_id: int) -> QPushButton:
        btn = QPushButton("رزرو")
        btn.clicked.connect(lambda: self.btn_reserve_clicked(book_id, member_id))
        return btn
    
    def create_loan_button(self, book_id: int, member_id: int) -> QPushButton:
        btn = QPushButton("امانت")
        btn.clicked.connect(lambda: self.btn_loan_clicked(book_id, member_id))
        return btn

    def btn_search_clicked(self):
        search_dlg = MemberSearchDialog(self)
        res, self.search_results = search_dlg.exec()
        if res == search_dlg.Accepted:
            self.fill_search_table(self.search_results)

    def btn_back_clicked(self):
        self.close()
        self.parent_window.showMaximized()

    def btn_loan_clicked(self, book_id: int, member_id: int):
        res, message = Loan.request_loan(book_id, member_id)
        QuestionDialog(self, message, "پیام").exec()
        if res:
            self.loans = Loan.get_loans_by_member(self.member.member_id)
            self.fill_loan_table(self.loans)
            for book in self.search_results:
                if book.book_id == book_id:
                    book.status = BookStatus.Loaned
                    self.fill_search_table(self.search_results)

    def btn_reserve_clicked(self, book_id: int, member_id: int):
        res, message = Loan.reserve(book_id, member_id)
        QuestionDialog(self, message, "پیام").exec()
        if res:
            for book in self.search_results:
                if book.book_id == book_id:
                    book.status = BookStatus.Reserved
                    self.fill_search_table(self.search_results)
                    break
