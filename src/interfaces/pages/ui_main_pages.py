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
        MainPages.resize(864, 709)
        self.verticalLayout_3 = QVBoxLayout(MainPages)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
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
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setSpacing(18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.teory_col1 = QVBoxLayout()
        self.teory_col1.setObjectName(u"teory_col1")
        self.title_section1 = QLabel(self.page_2)
        self.title_section1.setObjectName(u"title_section1")
        self.title_section1.setMinimumSize(QSize(0, 60))
        self.title_section1.setMaximumSize(QSize(16777215, 60))
        self.title_section1.setFont(font1)
        self.title_section1.setStyleSheet(u"font: 18pt \"Segoe UI\";")

        self.teory_col1.addWidget(self.title_section1, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.scroll_area_gen = QScrollArea(self.page_2)
        self.scroll_area_gen.setObjectName(u"scroll_area_gen")
        self.scroll_area_gen.setStyleSheet(u"background: transparent;")
        self.scroll_area_gen.setFrameShape(QFrame.NoFrame)
        self.scroll_area_gen.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_gen.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_gen.setWidgetResizable(True)
        self.contents_2 = QWidget()
        self.contents_2.setObjectName(u"contents_2")
        self.contents_2.setGeometry(QRect(0, 0, 277, 847))
        self.contents_2.setStyleSheet(u"background: transparent;")
        self.verticalLayout_5 = QVBoxLayout(self.contents_2)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.t_eslabon = QLabel(self.contents_2)
        self.t_eslabon.setObjectName(u"t_eslabon")
        self.t_eslabon.setMinimumSize(QSize(0, 35))
        self.t_eslabon.setMaximumSize(QSize(16777215, 35))
        self.t_eslabon.setStyleSheet(u"font-size: 12pt")

        self.verticalLayout_5.addWidget(self.t_eslabon, 0, Qt.AlignHCenter)

        self.description_eslabon = QLabel(self.contents_2)
        self.description_eslabon.setObjectName(u"description_eslabon")
        self.description_eslabon.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.description_eslabon.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.description_eslabon)

        self.t_grashof = QLabel(self.contents_2)
        self.t_grashof.setObjectName(u"t_grashof")
        self.t_grashof.setMinimumSize(QSize(0, 35))
        self.t_grashof.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setPointSize(12)
        self.t_grashof.setFont(font2)
        self.t_grashof.setStyleSheet(u"font-size: 12pt")
        self.t_grashof.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.t_grashof)

        self.description_grashof = QLabel(self.contents_2)
        self.description_grashof.setObjectName(u"description_grashof")
        self.description_grashof.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.description_grashof.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.description_grashof)

        self.img_grashof = QLabel(self.contents_2)
        self.img_grashof.setObjectName(u"img_grashof")
        self.img_grashof.setMinimumSize(QSize(190, 140))
        self.img_grashof.setMaximumSize(QSize(190, 140))
        font3 = QFont()
        font3.setPointSize(16)
        self.img_grashof.setFont(font3)
        self.img_grashof.setStyleSheet(u"font-size: 16pt")
        self.img_grashof.setPixmap(QPixmap(u"C:/Users/Usuario/Downloads/tmm_images/grashof.jpg"))
        self.img_grashof.setScaledContents(True)
        self.img_grashof.setAlignment(Qt.AlignCenter)
        self.img_grashof.setOpenExternalLinks(False)

        self.verticalLayout_5.addWidget(self.img_grashof, 0, Qt.AlignHCenter)

        self.description_label_2 = QLabel(self.contents_2)
        self.description_label_2.setObjectName(u"description_label_2")
        self.description_label_2.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.description_label_2.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.description_label_2)

        self.t_4bar = QLabel(self.contents_2)
        self.t_4bar.setObjectName(u"t_4bar")
        self.t_4bar.setMinimumSize(QSize(0, 35))
        self.t_4bar.setMaximumSize(QSize(16777215, 35))
        self.t_4bar.setFont(font2)
        self.t_4bar.setStyleSheet(u"font-size: 12pt")
        self.t_4bar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.t_4bar)

        self.description_4bar = QLabel(self.contents_2)
        self.description_4bar.setObjectName(u"description_4bar")
        self.description_4bar.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.description_4bar.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.description_4bar)

        self.img_mecanismo = QLabel(self.contents_2)
        self.img_mecanismo.setObjectName(u"img_mecanismo")
        self.img_mecanismo.setEnabled(True)
        self.img_mecanismo.setMinimumSize(QSize(267, 200))
        self.img_mecanismo.setMaximumSize(QSize(267, 200))
        self.img_mecanismo.setFont(font3)
        self.img_mecanismo.setStyleSheet(u"font-size: 16pt")
        self.img_mecanismo.setPixmap(QPixmap(u"C:/Users/Usuario/Downloads/tmm_images/mecanism.png"))
        self.img_mecanismo.setScaledContents(True)
        self.img_mecanismo.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.img_mecanismo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.scroll_area_gen.setWidget(self.contents_2)

        self.teory_col1.addWidget(self.scroll_area_gen)


        self.horizontalLayout_2.addLayout(self.teory_col1)

        self.teory_col2 = QVBoxLayout()
        self.teory_col2.setObjectName(u"teory_col2")
        self.scroll_area_vel = QScrollArea(self.page_2)
        self.scroll_area_vel.setObjectName(u"scroll_area_vel")
        self.scroll_area_vel.setStyleSheet(u"background: transparent;")
        self.scroll_area_vel.setFrameShape(QFrame.NoFrame)
        self.scroll_area_vel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_vel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_vel.setWidgetResizable(True)
        self.contents_pos = QWidget()
        self.contents_pos.setObjectName(u"contents_pos")
        self.contents_pos.setGeometry(QRect(0, 0, 263, 687))
        self.contents_pos.setStyleSheet(u"background: transparent;")
        self.verticalLayout_4 = QVBoxLayout(self.contents_pos)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.title_section2 = QLabel(self.contents_pos)
        self.title_section2.setObjectName(u"title_section2")
        self.title_section2.setMinimumSize(QSize(0, 60))
        self.title_section2.setMaximumSize(QSize(16777215, 60))
        self.title_section2.setStyleSheet(u"font: 18pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.title_section2, 0, Qt.AlignHCenter)

        self.title_label_2 = QLabel(self.contents_pos)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setMinimumSize(QSize(0, 35))
        self.title_label_2.setMaximumSize(QSize(16777215, 35))
        self.title_label_2.setFont(font2)
        self.title_label_2.setStyleSheet(u"font-size: 12pt")
        self.title_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.title_label_2)

        self.description_label_3 = QLabel(self.contents_pos)
        self.description_label_3.setObjectName(u"description_label_3")
        self.description_label_3.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.description_label_3.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.description_label_3)

        self.row_1_layout_2 = QHBoxLayout()
        self.row_1_layout_2.setObjectName(u"row_1_layout_2")

        self.verticalLayout_4.addLayout(self.row_1_layout_2)

        self.row_2_layout_2 = QHBoxLayout()
        self.row_2_layout_2.setObjectName(u"row_2_layout_2")

        self.verticalLayout_4.addLayout(self.row_2_layout_2)

        self.row_3_layout_2 = QHBoxLayout()
        self.row_3_layout_2.setObjectName(u"row_3_layout_2")

        self.verticalLayout_4.addLayout(self.row_3_layout_2)

        self.row_4_layout_2 = QVBoxLayout()
        self.row_4_layout_2.setObjectName(u"row_4_layout_2")

        self.verticalLayout_4.addLayout(self.row_4_layout_2)

        self.row_5_layout_2 = QVBoxLayout()
        self.row_5_layout_2.setObjectName(u"row_5_layout_2")

        self.verticalLayout_4.addLayout(self.row_5_layout_2)

        self.scroll_area_vel.setWidget(self.contents_pos)

        self.teory_col2.addWidget(self.scroll_area_vel)


        self.horizontalLayout_2.addLayout(self.teory_col2)

        self.teory_col3 = QVBoxLayout()
        self.teory_col3.setObjectName(u"teory_col3")
        self.scroll_area_vel_2 = QScrollArea(self.page_2)
        self.scroll_area_vel_2.setObjectName(u"scroll_area_vel_2")
        self.scroll_area_vel_2.setStyleSheet(u"background: transparent;")
        self.scroll_area_vel_2.setFrameShape(QFrame.NoFrame)
        self.scroll_area_vel_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_vel_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_vel_2.setWidgetResizable(True)
        self.contents_3 = QWidget()
        self.contents_3.setObjectName(u"contents_3")
        self.contents_3.setGeometry(QRect(0, 0, 262, 687))
        self.contents_3.setStyleSheet(u"background: transparent;")
        self.verticalLayout_6 = QVBoxLayout(self.contents_3)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.title_section3 = QLabel(self.contents_3)
        self.title_section3.setObjectName(u"title_section3")
        self.title_section3.setMinimumSize(QSize(0, 60))
        self.title_section3.setMaximumSize(QSize(16777215, 60))
        self.title_section3.setStyleSheet(u"font: 18pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.title_section3, 0, Qt.AlignHCenter)

        self.title_label_3 = QLabel(self.contents_3)
        self.title_label_3.setObjectName(u"title_label_3")
        self.title_label_3.setMinimumSize(QSize(0, 35))
        self.title_label_3.setMaximumSize(QSize(16777215, 35))
        self.title_label_3.setFont(font2)
        self.title_label_3.setStyleSheet(u"font-size: 12pt")
        self.title_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.title_label_3)

        self.description_label_4 = QLabel(self.contents_3)
        self.description_label_4.setObjectName(u"description_label_4")
        self.description_label_4.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.description_label_4.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.description_label_4)

        self.row_1_layout_4 = QHBoxLayout()
        self.row_1_layout_4.setObjectName(u"row_1_layout_4")

        self.verticalLayout_6.addLayout(self.row_1_layout_4)

        self.row_3_layout_3 = QHBoxLayout()
        self.row_3_layout_3.setObjectName(u"row_3_layout_3")

        self.verticalLayout_6.addLayout(self.row_3_layout_3)

        self.row_2_layout_4 = QHBoxLayout()
        self.row_2_layout_4.setObjectName(u"row_2_layout_4")

        self.verticalLayout_6.addLayout(self.row_2_layout_4)

        self.row_3_layout_4 = QHBoxLayout()
        self.row_3_layout_4.setObjectName(u"row_3_layout_4")

        self.verticalLayout_6.addLayout(self.row_3_layout_4)

        self.row_4_layout_4 = QVBoxLayout()
        self.row_4_layout_4.setObjectName(u"row_4_layout_4")

        self.verticalLayout_6.addLayout(self.row_4_layout_4)

        self.row_5_layout_4 = QVBoxLayout()
        self.row_5_layout_4.setObjectName(u"row_5_layout_4")

        self.verticalLayout_6.addLayout(self.row_5_layout_4)

        self.scroll_area_vel_2.setWidget(self.contents_3)

        self.teory_col3.addWidget(self.scroll_area_vel_2)


        self.horizontalLayout_2.addLayout(self.teory_col3)

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
        self.contents.setGeometry(QRect(0, 0, 214, 266))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        self.title_label.setFont(font3)
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

        self.verticalLayout_3.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.name_app.setText(QCoreApplication.translate("MainPages", u"Plataforma Educativa de Mecanismos Simples", None))
        self.Subtitle.setText(QCoreApplication.translate("MainPages", u"An\u00e1lisis de Posici\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Empezando", None))
        self.pie.setText("")
        self.title_section1.setText(QCoreApplication.translate("MainPages", u"Conceptos Generales", None))
        self.t_eslabon.setText(QCoreApplication.translate("MainPages", u"Eslabones y Juntas", None))
        self.description_eslabon.setText(QCoreApplication.translate("MainPages", u"Un eslab\u00f3n es un cuerpo r\u00edgido que posee por lo menos 2 nodos por los cuales se une a otros eslabones.\n"
"Una junta es una conexi\u00f3n entre dos o m\u00e1s eslabones, la cual permite alg\u00fan movimiento", None))
        self.t_grashof.setText(QCoreApplication.translate("MainPages", u"Condici\u00f3n de Grashof", None))
        self.description_grashof.setText(QCoreApplication.translate("MainPages", u"Es una relaci\u00f3n que predice el comportamiento de rotaci\u00f3n o rotabilidad de las inversiones de un mecanismo de cuatro barras basado s\u00f3lo en las longitudes de los eslabones.", None))
        self.img_grashof.setText("")
        self.description_label_2.setText(QCoreApplication.translate("MainPages", u"De cumplirse la condici\u00f3n, el eslabonamiento es de Grashof y por lo menos un eslab\u00f3n ser\u00e1 capaz de realizar una revoluci\u00f3n completa con respecto al plano de bancada.", None))
        self.t_4bar.setText(QCoreApplication.translate("MainPages", u"Mecanismo de cuatro barras", None))
        self.description_4bar.setText(QCoreApplication.translate("MainPages", u"Es un mecanismo plano compuesto por 4 s\u00f3lidos r\u00edgidos conectados entre s\u00ed mediante 4 pares cinem\u00e1ticos de revoluci\u00f3n. Usualmente uno de los s\u00f3lidos est\u00e1 fijo durante su movimiento.", None))
        self.img_mecanismo.setText("")
        self.title_section2.setText(QCoreApplication.translate("MainPages", u"An\u00e1lisis de Posici\u00f3n", None))
        self.title_label_2.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label_3.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.title_section3.setText(QCoreApplication.translate("MainPages", u"An\u00e1lisis de Velocidad", None))
        self.title_label_3.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label_4.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
    # retranslateUi

