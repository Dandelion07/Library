# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ShowMembersStatsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowMembersStatsDialog(object):
    def setupUi(self, ShowMembersStatsDialog):
        ShowMembersStatsDialog.setObjectName("ShowMembersStatsDialog")
        ShowMembersStatsDialog.resize(420, 400)
        ShowMembersStatsDialog.setMinimumSize(QtCore.QSize(420, 400))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        ShowMembersStatsDialog.setFont(font)
        ShowMembersStatsDialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        ShowMembersStatsDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.verticalLayout = QtWidgets.QVBoxLayout(ShowMembersStatsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbl_members = QtWidgets.QTableWidget(ShowMembersStatsDialog)
        self.tbl_members.setObjectName("tbl_members")
        self.tbl_members.setColumnCount(4)
        self.tbl_members.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_members.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_members.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_members.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_members.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tbl_members)
        self.hlay_buttons = QtWidgets.QHBoxLayout()
        self.hlay_buttons.setObjectName("hlay_buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_buttons.addItem(spacerItem)
        self.btn_back = QtWidgets.QPushButton(ShowMembersStatsDialog)
        self.btn_back.setObjectName("btn_back")
        self.hlay_buttons.addWidget(self.btn_back)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_buttons.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.hlay_buttons)

        self.retranslateUi(ShowMembersStatsDialog)
        QtCore.QMetaObject.connectSlotsByName(ShowMembersStatsDialog)

    def retranslateUi(self, ShowMembersStatsDialog):
        _translate = QtCore.QCoreApplication.translate
        ShowMembersStatsDialog.setWindowTitle(_translate("ShowMembersStatsDialog", "آمار امانت اعضا"))
        item = self.tbl_members.horizontalHeaderItem(0)
        item.setText(_translate("ShowMembersStatsDialog", "کد عضو"))
        item = self.tbl_members.horizontalHeaderItem(1)
        item.setText(_translate("ShowMembersStatsDialog", "نام"))
        item = self.tbl_members.horizontalHeaderItem(2)
        item.setText(_translate("ShowMembersStatsDialog", "نام خانوادگی"))
        item = self.tbl_members.horizontalHeaderItem(3)
        item.setText(_translate("ShowMembersStatsDialog", "تعداد امانت"))
        self.btn_back.setText(_translate("ShowMembersStatsDialog", "بازگشت"))