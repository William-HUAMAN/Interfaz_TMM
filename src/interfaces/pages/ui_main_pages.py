# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(20)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(20, 20, 20, 20)
        self.name_app = QLabel(self.page_1)
        self.name_app.setObjectName(u"name_app")
        self.name_app.setMinimumSize(QSize(0, 80))
        self.name_app.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.name_app.setFont(font)
        self.name_app.setStyleSheet(u"font: 24pt \"Segoe UI\";")

        self.page_1_layout.addWidget(self.name_app, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.home_Layout = QHBoxLayout()
        self.home_Layout.setSpacing(5)
        self.home_Layout.setObjectName(u"home_Layout")
        self.home_Layout.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Subtitle = QLabel(self.page_1)
        self.Subtitle.setObjectName(u"Subtitle")
        self.Subtitle.setMinimumSize(QSize(0, 60))
        self.Subtitle.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.Subtitle.setFont(font1)
        self.Subtitle.setStyleSheet(u"font: 18pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.Subtitle, 0, Qt.AlignHCenter)

        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setStyleSheet(u"font: 14pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.frame_basics = QFrame(self.page_1)
        self.frame_basics.setObjectName(u"frame_basics")
        self.frame_basics.setMinimumSize(QSize(250, 225))
        self.frame_basics.setMaximumSize(QSize(250, 225))
        self.frame_basics.setFrameShape(QFrame.StyledPanel)
        self.frame_basics.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_basics)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 241, 211))
        self.btns_basics = QVBoxLayout(self.layoutWidget)
        self.btns_basics.setObjectName(u"btns_basics")
        self.btns_basics.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_basics, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.home_Layout.addLayout(self.verticalLayout_2)

        self.frame_logo = QFrame(self.page_1)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMinimumSize(QSize(400, 349))
        self.frame_logo.setMaximumSize(QSize(400, 349))
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame_logo)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(5, 1, 381, 351))
        self.logo_layout = QVBoxLayout(self.layoutWidget1)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.home_Layout.addWidget(self.frame_logo, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.page_1_layout.addLayout(self.home_Layout)

        self.pie = QLabel(self.page_1)
        self.pie.setObjectName(u"pie")
        self.pie.setMinimumSize(QSize(0, 60))
        self.pie.setMaximumSize(QSize(16777215, 60))

        self.page_1_layout.addWidget(self.pie)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 250, 49, 16))
        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setSpacing(5)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_3)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 580))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(16)
        self.title_label.setFont(font2)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_3_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.name_app.setText(QCoreApplication.translate("MainPages", u"Plataforma Educativa de Mecanismos Simples", None))
        self.Subtitle.setText(QCoreApplication.translate("MainPages", u"An\u00e1lisis de Posici\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Empezando", None))
        self.pie.setText("")
        self.label_2.setText(QCoreApplication.translate("MainPages", u"pagina2", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
    # retranslateUi

