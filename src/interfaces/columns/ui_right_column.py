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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
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
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setMidLineWidth(0)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.exportar_layout = QVBoxLayout()
        self.exportar_layout.setObjectName(u"exportar_layout")

        self.verticalLayout.addLayout(self.exportar_layout)

        self.excel_check = QCheckBox(self.menu_1)
        self.excel_check.setObjectName(u"excel_check")
        self.excel_check.setMinimumSize(QSize(200, 0))
        self.excel_check.setMaximumSize(QSize(200, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.excel_check.setFont(font1)
        self.excel_check.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.excel_check)

        self.pdf_check = QCheckBox(self.menu_1)
        self.pdf_check.setObjectName(u"pdf_check")
        self.pdf_check.setMinimumSize(QSize(200, 0))
        self.pdf_check.setMaximumSize(QSize(200, 30))
        self.pdf_check.setFont(font1)

        self.verticalLayout.addWidget(self.pdf_check)

        self.frame = QFrame(self.menu_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

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
        self.return_layout = QVBoxLayout()
        self.return_layout.setObjectName(u"return_layout")

        self.verticalLayout_2.addLayout(self.return_layout)

        self.widget = QWidget(self.menu_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 200))
        self.verticalLayoutWidget_2 = QWidget(self.widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 10, 220, 175))
        self.comment_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.comment_layout.setObjectName(u"comment_layout")
        self.comment_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.widget)

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
        self.excel_check.setText(QCoreApplication.translate("RightColumn", u"Excel", None))
        self.pdf_check.setText(QCoreApplication.translate("RightColumn", u"PDF", None))
    # retranslateUi

