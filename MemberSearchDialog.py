from PyQt5.QtWidgets import QDialog
from Ui_MemberSearchDialog import Ui_MemberSearchDialog
from Section import Section
from Book import Book

class MemberSearchDialog(Ui_MemberSearchDialog, QDialog):
    def __init__(self, parent = None):
        super(Ui_MemberSearchDialog, self).__init__()
        super(QDialog, self).__init__(parent)
        self.setupUi(self)

        self.sections = Section.get_all_sections()
        self.cmb_section.clear()
        self.cmb_section.addItem("همه بخش‌ها")
        self.cmb_section.addItems([s.name for s in self.sections])
        self.cmb_section.setCurrentIndex(0)

        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)

    def exec(self):
        res = super().exec()
        if res == self.Rejected:
            return (res, None)
        return (res, self.books)

    def btn_back_clicked(self):
        self.reject()

    def btn_search_clicked(self):
        self.book_id = int(self.txt_id.text().strip()) if self.txt_id.text().strip() != "" else None
        self.title = self.txt_title.text().strip() or None
        self.author = self.txt_author.text().strip() or None
        self.translator = self.txt_translator.text().strip() or None
        self.publication = self.txt_publication.text().strip() or None
        self.section = self.cmb_section.currentText() if self.cmb_section.currentIndex() != 0 else None

        self.books = Book.search(book_id = self.book_id, name = self.title, authors = self.author, translators = self.translator, publication_name = self.publication, section_name = self.section)
        self.accept()