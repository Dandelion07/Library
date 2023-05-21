from PyQt5.QtWidgets import QDialog
from Ui_UserSearchDialog import Ui_UserSearchDialog
from Book import Book

class UserSearchDialog(Ui_UserSearchDialog, QDialog):
    def __init__(self, parent = None):
        super(QDialog, self).__init__(parent)
        super(Ui_UserSearchDialog, self).__init__()
        self.setupUi(self)
        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)

    def exec(self):
        res = super().exec()
        if res == self.Rejected:
            return (res, None)
        return (res, self.search_result)

    def btn_back_clicked(self):
        self.reject()

    def btn_search_clicked(self):
        self.title = self.txt_title.text().strip()
        self.author = self.txt_author.text().strip()

        self.search_result = Book.search(name = self.title, authors= self.author)
        self.accept()