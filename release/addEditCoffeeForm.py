# Form implementation generated from reading ui file 'UI\addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(797, 599)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.addId = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.addId.setObjectName("addId")
        self.horizontalLayout.addWidget(self.addId)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.addName = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.addName.setObjectName("addName")
        self.horizontalLayout_2.addWidget(self.addName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.addRoasting = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.addRoasting.setObjectName("addRoasting")
        self.horizontalLayout_3.addWidget(self.addRoasting)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.addGrounding = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.addGrounding.setObjectName("addGrounding")
        self.horizontalLayout_4.addWidget(self.addGrounding)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.addFlavour = QtWidgets.QPlainTextEdit(parent=self.horizontalLayoutWidget_11)
        self.addFlavour.setObjectName("addFlavour")
        self.horizontalLayout_5.addWidget(self.addFlavour)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.addPrice = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.addPrice.setObjectName("addPrice")
        self.horizontalLayout_13.addWidget(self.addPrice)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.addVolume = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.addVolume.setObjectName("addVolume")
        self.horizontalLayout_14.addWidget(self.addVolume)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.addButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_11)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_2.addWidget(self.addButton)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.redactId = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.redactId.setObjectName("redactId")
        self.horizontalLayout_10.addWidget(self.redactId)
        self.loadButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_11)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout_10.addWidget(self.loadButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.redactName = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.redactName.setObjectName("redactName")
        self.horizontalLayout_9.addWidget(self.redactName)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.redactRoasting = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.redactRoasting.setObjectName("redactRoasting")
        self.horizontalLayout_8.addWidget(self.redactRoasting)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.redactGrounding = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.redactGrounding.setObjectName("redactGrounding")
        self.horizontalLayout_7.addWidget(self.redactGrounding)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.redactFlavour = QtWidgets.QPlainTextEdit(parent=self.horizontalLayoutWidget_11)
        self.redactFlavour.setObjectName("redactFlavour")
        self.horizontalLayout_6.addWidget(self.redactFlavour)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_14 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_12.addWidget(self.label_14)
        self.redactPrice = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.redactPrice.setObjectName("redactPrice")
        self.horizontalLayout_12.addWidget(self.redactPrice)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.redactVolume = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_11)
        self.redactVolume.setObjectName("redactVolume")
        self.horizontalLayout_15.addWidget(self.redactVolume)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.redactButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_11)
        self.redactButton.setObjectName("redactButton")
        self.verticalLayout_3.addWidget(self.redactButton)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.error_label = QtWidgets.QLabel(parent=Form)
        self.error_label.setGeometry(QtCore.QRect(10, 566, 251, 20))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Добавить кофе"))
        self.label_3.setText(_translate("Form", "ID"))
        self.label_4.setText(_translate("Form", "Название сорта"))
        self.label_5.setText(_translate("Form", "Степень обжарки (1-5)"))
        self.label_6.setText(_translate("Form", "Молотый/в зернах"))
        self.label_7.setText(_translate("Form", "Описание вкуса"))
        self.label_13.setText(_translate("Form", "Цена"))
        self.label_15.setText(_translate("Form", "Объем упаковки"))
        self.addButton.setText(_translate("Form", "Добавить"))
        self.label_2.setText(_translate("Form", "Редактировать кофе"))
        self.label_12.setText(_translate("Form", "ID"))
        self.loadButton.setText(_translate("Form", "Загрузить данные"))
        self.label_11.setText(_translate("Form", "Название сорта"))
        self.label_10.setText(_translate("Form", "Степень обжарки (1-5)"))
        self.label_9.setText(_translate("Form", "Молотый/в зернах"))
        self.label_8.setText(_translate("Form", "Описание вкуса"))
        self.label_14.setText(_translate("Form", "Цена"))
        self.label_16.setText(_translate("Form", "Объем упаковки"))
        self.redactButton.setText(_translate("Form", "Сохранить изменения"))
