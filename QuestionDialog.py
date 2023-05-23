from PyQt5.QtWidgets import QDialog
from Ui_QuestionDialog import Ui_QuestionDialog

class QuestionDialog(Ui_QuestionDialog, QDialog):
    def __init__(self, parent = None, message: str = "", title: str = ""):
        super(Ui_QuestionDialog, self).__init__()
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.lbl_message.setText(message)
        self.setWindowTitle(title)

        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_confirm.clicked.connect(self.btn_confirm_clicked)

    def btn_back_clicked(self):
        self.reject()

    def btn_confirm_clicked(self):
        self.accept()