from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QHBoxLayout
from Ui_EmployeeMainWindow import Ui_EmployeeMainWindow
from Employee import Employee
from Loan import Loan

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

    def fill_loan_requests_table(self, loans: list[Loan]):
        self.tbl_loan_requests.setRowCount(0)
        i = 0
        for l in loans:
            self.tbl_loan_requests.insertRow(i)
            self.tbl_loan_requests.setItem(i, 0, QTableWidgetItem(str(l.book.book_id)))
            self.tbl_loan_requests.setItem(i, 1, QTableWidgetItem(l.book.name))
            self.tbl_loan_requests.setItem(i, 2, QTableWidgetItem(l.member.member_id))
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

    def confirm_loan(self, loan_id: int):
        pass

    def reject_loan(self, loan_id: int):
        pass
    