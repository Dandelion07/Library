from Ui_ShowEmployeesDialog import Ui_ShowEmployeesDialog
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from Employee import Employee

class ShowEmployeesDialog(Ui_ShowEmployeesDialog, QDialog):
    def __init__(self, parent = None, employees: list[Employee] = []):
        super(Ui_ShowEmployeesDialog, self).__init__()
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.employees = employees
        self.btn_back.clicked.connect(self.btn_back_clicked)

        self.tbl_employees.setRowCount(0)
        i = 0
        for e in self.employees:
            self.tbl_employees.insertRow(i)
            self.tbl_employees.setItem(i, 0, QTableWidgetItem(str(e.employee_id)))
            self.tbl_employees.setItem(i, 1, QTableWidgetItem(e.first_name))
            self.tbl_employees.setItem(i, 2, QTableWidgetItem(e.last_name))
            self.tbl_employees.setItem(i, 3, QTableWidgetItem(e.phone))
            self.tbl_employees.setItem(i, 4, QTableWidgetItem(e.section.name))
            i += 1

        self.tbl_employees.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_employees.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tbl_employees.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.tbl_employees.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def btn_back_clicked(self):
        self.reject()