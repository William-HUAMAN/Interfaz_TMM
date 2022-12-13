# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'right_column.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.menu_1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setMidLineWidth(0)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.Title_check = QCheckBox(self.menu_1)
        self.Title_check.setObjectName(u"Title_check")
        self.Title_check.setMinimumSize(QSize(200, 0))
        self.Title_check.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.Title_check.setFont(font1)
        self.Title_check.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.Title_check, 0, Qt.AlignHCenter)

        self.checkBox_5 = QCheckBox(self.menu_1)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setMinimumSize(QSize(200, 0))
        self.checkBox_5.setMaximumSize(QSize(200, 16777215))
        self.checkBox_5.setFont(font1)

        self.verticalLayout.addWidget(self.checkBox_5, 0, Qt.AlignHCenter)

        self.Schematic_check = QCheckBox(self.menu_1)
        self.Schematic_check.setObjectName(u"Schematic_check")
        self.Schematic_check.setMinimumSize(QSize(200, 0))
        self.Schematic_check.setMaximumSize(QSize(200, 16777215))
        self.Schematic_check.setFont(font1)

        self.verticalLayout.addWidget(self.Schematic_check, 0, Qt.AlignHCenter)

        self.Table_check = QCheckBox(self.menu_1)
        self.Table_check.setObjectName(u"Table_check")
        self.Table_check.setMinimumSize(QSize(200, 0))
        self.Table_check.setFont(font1)

        self.verticalLayout.addWidget(self.Table_check, 0, Qt.AlignHCenter)

        self.trajectory_check = QCheckBox(self.menu_1)
        self.trajectory_check.setObjectName(u"trajectory_check")
        self.trajectory_check.setMinimumSize(QSize(200, 0))
        self.trajectory_check.setMaximumSize(QSize(200, 16777215))
        self.trajectory_check.setFont(font1)

        self.verticalLayout.addWidget(self.trajectory_check, 0, Qt.AlignHCenter)

        self.File_name_layout = QWidget(self.menu_1)
        self.File_name_layout.setObjectName(u"File_name_layout")
        self.File_name_layout.setMinimumSize(QSize(0, 40))
        self.File_name_layout.setMaximumSize(QSize(16777215, 40))
        self.name_layout = QVBoxLayout(self.File_name_layout)
        self.name_layout.setSpacing(0)
        self.name_layout.setObjectName(u"name_layout")
        self.name_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.File_name_layout)

        self.File_format = QComboBox(self.menu_1)
        self.File_format.addItem("")
        self.File_format.addItem("")
        self.File_format.addItem("")
        self.File_format.addItem("")
        self.File_format.addItem("")
        self.File_format.setObjectName(u"File_format")
        self.File_format.setMinimumSize(QSize(190, 40))
        self.File_format.setMaximumSize(QSize(190, 40))
        self.File_format.setFont(font1)

        self.verticalLayout.addWidget(self.File_format, 0, Qt.AlignHCenter)

        self.btn_exportar = QWidget(self.menu_1)
        self.btn_exportar.setObjectName(u"btn_exportar")
        self.btn_exportar.setMinimumSize(QSize(0, 40))
        self.btn_exportar.setMaximumSize(QSize(16777215, 40))
        self.btn_export_layout = QVBoxLayout(self.btn_exportar)
        self.btn_export_layout.setSpacing(0)
        self.btn_export_layout.setObjectName(u"btn_export_layout")
        self.btn_export_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_exportar)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.btn_return = QWidget(self.menu_2)
        self.btn_return.setObjectName(u"btn_return")
        self.btn_return.setMinimumSize(QSize(0, 40))
        self.btn_return.setMaximumSize(QSize(16777215, 40))
        self.btn_return_layout = QVBoxLayout(self.btn_return)
        self.btn_return_layout.setSpacing(0)
        self.btn_return_layout.setObjectName(u"btn_return_layout")
        self.btn_return_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_return)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.label.setText(QCoreApplication.translate("RightColumn", u"Exportar", None))
        self.Title_check.setText(QCoreApplication.translate("RightColumn", u"T\u00edtulo", None))
        self.checkBox_5.setText(QCoreApplication.translate("RightColumn", u"Condici\u00f3n de Grashof", None))
        self.Schematic_check.setText(QCoreApplication.translate("RightColumn", u"Esquematizaci\u00f3n", None))
        self.Table_check.setText(QCoreApplication.translate("RightColumn", u"Tabla de resultados", None))
        self.trajectory_check.setText(QCoreApplication.translate("RightColumn", u"Gr\u00e1fica de la Trayectoria", None))
        self.File_format.setItemText(0, QCoreApplication.translate("RightColumn", u"Exportar como:", None))
        self.File_format.setItemText(1, QCoreApplication.translate("RightColumn", u"Word", None))
        self.File_format.setItemText(2, QCoreApplication.translate("RightColumn", u"PDF", None))
        self.File_format.setItemText(3, QCoreApplication.translate("RightColumn", u"Excel", None))
        self.File_format.setItemText(4, QCoreApplication.translate("RightColumn", u"Todos", None))

        self.label_2.setText(QCoreApplication.translate("RightColumn", u"Menu 2 - Right Menu", None))
    # retranslateUi

