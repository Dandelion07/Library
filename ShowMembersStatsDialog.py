from Ui_ShowMembersStatsDialog import Ui_ShowMembersStatsDialog
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView

class ShowMembersStatsDialog(Ui_ShowMembersStatsDialog, QDialog):
    def __init__(self, parent = None, stats: list[tuple] = []):
        super(Ui_ShowMembersStatsDialog, self).__init__()
        super(QDialog, self).__init__(parent)
        self.setupUi(self)

        self.btn_back.clicked.connect(self.btn_back_clicked)

        self.tbl_members.setRowCount(0)
        i = 0
        for row in stats:
            self.tbl_members.insertRow(i)
            self.tbl_members.setItem(i, 0, QTableWidgetItem(str(row[0])))
            self.tbl_members.setItem(i, 1, QTableWidgetItem(row[1]))
            self.tbl_members.setItem(i, 2, QTableWidgetItem(row[2]))
            self.tbl_members.setItem(i, 3, QTableWidgetItem(str(row[3])))
            i += 1
        self.tbl_members.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_members.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tbl_members.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.tbl_members.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def btn_back_clicked(self):
        self.reject()