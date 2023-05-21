from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from Ui_MemberMainWindow import Ui_MemberMainWindow
from Member import Member
from Loan import Loan

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

    def btn_search_clicked(self):
        pass

    def btn_back_clicked(self):
        self.close()