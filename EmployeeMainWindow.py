from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QHeaderView
from Ui_EmployeeMainWindow import Ui_EmployeeMainWindow
from Employee import Employee
from Loan import Loan
from QuestionDialog import QuestionDialog
from Book import Book
from ShowMembersDialog import ShowMembersDialog

class EmployeeMainWindow(Ui_EmployeeMainWindow, QWidget):
    def __init__(self, employee: Employee, parent = None):
        super(Ui_EmployeeMainWindow, self).__init__()
        super(QWidget, self).__init__(parent)
        self.setupUi(self)

        self.employee = employee
        self.lbl_employee_id.setText(str(self.employee.employee_id))
        self.lbl_fname.setText(self.employee.first_name)
        self.lbl_lname.setText(self.employee.last_name)
        self.lbl_phone.setText(self.employee.phone)
        self.lbl_section.setText(self.employee.section.name)
        self.lbl_is_manager.setText("مدیر" if self.employee.is_manager else "مسئول")

        if not self.employee.is_manager:
            self.grp_manager_operations.setVisible(False)

        self.unconfirmed_lons = Loan.get_unconfirmed_loans(self.employee.section.section_id)
        self.fill_loan_requests_table(self.unconfirmed_lons)

        self.books = Book.search(section_name = self.employee.section.name if not self.employee.is_manager else None)
        self.fill_book_table(self.books)

        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_show_members.clicked.connect(self.btn_show_members_clicked)
        self.btn_delete_member.clicked.connect(self.btn_delete_member_clicked)
        self.btn_add_member.clicked.connect(self.btn_add_member_clicked)
        self.btn_add_book.clicked.connect(self.btn_add_book_clicked)
        self.btn_delete_book.clicked.connect(self.btn_delete_book_clicked)
        self.btn_delete_old_books.clicked.connect(self.btn_delete_old_books_clicked)


    def fill_loan_requests_table(self, loans: list[Loan]):
        self.tbl_loan_requests.setRowCount(0)
        i = 0
        for l in loans:
            self.tbl_loan_requests.insertRow(i)
            self.tbl_loan_requests.setItem(i, 0, QTableWidgetItem(str(l.book.book_id)))
            self.tbl_loan_requests.setItem(i, 1, QTableWidgetItem(l.book.name))
            self.tbl_loan_requests.setItem(i, 2, QTableWidgetItem(str(l.member.member_id)))
            self.tbl_loan_requests.setItem(i, 3, QTableWidgetItem(l.borrow_date.isoformat()))

            hlay_row_buttons = QHBoxLayout()
            btn_confirm = QPushButton("تایید")
            btn_confirm.clicked.connect(lambda: self.confirm_loan(l.loan_id))
            btn_reject = QPushButton("رد")
            btn_reject.clicked.connect(lambda: self.reject_loan(l.loan_id))
            hlay_row_buttons.addWidget(btn_confirm)
            hlay_row_buttons.addWidget(btn_reject)

            button_widget = QWidget()
            button_widget.setLayout(hlay_row_buttons)
            self.tbl_loan_requests.setCellWidget(i, 4, button_widget)
            self.tbl_loan_requests.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.tbl_loan_requests.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.tbl_loan_requests.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

            i += 1

    def fill_book_table(self, books: list[Book]):
        self.tbl_books.setRowCount(0)
        i = 0
        for b in books:
            self.tbl_books.insertRow(i)
            self.tbl_books.setItem(i, 0, QTableWidgetItem(str(b.book_id)))
            self.tbl_books.setItem(i, 1, QTableWidgetItem(b.name))
            self.tbl_books.setItem(i, 2, QTableWidgetItem(b.authors))
            self.tbl_books.setItem(i, 3, QTableWidgetItem(b.publication_name))
            self.tbl_books.setItem(i, 4, QTableWidgetItem(b.section.name))
            self.tbl_books.setItem(i, 5, QTableWidgetItem(b.status.value))

            self.tbl_books.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.tbl_books.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.tbl_books.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

            i += 1


    def confirm_loan(self, loan_id: int):
        Loan.confirm_loan(loan_id)
        QuestionDialog(self, "درخواست امانت تایید شد.", "پیام").exec()
        self.unconfirmed_lons = Loan.get_unconfirmed_loans(self.employee.section.section_id)
        self.fill_loan_requests_table(self.unconfirmed_lons)

    def reject_loan(self, loan_id: int):
        Loan.reject_loan(loan_id)
        QuestionDialog(self, "درخواست امانت رد شد.", "پیام").exec()
        self.unconfirmed_lons = Loan.get_unconfirmed_loans(self.employee.section.section_id)
        self.fill_loan_requests_table(self.unconfirmed_lons)
    
    def btn_back_clicked(self):
        self.close()

    def btn_show_members_clicked(self):
        ShowMembersDialog(self).exec()

    def btn_delete_member_clicked(self):
        ShowMembersDialog(self, True).exec()

    def btn_add_member_clicked(self):
        pass

    def btn_add_book_clicked(self):
        pass

    def btn_delete_book_clicked(self):
        pass

    def btn_delete_old_books_clicked(self):
        pass