from Ui_ShowLoanStatsDialog import Ui_ShowLoanStatsDialog
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView

class ShowLoanStatsDialog(Ui_ShowLoanStatsDialog, QDialog):
    def __init__(self, parent = None, stats: list[tuple] = []):
        super(Ui_ShowLoanStatsDialog, self).__init__()
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.stats = stats

        self.tbl_sections.setRowCount(0)
        i = 0
        for row in self.stats:
            self.tbl_sections.insertRow(i)
            self.tbl_sections.setItem(i, 0, QTableWidgetItem(str(row[0])))
            self.tbl_sections.setItem(i, 1, QTableWidgetItem(row[1]))
            self.tbl_sections.setItem(i, 2, QTableWidgetItem(str(row[2])))
            i += 1

        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.tbl_sections.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_sections.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tbl_sections.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def btn_back_clicked(self):
        self.reject()