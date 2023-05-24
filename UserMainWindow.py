from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from Section import Section
from Ui_UserMainWindow import Ui_UserMainWindow
from Library import Library
from Book import Book
from LoginDialog import LoginDialog
from UserSearchDialog import UserSearchDialog
from Member import Member
from MemberMainWindow import MemberMainWindow
from EmployeeMainWindow import EmployeeMainWindow

class UserMainWindow(QMainWindow, Ui_UserMainWindow):
    def __init__(self) -> None:
        super(QMainWindow, self).__init__()
        super(Ui_UserMainWindow, self).__init__()
        self.setupUi(self)

        self.library = Library.get_info()
        self.lbl_lib_name.setText(self.library.name)
        self.lbl_tel.setText(self.library.phone)
        self.lbl_address.setText(self.library.address)

        self.sections = Section.get_all_sections()
        self.cmb_section.clear()
        self.cmb_section.addItem("--نمایش همه بخش‌ها--")
        for s in self.sections:
            self.cmb_section.addItem(s.name)

        self.cmb_section.currentIndexChanged.connect(self.cmb_section_changed)
        self.cmb_section.setCurrentIndex(0)
        self.btn_show_all.clicked.connect(self.btn_all_books_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_Login.clicked.connect(self.btn_login_clicked)

    def fill_book_table(self, books: list[Book]) -> None:
        self.tbl_books.setRowCount(0)

        i = 0
        for b in books:
            self.tbl_books.insertRow(i)
            self.tbl_books.setItem(i, 0, QTableWidgetItem(str(b.book_id)))
            self.tbl_books.setItem(i, 1, QTableWidgetItem(b.name))
            self.tbl_books.setItem(i, 2, QTableWidgetItem(b.authors))
            self.tbl_books.setItem(i, 3, QTableWidgetItem(b.translators))
            self.tbl_books.setItem(i, 4, QTableWidgetItem(b.publication_name))
            self.tbl_books.setItem(i, 5, QTableWidgetItem(b.section.name))
            self.tbl_books.setItem(i, 6, QTableWidgetItem(b.release_date.isoformat()))
            self.tbl_books.setItem(i, 7, QTableWidgetItem(b.status.value))
            i += 1
    
    def cmb_section_changed(self, section_id: int) -> None:
        books = Book.get_book_from_section(self.cmb_section.itemText(section_id) if section_id != 0 else "")
        self.fill_book_table(books)

    def btn_all_books_clicked(self):
        self.cmb_section.setCurrentIndex(0)

    def btn_search_clicked(self):
        search_dlg = UserSearchDialog(self)
        res = search_dlg.exec()
        if res[0] == search_dlg.Accepted:
            self.fill_book_table(res[1])

    def btn_login_clicked(self):
        login_dlg = LoginDialog(self)
        res = login_dlg.exec()
        if res[0] == login_dlg.Accepted:
            self.close()
            if isinstance(res[1], Member):
                self.member_window = MemberMainWindow(res[1])
                self.member_window.showMaximized()
            else:
                self.employee_window = EmployeeMainWindow(res[1])
                self.employee_window.showMaximized()
