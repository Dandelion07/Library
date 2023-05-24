from PyQt5.QtWidgets import QDialog
from Ui_AddMemberDialog import Ui_AddMemberDialog
from Member import Member
from QuestionDialog import QuestionDialog

class AddMemberDialog(Ui_AddMemberDialog, QDialog):
    def __init__(self,employee_id: int, parent = None):
        super(Ui_AddMemberDialog, self).__init__()
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.employee_id = employee_id

        self.lbl_error.setVisible(False)
        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_add.clicked.connect(self.btn_add_clicked)

    def set_error(self, message: str = "خطا"):
        self.lbl_error.setText(message)
        self.lbl_error.setVisible(True)

    def check_error(self) -> bool:
        self.lbl_error.setVisible(False)
        if self.txt_fname.text().strip() == "":
            self.set_error("نام عضو را وارد کنید")
            return False
        if self.txt_lname.text().strip() == "":
            self.set_error("نام خانوادگی عضو را وارد کنید")
            return False
        if self.txt_phone.text().strip() == "":
            self.set_error("شماره موبایل عضو را وارد کنید")
            return False
        if self.txt_address.text().strip() == "":
            self.set_error("آدرس عضو را وارد کنید")
            return False
        return True
    
    def btn_back_clicked(self):
        self.reject()

    def btn_add_clicked(self):
        if not self.check_error():
            return
        first_name = self.txt_fname.text().strip()
        last_name = self.txt_lname.text().strip()
        phone = self.txt_phone.text().strip()
        address = self.txt_address.text().strip()
        Member.add_member(first_name, last_name, phone, address, self.employee_id)
        QuestionDialog(self, "عضو جدید با موفقیت ایجاد شد.", "پیام").exec()
        self.accept()
    