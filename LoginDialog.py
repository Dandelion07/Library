from PyQt5.QtWidgets import QDialog
from Ui_LoginDialog import Ui_LoginDialog
from Member import Member
from Employee import Employee

class LoginDialog(Ui_LoginDialog, QDialog):
    def __init__(self, parent = None) -> None:
        super(Ui_LoginDialog, self).__init__()
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.lbl_error.setVisible(False)
        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_login.clicked.connect(self.btn_login_clicked)

        self.adjustSize()

    def exec(self):
        res = super().exec()
        if res == self.Rejected:
            return (res, None)
        return (res, self.member or self.employee)

    def __set_error_message(self, message):
        self.lbl_error.setText(message)
        self.lbl_error.setVisible(True)

    def btn_back_clicked(self):
        self.reject()

    def btn_login_clicked(self):
        self.lbl_error.setVisible(False)
        if self.txt_username.text().strip() == "":
            self.__set_error_message("کد عضویت/پرسنلی را وارد کنید")
            return
        if self.txt_password.text().strip() == "":
            self.__set_error_message("رمز عبور را وارد کنید")
            return
        
        self.id = int(self.txt_username.text().strip())
        self.password = self.txt_password.text().strip()

        if self.rdb_member.isChecked():
            res = Member.Login(self.id, self.password)
            if not res[0]:
                self.__set_error_message(res[1])
                self.reject()
                return
            self.member = res[1]
            self.employee = None
        else:
            res = Employee.Login(self.id, self.password)
            if not res[0]:
                self.__set_error_message(res[1])
                self.reject()
                return
            self.member = None
            self.employee = res[1]

        self.accept()