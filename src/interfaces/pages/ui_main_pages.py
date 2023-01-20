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
        MainPages.resize(864, 833)
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
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.title_section1.setFont(font2)
        self.title_section1.setStyleSheet(u"font: 20pt \"Segoe UI\";")

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
        self.contents_2.setGeometry(QRect(0, 0, 277, 1110))
        self.contents_2.setStyleSheet(u"background: transparent;")
        self.verticalLayout_5 = QVBoxLayout(self.contents_2)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.t_eslabon = QLabel(self.contents_2)
        self.t_eslabon.setObjectName(u"t_eslabon")
        self.t_eslabon.setMinimumSize(QSize(0, 35))
        self.t_eslabon.setMaximumSize(QSize(16777215, 35))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        self.t_eslabon.setFont(font3)
        self.t_eslabon.setStyleSheet(u"font-size: 16pt")

        self.verticalLayout_5.addWidget(self.t_eslabon, 0, Qt.AlignHCenter)

        self.description_layout = QVBoxLayout()
        self.description_layout.setObjectName(u"description_layout")

        self.verticalLayout_5.addLayout(self.description_layout)

        self.frame_eslabon = QFrame(self.contents_2)
        self.frame_eslabon.setObjectName(u"frame_eslabon")
        self.frame_eslabon.setMinimumSize(QSize(220, 300))
        self.frame_eslabon.setMaximumSize(QSize(220, 300))
        self.frame_eslabon.setFrameShape(QFrame.StyledPanel)
        self.frame_eslabon.setFrameShadow(QFrame.Raised)
        self.layoutWidget_5 = QWidget(self.frame_eslabon)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(0, 0, 221, 291))
        self.eslabon_layout = QVBoxLayout(self.layoutWidget_5)
        self.eslabon_layout.setObjectName(u"eslabon_layout")
        self.eslabon_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_eslabon, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.t_grubler = QLabel(self.contents_2)
        self.t_grubler.setObjectName(u"t_grubler")
        self.t_grubler.setMinimumSize(QSize(0, 35))
        self.t_grubler.setMaximumSize(QSize(16777215, 35))
        font4 = QFont()
        font4.setPointSize(16)
        self.t_grubler.setFont(font4)
        self.t_grubler.setStyleSheet(u"font-size: 16pt")
        self.t_grubler.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.t_grubler)

        self.desc_gruebler_layout = QVBoxLayout()
        self.desc_gruebler_layout.setObjectName(u"desc_gruebler_layout")

        self.verticalLayout_5.addLayout(self.desc_gruebler_layout)

        self.frame_gruebler = QFrame(self.contents_2)
        self.frame_gruebler.setObjectName(u"frame_gruebler")
        self.frame_gruebler.setMinimumSize(QSize(235, 100))
        self.frame_gruebler.setMaximumSize(QSize(235, 100))
        self.frame_gruebler.setFrameShape(QFrame.StyledPanel)
        self.frame_gruebler.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.frame_gruebler)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 0, 231, 101))
        self.gruebler_layout = QVBoxLayout(self.layoutWidget_4)
        self.gruebler_layout.setObjectName(u"gruebler_layout")
        self.gruebler_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_gruebler, 0, Qt.AlignHCenter)

        self.t_4bar = QLabel(self.contents_2)
        self.t_4bar.setObjectName(u"t_4bar")
        self.t_4bar.setMinimumSize(QSize(0, 35))
        self.t_4bar.setMaximumSize(QSize(16777215, 35))
        self.t_4bar.setFont(font4)
        self.t_4bar.setStyleSheet(u"font-size: 16pt")
        self.t_4bar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.t_4bar)

        self.mecanismo4_layout = QVBoxLayout()
        self.mecanismo4_layout.setObjectName(u"mecanismo4_layout")

        self.verticalLayout_5.addLayout(self.mecanismo4_layout)

        self.frame_mecanismo = QFrame(self.contents_2)
        self.frame_mecanismo.setObjectName(u"frame_mecanismo")
        self.frame_mecanismo.setMinimumSize(QSize(267, 200))
        self.frame_mecanismo.setMaximumSize(QSize(267, 200))
        self.frame_mecanismo.setFrameShape(QFrame.StyledPanel)
        self.frame_mecanismo.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame_mecanismo)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 10, 261, 181))
        self.mecanismo_layout = QVBoxLayout(self.layoutWidget_2)
        self.mecanismo_layout.setObjectName(u"mecanismo_layout")
        self.mecanismo_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_mecanismo, 0, Qt.AlignHCenter)

        self.t_grashof = QLabel(self.contents_2)
        self.t_grashof.setObjectName(u"t_grashof")
        self.t_grashof.setMinimumSize(QSize(0, 35))
        self.t_grashof.setMaximumSize(QSize(16777215, 35))
        self.t_grashof.setFont(font4)
        self.t_grashof.setStyleSheet(u"font-size: 16pt")
        self.t_grashof.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.t_grashof)

        self.desc_grashof_layout = QVBoxLayout()
        self.desc_grashof_layout.setObjectName(u"desc_grashof_layout")

        self.verticalLayout_5.addLayout(self.desc_grashof_layout)

        self.frame_grashof = QFrame(self.contents_2)
        self.frame_grashof.setObjectName(u"frame_grashof")
        self.frame_grashof.setMinimumSize(QSize(220, 170))
        self.frame_grashof.setMaximumSize(QSize(220, 170))
        self.frame_grashof.setFrameShape(QFrame.StyledPanel)
        self.frame_grashof.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.frame_grashof)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 0, 221, 161))
        self.grashof_layout = QVBoxLayout(self.layoutWidget_3)
        self.grashof_layout.setObjectName(u"grashof_layout")
        self.grashof_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_grashof, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.grashof2_layout = QVBoxLayout()
        self.grashof2_layout.setObjectName(u"grashof2_layout")

        self.verticalLayout_5.addLayout(self.grashof2_layout)

        self.scroll_area_gen.setWidget(self.contents_2)

        self.teory_col1.addWidget(self.scroll_area_gen)


        self.horizontalLayout_2.addLayout(self.teory_col1)

        self.teory_col2 = QVBoxLayout()
        self.teory_col2.setObjectName(u"teory_col2")
        self.scroll_area_pos = QScrollArea(self.page_2)
        self.scroll_area_pos.setObjectName(u"scroll_area_pos")
        self.scroll_area_pos.setStyleSheet(u"background: transparent;")
        self.scroll_area_pos.setFrameShape(QFrame.NoFrame)
        self.scroll_area_pos.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_pos.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_pos.setWidgetResizable(True)
        self.contents_pos = QWidget()
        self.contents_pos.setObjectName(u"contents_pos")
        self.contents_pos.setGeometry(QRect(0, 0, 299, 811))
        self.contents_pos.setStyleSheet(u"background: transparent;")
        self.verticalLayout_4 = QVBoxLayout(self.contents_pos)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.title_section2 = QLabel(self.contents_pos)
        self.title_section2.setObjectName(u"title_section2")
        self.title_section2.setMinimumSize(QSize(0, 60))
        self.title_section2.setMaximumSize(QSize(16777215, 60))
        self.title_section2.setStyleSheet(u"font: 20pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.title_section2, 0, Qt.AlignHCenter)

        self.t_position = QLabel(self.contents_pos)
        self.t_position.setObjectName(u"t_position")
        self.t_position.setMinimumSize(QSize(0, 35))
        self.t_position.setMaximumSize(QSize(16777215, 35))
        self.t_position.setFont(font4)
        self.t_position.setStyleSheet(u"font-size: 16pt")
        self.t_position.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.t_position)

        self.pos_layout = QVBoxLayout()
        self.pos_layout.setObjectName(u"pos_layout")

        self.verticalLayout_4.addLayout(self.pos_layout)

        self.t_grashof_2 = QLabel(self.contents_pos)
        self.t_grashof_2.setObjectName(u"t_grashof_2")
        self.t_grashof_2.setMinimumSize(QSize(0, 35))
        self.t_grashof_2.setMaximumSize(QSize(16777215, 35))
        self.t_grashof_2.setFont(font4)
        self.t_grashof_2.setStyleSheet(u"font-size: 16pt")
        self.t_grashof_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.t_grashof_2)

        self.pos_analysis_layout = QVBoxLayout()
        self.pos_analysis_layout.setObjectName(u"pos_analysis_layout")

        self.verticalLayout_4.addLayout(self.pos_analysis_layout)

        self.widget_2 = QWidget(self.contents_pos)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(267, 0))
        self.widget_2.setMaximumSize(QSize(267, 16777215))
        self.Ec_pos_layout = QVBoxLayout(self.widget_2)
        self.Ec_pos_layout.setObjectName(u"Ec_pos_layout")

        self.verticalLayout_4.addWidget(self.widget_2)

        self.scroll_area_pos.setWidget(self.contents_pos)

        self.teory_col2.addWidget(self.scroll_area_pos)


        self.horizontalLayout_2.addLayout(self.teory_col2)

        self.teory_col3 = QVBoxLayout()
        self.teory_col3.setObjectName(u"teory_col3")
        self.scroll_area_vel = QScrollArea(self.page_2)
        self.scroll_area_vel.setObjectName(u"scroll_area_vel")
        self.scroll_area_vel.setStyleSheet(u"background: transparent;")
        self.scroll_area_vel.setFrameShape(QFrame.NoFrame)
        self.scroll_area_vel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_vel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_vel.setWidgetResizable(True)
        self.contents_3 = QWidget()
        self.contents_3.setObjectName(u"contents_3")
        self.contents_3.setGeometry(QRect(0, 0, 277, 811))
        self.contents_3.setStyleSheet(u"background: transparent;")
        self.verticalLayout_6 = QVBoxLayout(self.contents_3)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.title_section3 = QLabel(self.contents_3)
        self.title_section3.setObjectName(u"title_section3")
        self.title_section3.setMinimumSize(QSize(0, 60))
        self.title_section3.setMaximumSize(QSize(16777215, 60))
        self.title_section3.setStyleSheet(u"font: 20pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.title_section3, 0, Qt.AlignHCenter)

        self.title_label_3 = QLabel(self.contents_3)
        self.title_label_3.setObjectName(u"title_label_3")
        self.title_label_3.setMinimumSize(QSize(0, 35))
        self.title_label_3.setMaximumSize(QSize(16777215, 35))
        self.title_label_3.setFont(font4)
        self.title_label_3.setStyleSheet(u"font-size: 16pt")
        self.title_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.title_label_3)

        self.vel_analysis_layout = QVBoxLayout()
        self.vel_analysis_layout.setObjectName(u"vel_analysis_layout")

        self.verticalLayout_6.addLayout(self.vel_analysis_layout)

        self.widget_3 = QWidget(self.contents_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(267, 0))
        self.widget_3.setMaximumSize(QSize(267, 16777215))
        self.Ec_vel_layout = QVBoxLayout(self.widget_3)
        self.Ec_vel_layout.setObjectName(u"Ec_vel_layout")

        self.verticalLayout_6.addWidget(self.widget_3)

        self.scroll_area_vel.setWidget(self.contents_3)

        self.teory_col3.addWidget(self.scroll_area_vel)


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
        self.contents.setGeometry(QRect(0, 0, 844, 813))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.Initial_layout = QHBoxLayout()
        self.Initial_layout.setObjectName(u"Initial_layout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.graph_layout = QVBoxLayout()
        self.graph_layout.setObjectName(u"graph_layout")

        self.verticalLayout_8.addLayout(self.graph_layout)

        self.cond_grashof_layout = QHBoxLayout()
        self.cond_grashof_layout.setObjectName(u"cond_grashof_layout")
        self.label_14 = QLabel(self.contents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(80, 30))
        self.label_14.setMaximumSize(QSize(80, 30))
        self.label_14.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.cond_grashof_layout.addWidget(self.label_14, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_8.addLayout(self.cond_grashof_layout)


        self.Initial_layout.addLayout(self.verticalLayout_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.parameters = QVBoxLayout()
        self.parameters.setObjectName(u"parameters")
        self.title_section3_2 = QLabel(self.contents)
        self.title_section3_2.setObjectName(u"title_section3_2")
        self.title_section3_2.setMinimumSize(QSize(0, 50))
        self.title_section3_2.setMaximumSize(QSize(16777215, 50))
        self.title_section3_2.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"border :2px solid;\n"
"border-color: rgb(108, 153, 244);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius : 5px; \n"
"border-bottom-left-radius : 5px; \n"
"border-bottom-right-radius : 5px;")
        self.title_section3_2.setAlignment(Qt.AlignCenter)

        self.parameters.addWidget(self.title_section3_2)

        self.O2_layout = QHBoxLayout()
        self.O2_layout.setObjectName(u"O2_layout")
        self.label_7 = QLabel(self.contents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 30))
        self.label_7.setMaximumSize(QSize(80, 30))
        self.label_7.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.O2_layout.addWidget(self.label_7, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.parameters.addLayout(self.O2_layout)

        self.O4_layout = QHBoxLayout()
        self.O4_layout.setObjectName(u"O4_layout")
        self.label_8 = QLabel(self.contents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 30))
        self.label_8.setMaximumSize(QSize(80, 30))
        self.label_8.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.O4_layout.addWidget(self.label_8, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.parameters.addLayout(self.O4_layout)

        self.Eslabon_layout2 = QHBoxLayout()
        self.Eslabon_layout2.setObjectName(u"Eslabon_layout2")
        self.label_3 = QLabel(self.contents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 30))
        self.label_3.setMaximumSize(QSize(80, 30))
        self.label_3.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.Eslabon_layout2.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.parameters.addLayout(self.Eslabon_layout2)

        self.Eslabon_layout3 = QHBoxLayout()
        self.Eslabon_layout3.setObjectName(u"Eslabon_layout3")
        self.label_4 = QLabel(self.contents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 30))
        self.label_4.setMaximumSize(QSize(80, 30))
        self.label_4.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.Eslabon_layout3.addWidget(self.label_4, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.parameters.addLayout(self.Eslabon_layout3)

        self.Eslabon_layout4 = QHBoxLayout()
        self.Eslabon_layout4.setObjectName(u"Eslabon_layout4")
        self.label_5 = QLabel(self.contents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 30))
        self.label_5.setMaximumSize(QSize(80, 30))
        self.label_5.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.Eslabon_layout4.addWidget(self.label_5, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.parameters.addLayout(self.Eslabon_layout4)

        self.PointP_layout = QHBoxLayout()
        self.PointP_layout.setObjectName(u"PointP_layout")
        self.P_layout = QHBoxLayout()
        self.P_layout.setObjectName(u"P_layout")
        self.label_11 = QLabel(self.contents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(30, 30))
        self.label_11.setMaximumSize(QSize(30, 30))
        self.label_11.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.P_layout.addWidget(self.label_11, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.PointP_layout.addLayout(self.P_layout)

        self.delta3_layout = QHBoxLayout()
        self.delta3_layout.setObjectName(u"delta3_layout")
        self.label_12 = QLabel(self.contents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(30, 30))
        self.label_12.setMaximumSize(QSize(30, 30))
        self.label_12.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.delta3_layout.addWidget(self.label_12, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.PointP_layout.addLayout(self.delta3_layout)


        self.parameters.addLayout(self.PointP_layout)

        self.other_layout = QHBoxLayout()
        self.other_layout.setObjectName(u"other_layout")
        self.theta2_layout = QHBoxLayout()
        self.theta2_layout.setObjectName(u"theta2_layout")
        self.label_9 = QLabel(self.contents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(30, 30))
        self.label_9.setMaximumSize(QSize(30, 30))
        self.label_9.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.theta2_layout.addWidget(self.label_9, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.other_layout.addLayout(self.theta2_layout)

        self.velocity_layout = QHBoxLayout()
        self.velocity_layout.setObjectName(u"velocity_layout")
        self.label_10 = QLabel(self.contents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(30, 30))
        self.label_10.setMaximumSize(QSize(30, 30))
        self.label_10.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.velocity_layout.addWidget(self.label_10, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.other_layout.addLayout(self.velocity_layout)

        self.aceleration_layout = QHBoxLayout()
        self.aceleration_layout.setObjectName(u"aceleration_layout")
        self.label_13 = QLabel(self.contents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(30, 30))
        self.label_13.setMaximumSize(QSize(30, 30))
        self.label_13.setStyleSheet(u"border :2px solid;\n"
"border-color: rgb(30, 34, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius : 8px; \n"
"border-bottom-left-radius : 8px; \n"
"border-bottom-right-radius : 8px;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.aceleration_layout.addWidget(self.label_13, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.other_layout.addLayout(self.aceleration_layout)


        self.parameters.addLayout(self.other_layout)

        self.play_layout = QVBoxLayout()
        self.play_layout.setObjectName(u"play_layout")

        self.parameters.addLayout(self.play_layout)


        self.horizontalLayout.addLayout(self.parameters)


        self.Initial_layout.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.Initial_layout)

        self.Position_title = QLabel(self.contents)
        self.Position_title.setObjectName(u"Position_title")
        self.Position_title.setMinimumSize(QSize(0, 70))
        self.Position_title.setMaximumSize(QSize(16777215, 70))
        self.Position_title.setFont(font2)
        self.Position_title.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"border :2px solid;\n"
"border-color: rgb(108, 153, 244);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius : 5px; \n"
"border-bottom-left-radius : 5px; \n"
"border-bottom-right-radius : 5px;")
        self.Position_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Position_title)

        self.widget = QWidget(self.contents)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 310))
        self.widget.setMaximumSize(QSize(16777215, 310))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.table1_layout = QHBoxLayout()
        self.table1_layout.setObjectName(u"table1_layout")

        self.horizontalLayout_3.addLayout(self.table1_layout)


        self.verticalLayout.addWidget(self.widget)

        self.scroll_area.setWidget(self.contents)

        self.page_3_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_3)

        self.verticalLayout_3.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.name_app.setText(QCoreApplication.translate("MainPages", u"Plataforma Educativa de Mecanismos Simples", None))
        self.Subtitle.setText(QCoreApplication.translate("MainPages", u"An\u00e1lisis Cinem\u00e1tico de Mecanismos", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Empezando", None))
        self.pie.setText("")
        self.title_section1.setText(QCoreApplication.translate("MainPages", u"Conceptos Generales", None))
        self.t_eslabon.setText(QCoreApplication.translate("MainPages", u"Eslabones y Juntas", None))
        self.t_grubler.setText(QCoreApplication.translate("MainPages", u"La ecuaci\u00f3n de Gruebler", None))
        self.t_4bar.setText(QCoreApplication.translate("MainPages", u"Mecanismo de cuatro barras", None))
        self.t_grashof.setText(QCoreApplication.translate("MainPages", u"Condici\u00f3n de Grashof", None))
        self.title_section2.setText(QCoreApplication.translate("MainPages", u"An\u00e1lisis de Posici\u00f3n", None))
        self.t_position.setText(QCoreApplication.translate("MainPages", u"Posici\u00f3n", None))
        self.t_grashof_2.setText(QCoreApplication.translate("MainPages", u"\u00bfQu\u00e9 es el an\u00e1lisis de Posici\u00f3n?", None))
        self.title_section3.setText(QCoreApplication.translate("MainPages", u"An\u00e1lisis de Velocidad", None))
        self.title_label_3.setText(QCoreApplication.translate("MainPages", u"Velocidad", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"Cond. Grashof", None))
        self.title_section3_2.setText(QCoreApplication.translate("MainPages", u"Par\u00e1metros", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"O_2", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"O_4", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Eslab\u00f3n 2", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Eslab\u00f3n 3", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Eslab\u00f3n 4", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"\u03b43", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"\u03b82", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"\u03c92", None))
        self.label_13.setText(QCoreApplication.translate("MainPages", u"\u03b12", None))
        self.Position_title.setText(QCoreApplication.translate("MainPages", u"Resultados del an\u00e1lisis cinem\u00e1tico", None))
    # retranslateUi

