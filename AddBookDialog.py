from Ui_AddBookDialog import Ui_AddBookDialog
from PyQt5.QtWidgets import QDialog, QPushButton, QHeaderView, QTableWidgetItem
from Section import Section
import jdatetime
from Book import Book
from QuestionDialog import QuestionDialog

class AddBookDialog(Ui_AddBookDialog, QDialog):
    def __init__(self, section: Section, parent = None):
        super(Ui_AddBookDialog, self).__init__()
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.lbl_error.setVisible(False)
        self.section = section
        self.cmb_section.clear()
        self.cmb_section.addItem(self.section.name)
        self.cmb_section.setCurrentIndex(0)

        self.tbl_authors.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_authors.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_translators.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_translators.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_add_author.clicked.connect(self.btn_add_author_clicked)
        self.btn_add_translator.clicked.connect(self.btn_add_translator_clicked)
        self.btn_add_book.clicked.connect(self.btn_add_book_clicked)

    def set_error(self, message: str = "خطا"):
        self.lbl_error.setText(message)
        self.lbl_error.setVisible(True)

    def check_error(self) -> bool:
        self.lbl_error.setVisible(False)
        if self.txt_title.text().strip() == "":
            self.set_error("نام کتاب را وارد کنید")
            return False
        if self.txt_publication.text().strip() == "":
            self.set_error("نام انتشارات را وارد کنید")
            return False
        try:
            d = jdatetime.date(int(self.spn_year.text()), int(self.spn_month.text()), int(self.spn_day.text()))
            if d > jdatetime.date.today():
                self.set_error("تاریخ انتشار نباید از تاریخ امروز بزرگتر باشد")
                return False
        except:
            self.set_error("تاریخ نادرست است")
            return False
        if self.tbl_authors.rowCount() == 0:
            self.set_error("باید حداقل یک نویسنده را اضافه کنید")
            return False
        return True
    
    def btn_back_clicked(self):
        self.reject()

    def btn_add_author_clicked(self):
        self.lbl_error.setVisible(False)
        if self.txt_fname.text().strip() == "":
            self.set_error("نام نویسنده را وارد کنید")
            return
        if self.txt_lname.text().strip() == "":
            self.set_error("نام خانوادگی نویسنده را وارد کنید")
            return
        idx = self.tbl_authors.rowCount()
        self.tbl_authors.insertRow(idx)
        self.tbl_authors.setItem(idx, 0, QTableWidgetItem(self.txt_fname.text().strip()))
        self.tbl_authors.setItem(idx, 1, QTableWidgetItem(self.txt_lname.text().strip()))

        btn_delete = QPushButton("حذف")
        btn_delete.clicked.connect(lambda: self.tbl_authors.removeRow(self.tbl_authors.currentRow()))
        self.tbl_authors.setCellWidget(idx, 2, btn_delete)
        self.txt_fname.clear()
        self.txt_lname.clear()
        self.txt_fname.setFocus()

    def btn_add_translator_clicked(self):
        self.lbl_error.setVisible(False)
        if self.txt_fname.text().strip() == "":
            self.set_error("نام مترجم را وارد کنید")
            return
        if self.txt_lname.text().strip() == "":
            self.set_error("نام خانوادگی مترجم را وارد کنید")
            return
        idx = self.tbl_translators.rowCount()
        self.tbl_translators.insertRow(idx)
        self.tbl_translators.setItem(idx, 0, QTableWidgetItem(self.txt_fname.text().strip()))
        self.tbl_translators.setItem(idx, 1, QTableWidgetItem(self.txt_lname.text().strip()))

        btn_delete = QPushButton("حذف")
        btn_delete.clicked.connect(lambda: self.tbl_translators.removeRow(self.tbl_translators.currentRow()))
        self.tbl_translators.setCellWidget(idx, 2, btn_delete)

        self.txt_fname.clear()
        self.txt_lname.clear()
        self.txt_fname.setFocus()

    def btn_add_book_clicked(self):
        self.lbl_error.setVisible(False)
        if not self.check_error():
            return
        authors = " - ".join(f"{self.tbl_authors.item(row, 0).text()} {self.tbl_authors.item(row, 1).text()}" for row in range(self.tbl_authors.rowCount()))
        translators = " - ".join(f"{self.tbl_translators.item(row, 0).text()} {self.tbl_translators.item(row, 1).text()}" for row in range(self.tbl_translators.rowCount())) if self.tbl_translators.rowCount() > 0 else None
        title = self.txt_title.text().strip()
        publication = self.txt_publication.text().strip()
        release_date = jdatetime.date(int(self.spn_year.text()), int(self.spn_month.text()), int(self.spn_day.text())).togregorian()
        Book.add_book(title, authors, translators, publication, release_date, self.section.section_id)
        QuestionDialog(self, "کتاب با موفقیت ثبت شد", "پیام").exec()
        self.accept()