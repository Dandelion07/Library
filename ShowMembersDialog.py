from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from Ui_ShowMembersDialog import Ui_ShowMembersDialog
from Member import Member

class ShowMembersDialog(Ui_ShowMembersDialog, QDialog):
    def __init__(self, parent = None, delete_mode: bool = False):
        super(Ui_ShowMembersDialog, self).__init__()
        super(QDialog, self).__init__(parent)
        self.setupUi(self)

        if delete_mode:
            self.setWindowTitle("حذف اعضای کتابخانه")
        else:
            self.btn_delete.setVisible(False)

        self.members = Member.get_all_members()
        self.fill_members_table(self.members)

        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_back.clicked.connect(self.btn_back_clicked)

    def fill_members_table(self, members: list[Member]):
        self.tbl_members.setRowCount(0)
        i = 0
        for m in members:
            self.tbl_members.insertRow(i)
            self.tbl_members.setItem(i, 0, QTableWidgetItem(str(m.member_id)))
            self.tbl_members.setItem(i, 1, QTableWidgetItem(m.first_name))
            self.tbl_members.setItem(i, 2, QTableWidgetItem(m.last_name))
            self.tbl_members.setItem(i, 3, QTableWidgetItem(m.phone))
            self.tbl_members.setItem(i, 4, QTableWidgetItem(m.membership_date.isoformat()))
            self.tbl_members.setItem(i, 5, QTableWidgetItem(m.address))

            i += 1

        self.tbl_members.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_members.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)

    def btn_delete_clicked(self):
        pass        

    def btn_back_clicked(self):
        self.reject()
