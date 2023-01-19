# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_column.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(679, 600)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.theme_Layout = QHBoxLayout()
        self.theme_Layout.setObjectName(u"theme_Layout")

        self.verticalLayout.addLayout(self.theme_Layout)

        self.sizetext_Layout = QHBoxLayout()
        self.sizetext_Layout.setObjectName(u"sizetext_Layout")

        self.verticalLayout.addLayout(self.sizetext_Layout)

        self.name_Layout = QVBoxLayout()
        self.name_Layout.setObjectName(u"name_Layout")

        self.verticalLayout.addLayout(self.name_Layout)

        self.dir_Layout = QVBoxLayout()
        self.dir_Layout.setObjectName(u"dir_Layout")

        self.verticalLayout.addLayout(self.dir_Layout)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.menu_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(220, 0))
        self.label_3.setMaximumSize(QSize(220, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font-size: 10pt")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(-1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.btn_doc = QWidget(self.menu_2)
        self.btn_doc.setObjectName(u"btn_doc")
        self.btn_doc.setMinimumSize(QSize(0, 40))
        self.btn_doc.setMaximumSize(QSize(16777215, 40))
        self.btn_4_layout = QVBoxLayout(self.btn_doc)
        self.btn_4_layout.setSpacing(0)
        self.btn_4_layout.setObjectName(u"btn_4_layout")
        self.btn_4_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_doc)

        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 10pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("LeftColumn", u" El presente producto es una herramienta software desarrollada por un grupo de estudiantes de la Universidad Nacional de Trujillo con la finalidad de facilitar a los nuevos estudiantes la parte operativa al realizar el an\u00e1lisis de Posici\u00f3n de Mecanismos de 4 Barras. Si usted es nuevo en la aplicaci\u00f3n, sientase libre de revisar la documentaci\u00f3n que se adjunta debajo.", None))
        self.label_2.setText("")
    # retranslateUi

