# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MemberSearchDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MemberSearchDialog(object):
    def setupUi(self, MemberSearchDialog):
        MemberSearchDialog.setObjectName("MemberSearchDialog")
        MemberSearchDialog.resize(270, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MemberSearchDialog.sizePolicy().hasHeightForWidth())
        MemberSearchDialog.setSizePolicy(sizePolicy)
        MemberSearchDialog.setMinimumSize(QtCore.QSize(270, 270))
        MemberSearchDialog.setMaximumSize(QtCore.QSize(270, 270))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        MemberSearchDialog.setFont(font)
        MemberSearchDialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        MemberSearchDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.verticalLayout = QtWidgets.QVBoxLayout(MemberSearchDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.flay_inputs = QtWidgets.QFormLayout()
        self.flay_inputs.setObjectName("flay_inputs")
        self.lbl_title = QtWidgets.QLabel(MemberSearchDialog)
        self.lbl_title.setObjectName("lbl_title")
        self.flay_inputs.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_title)
        self.txt_title = QtWidgets.QLineEdit(MemberSearchDialog)
        self.txt_title.setClearButtonEnabled(True)
        self.txt_title.setObjectName("txt_title")
        self.flay_inputs.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_title)
        self.lbl_author = QtWidgets.QLabel(MemberSearchDialog)
        self.lbl_author.setObjectName("lbl_author")
        self.flay_inputs.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_author)
        self.txt_author = QtWidgets.QLineEdit(MemberSearchDialog)
        self.txt_author.setClearButtonEnabled(True)
        self.txt_author.setObjectName("txt_author")
        self.flay_inputs.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_author)
        self.lbl_id = QtWidgets.QLabel(MemberSearchDialog)
        self.lbl_id.setObjectName("lbl_id")
        self.flay_inputs.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_id)
        self.txt_id = QtWidgets.QLineEdit(MemberSearchDialog)
        self.txt_id.setClearButtonEnabled(True)
        self.txt_id.setObjectName("txt_id")
        self.flay_inputs.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_id)
        self.lbl_translator = QtWidgets.QLabel(MemberSearchDialog)
        self.lbl_translator.setObjectName("lbl_translator")
        self.flay_inputs.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_translator)
        self.txt_translator = QtWidgets.QLineEdit(MemberSearchDialog)
        self.txt_translator.setClearButtonEnabled(True)
        self.txt_translator.setObjectName("txt_translator")
        self.flay_inputs.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_translator)
        self.lbl_publication = QtWidgets.QLabel(MemberSearchDialog)
        self.lbl_publication.setObjectName("lbl_publication")
        self.flay_inputs.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_publication)
        self.txt_publication = QtWidgets.QLineEdit(MemberSearchDialog)
        self.txt_publication.setClearButtonEnabled(True)
        self.txt_publication.setObjectName("txt_publication")
        self.flay_inputs.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_publication)
        self.lbl_section = QtWidgets.QLabel(MemberSearchDialog)
        self.lbl_section.setObjectName("lbl_section")
        self.flay_inputs.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_section)
        self.cmb_section = QtWidgets.QComboBox(MemberSearchDialog)
        self.cmb_section.setObjectName("cmb_section")
        self.flay_inputs.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cmb_section)
        self.verticalLayout.addLayout(self.flay_inputs)
        self.hlay_buttons = QtWidgets.QHBoxLayout()
        self.hlay_buttons.setObjectName("hlay_buttons")
        self.btn_search = QtWidgets.QPushButton(MemberSearchDialog)
        self.btn_search.setObjectName("btn_search")
        self.hlay_buttons.addWidget(self.btn_search)
        self.btn_back = QtWidgets.QPushButton(MemberSearchDialog)
        self.btn_back.setObjectName("btn_back")
        self.hlay_buttons.addWidget(self.btn_back)
        self.verticalLayout.addLayout(self.hlay_buttons)

        self.retranslateUi(MemberSearchDialog)
        QtCore.QMetaObject.connectSlotsByName(MemberSearchDialog)

    def retranslateUi(self, MemberSearchDialog):
        _translate = QtCore.QCoreApplication.translate
        MemberSearchDialog.setWindowTitle(_translate("MemberSearchDialog", "جست‌وجوی کتاب"))
        self.lbl_title.setText(_translate("MemberSearchDialog", "عنوان کتاب"))
        self.lbl_author.setText(_translate("MemberSearchDialog", "نویسنده"))
        self.lbl_id.setText(_translate("MemberSearchDialog", "کد کتاب"))
        self.lbl_translator.setText(_translate("MemberSearchDialog", "مترجم"))
        self.lbl_publication.setText(_translate("MemberSearchDialog", "انتشارات"))
        self.lbl_section.setText(_translate("MemberSearchDialog", "بخش"))
        self.btn_search.setText(_translate("MemberSearchDialog", "جست‌وجو"))
        self.btn_back.setText(_translate("MemberSearchDialog", "بازگشت"))
