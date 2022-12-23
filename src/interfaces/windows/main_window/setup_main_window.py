# Importando Librerías necesarias
from src.core.libraries import *

# Importando configuraciones
from src.core.json_settings import Settings  # Archivo JSON de configuraciones
from src.core.json_themes import Themes  # Tema de color seleccionado

# Importando recursos gráficos
from src.widgets.py_table_widget.py_table_widget import PyTableWidget
from .functions_main_window import *
from src.widgets import *
from .ui_main import *  # Cargando la interfaz principal

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from .functions_main_window import *
from src.math.analysis import analyze


# PY WINDOW
# ////////////////////////////////////////////////////////////// 
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        self.analyze_button = None
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Inicio",
            "btn_tooltip": "Página de Inicio",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "icon_books.svg",
            "btn_id": "btn_teory",
            "btn_text": "Fundamento teórico",
            "btn_tooltip": "Mostrar teoría",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_calculadora.svg",
            "btn_id": "btn_calculus",
            "btn_text": "Cálculos del análisis",
            "btn_tooltip": "Cálculos",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_file.svg",
            "btn_id": "btn_new_file",
            "btn_text": "New File",
            "btn_tooltip": "Create new file",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_folder_open.svg",
            "btn_id": "btn_open_file",
            "btn_text": "Open File",
            "btn_tooltip": "Open file",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_save.svg",
            "btn_id": "btn_save",
            "btn_text": "Guardar",
            "btn_tooltip": "Guardar proyecto",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_info",
            "btn_text": "Información",
            "btn_tooltip": "Panel de Información",
            "show_top": False,
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_settings",
            "btn_text": "Ajustes",
            "btn_tooltip": "Abrir ajustes",
            "show_top": False,
            "is_active": False
        }
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon": "icon_search.svg",
            "btn_id": "btn_search",
            "btn_tooltip": "Buscar",
            "is_active": False
        },
        {
            "btn_icon": "icon_export.svg",
            "btn_id": "btn_top_export",
            "btn_tooltip": "Exportar",
            "is_active": False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////
        # BTN Documentation

        self.left_btn_doc = PyPushButton(
            text="Guía de usuario",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_two"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_doc.setMaximumHeight(40)
        self.ui.left_column.menus.btn_4_layout.addWidget(self.left_btn_doc)

        # BTN 1
        self.left_btn_1 = PyPushButton(
            text="Btn 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

        # BTN 2
        self.left_btn_2 = PyPushButton(
            text="Btn With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_2.setIcon(self.icon)
        self.left_btn_2.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        # BTN 3 - Default QPushButton
        self.left_btn_3 = QPushButton("Default QPushButton")
        self.left_btn_3.setMaximumHeight(40)
        self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

        # PAGES
        # ///////////////////////////////////////////////////////////////
        # PAGE 1 - first page
        # new file button
        self.new_file_btn = PyPushButton(
            text=" Crear un Proyecto",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_new_file = QIcon(Functions.set_svg_icon("icon_file.svg"))
        self.new_file_btn.setMinimumHeight(30)
        self.new_file_btn.setIcon(self.icon_new_file)

        self.open_dir_btn = PyPushButton(
            text=" Abrir un Proyecto",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_folder = QIcon(Functions.set_svg_icon("icon_folder_open.svg"))
        self.open_dir_btn.setMinimumHeight(30)
        self.open_dir_btn.setIcon(self.icon_folder)

        self.user_guide_btn = PyPushButton(
            text=" Guía de usuario",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_user_guide = QIcon(Functions.set_svg_icon("icon_restore.svg"))
        self.user_guide_btn.setMinimumHeight(30)
        self.user_guide_btn.setIcon(self.icon_user_guide)

        self.contact_btn = PyPushButton(
            text="  Contáctanos",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_support = QIcon(Functions.set_svg_icon("icon_support.svg"))
        self.contact_btn.setMinimumHeight(30)
        self.contact_btn.setIcon(self.icon_support)

        # Agregando botones básicos
        self.ui.load_pages.btns_basics.addWidget(self.new_file_btn)
        self.ui.load_pages.btns_basics.addWidget(self.open_dir_btn)
        self.ui.load_pages.btns_basics.addWidget(self.user_guide_btn)
        self.ui.load_pages.btns_basics.addWidget(self.contact_btn)

        # Agregando el logo
        self.logo_svg = QSvgWidget(Functions.set_svg_image("logo.svg"))
        self.ui.load_pages.logo_layout.addWidget(self.logo_svg)

        # PAGE 2
        # column 1
        self.eslabon_svg = QSvgWidget(Functions.set_svg_image("eslabon.svg"))
        self.ui.load_pages.eslabon_layout.addWidget(self.eslabon_svg)

        self.gruebler_svg = QSvgWidget(Functions.set_svg_image("gruebler.svg"))
        self.ui.load_pages.gruebler_layout.addWidget(self.gruebler_svg)

        self.grashof_svg = QSvgWidget(Functions.set_svg_image("grashof.svg"))
        self.ui.load_pages.grashof_layout.addWidget(self.grashof_svg)

        self.mecanismo_svg = QSvgWidget(Functions.set_svg_image("mecanismo.svg"))
        self.ui.load_pages.mecanismo_layout.addWidget(self.mecanismo_svg)

        # self.grashof = QSvgWidget(Functions.set_svg_image("mecanismo.svg"))
        # self.ui.load_pages.prueba_layout.addWidget(self.grashof)

        # PAGE 3
        self.analyze_button = PyPushButton(
            text="Analizar",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.analyze_button.setMinimumHeight(40)
        self.analyze_button.setMinimumWidth(80)

        # PY LINE EDIT O2x
        self.line_O2x = PyLineEdit(
            text="",
            place_holder_text="O2x",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_O2x.setMinimumHeight(30)

        # PY LINE EDIT O2y
        self.line_O2y = PyLineEdit(
            text="",
            place_holder_text="O2y",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_O2y.setMinimumHeight(30)

        # PY LINE EDIT O4x
        self.line_O4x = PyLineEdit(
            text="",
            place_holder_text="O4x",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_O4x.setMinimumHeight(30)
        # PY LINE EDIT O4y
        self.line_O4y = PyLineEdit(
            text="",
            place_holder_text="O4y",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_O4y.setMinimumHeight(30)

        # PY LINE EDIT Eslabón2
        self.line_eslabon2 = PyLineEdit(
            text="",
            place_holder_text="Medida eslabón 2",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_eslabon2.setMinimumHeight(30)

        # PY LINE EDIT Eslabón3
        self.line_eslabon3 = PyLineEdit(
            text="",
            place_holder_text="Medida eslabón 3",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_eslabon3.setMinimumHeight(30)
        # PY LINE EDIT Eslabón4
        self.line_eslabon4 = PyLineEdit(
            text="",
            place_holder_text="Medida eslabón 4",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_eslabon4.setMinimumHeight(30)
        # PY LINE EDIT Eslabón distancia P
        self.line_distance = PyLineEdit(
            text="",
            place_holder_text="Medida de la distancia P",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_distance.setMinimumHeight(30)
        # PY LINE EDIT theta2
        self.line_theta2 = PyLineEdit(
            text="",
            place_holder_text="theta 2 (°)",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_theta2.setMinimumHeight(30)
        # PY LINE EDIT omega2
        self.line_omega2 = PyLineEdit(
            text="",
            place_holder_text="omega 2 (rad/s)",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_omega2.setMinimumHeight(30)

        # Tabla de valores obtenidos mediante el análisis de Posición
        self.table_positions = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.table_positions.setColumnCount(13)
        self.table_positions.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_positions.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_positions.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.t1_column_1 = QTableWidgetItem()
        self.t1_column_1.setTextAlignment(Qt.AlignCenter)
        self.t1_column_1.setText("θ2")

        self.t1_column_2 = QTableWidgetItem()
        self.t1_column_2.setTextAlignment(Qt.AlignCenter)
        self.t1_column_2.setText("Ax")

        self.t1_column_3 = QTableWidgetItem()
        self.t1_column_3.setTextAlignment(Qt.AlignCenter)
        self.t1_column_3.setText("Ay")

        self.t1_column_4 = QTableWidgetItem()
        self.t1_column_4.setTextAlignment(Qt.AlignCenter)
        self.t1_column_4.setText("Bx")

        self.t1_column_5 = QTableWidgetItem()
        self.t1_column_5.setTextAlignment(Qt.AlignCenter)
        self.t1_column_5.setText("By")

        self.t1_column_6 = QTableWidgetItem()
        self.t1_column_6.setTextAlignment(Qt.AlignCenter)
        self.t1_column_6.setText("θ3")

        self.t1_column_7 = QTableWidgetItem()
        self.t1_column_7.setTextAlignment(Qt.AlignCenter)
        self.t1_column_7.setText("θ4")

        # Columns / Header
        self.t1_column_8= QTableWidgetItem()
        self.t1_column_8.setTextAlignment(Qt.AlignCenter)
        self.t1_column_8.setText("ω2")

        self.t1_column_9 = QTableWidgetItem()
        self.t1_column_9.setTextAlignment(Qt.AlignCenter)
        self.t1_column_9.setText("ω3")

        self.t1_column_10 = QTableWidgetItem()
        self.t1_column_10.setTextAlignment(Qt.AlignCenter)
        self.t1_column_10.setText("ω4")

        self.t1_column_11 = QTableWidgetItem()
        self.t1_column_11.setTextAlignment(Qt.AlignCenter)
        self.t1_column_11.setText("V_A")

        self.t1_column_12 = QTableWidgetItem()
        self.t1_column_12.setTextAlignment(Qt.AlignCenter)
        self.t1_column_12.setText("V_B")

        self.t1_column_13 = QTableWidgetItem()
        self.t1_column_13.setTextAlignment(Qt.AlignCenter)
        self.t1_column_13.setText("V_P")

        # Set column
        self.table_positions.setHorizontalHeaderItem(0, self.t1_column_1)
        self.table_positions.setHorizontalHeaderItem(1, self.t1_column_2)
        self.table_positions.setHorizontalHeaderItem(2, self.t1_column_3)
        self.table_positions.setHorizontalHeaderItem(3, self.t1_column_4)
        self.table_positions.setHorizontalHeaderItem(4, self.t1_column_5)
        self.table_positions.setHorizontalHeaderItem(5, self.t1_column_6)
        self.table_positions.setHorizontalHeaderItem(6, self.t1_column_7)
        self.table_positions.setHorizontalHeaderItem(7, self.t1_column_8)
        self.table_positions.setHorizontalHeaderItem(8, self.t1_column_9)
        self.table_positions.setHorizontalHeaderItem(9, self.t1_column_10)
        self.table_positions.setHorizontalHeaderItem(10, self.t1_column_11)
        self.table_positions.setHorizontalHeaderItem(11, self.t1_column_12)
        self.table_positions.setHorizontalHeaderItem(12, self.t1_column_13)
        # Tabla de valores obtenidos mediante el análisis de Velocidad





        # Función para realizar el análisis del mecanismo
        def calculate():
            global tabla
            O2x = self.line_O2x.text()
            O2y = self.line_O2y.text()
            O4x = self.line_O4x.text()
            O4y = self.line_O4y.text()
            L2 = self.line_eslabon2.text()
            L3 = self.line_eslabon3.text()
            L4 = self.line_eslabon4.text()
            P = self.line_distance.text()
            theta2 = self.line_theta2.text()
            omega2 = self.line_omega2.text()

            theta2_values = [theta2, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180]
            tabla = []
            for value in theta2_values:
                data1 = analyze(O2x, O2y, O4x, O4y, L2, L3, L4, P, value, omega2)
                tabla.append(data1)
                # data_initial = [] + data

            print(tabla)
            # para la primera tabla
            for x in tabla:
                row_number = self.table_positions.rowCount()
                self.table_positions.insertRow(row_number)  # Insert row
                self.table_positions.setItem(row_number, 0, QTableWidgetItem(str(x[0])))  # Add nick
                self.table_positions.setItem(row_number, 1, QTableWidgetItem(str(x[1])))
                self.table_positions.setItem(row_number, 2, QTableWidgetItem(str(x[2])))
                self.table_positions.setItem(row_number, 3, QTableWidgetItem(str(x[3])))
                self.table_positions.setItem(row_number, 4, QTableWidgetItem(str(x[4])))
                self.table_positions.setItem(row_number, 5, QTableWidgetItem(str(x[5])))
                self.table_positions.setItem(row_number, 6, QTableWidgetItem(str(x[6])))
                self.table_positions.setItem(row_number, 7, QTableWidgetItem(str(x[7])))
                self.table_positions.setItem(row_number, 8, QTableWidgetItem(str(x[8])))
                self.table_positions.setItem(row_number, 9, QTableWidgetItem(str(x[9])))
                self.table_positions.setItem(row_number, 10, QTableWidgetItem(str(x[10])))
                self.table_positions.setItem(row_number, 11, QTableWidgetItem(str(x[11])))
                self.table_positions.setRowHeight(row_number, 22)



        self.analyze_button.clicked.connect(calculate)
        # Agregando los widgets
        self.ui.load_pages.play_layout.addWidget(self.analyze_button)
        self.ui.load_pages.O2_layout.addWidget(self.line_O2x)
        self.ui.load_pages.O2_layout.addWidget(self.line_O2y)
        self.ui.load_pages.O4_layout.addWidget(self.line_O4x)
        self.ui.load_pages.O4_layout.addWidget(self.line_O4y)
        self.ui.load_pages.Eslabon_layout2.addWidget(self.line_eslabon2)
        self.ui.load_pages.Eslabon_layout3.addWidget(self.line_eslabon3)
        self.ui.load_pages.Eslabon_layout4.addWidget(self.line_eslabon4)
        self.ui.load_pages.P_layout.addWidget(self.line_distance)
        self.ui.load_pages.theta2_layout.addWidget(self.line_theta2)
        self.ui.load_pages.velocity_layout.addWidget(self.line_omega2)
        self.ui.load_pages.table1_layout.addWidget(self.table_positions)

        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.right_btn_1 = PyPushButton(
            text="Exportar",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_2
        ))

        # PY name file edit
        self.name_file_edit = PyLineEdit(
            text="",
            place_holder_text="Place holder text",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.name_file_edit.setMinimumHeight(40)

        self.ui.right_column.btn_export_layout.addWidget(self.right_btn_1)
        self.ui.right_column.name_layout.addWidget(self.name_file_edit)

        # BTN 2
        self.right_btn_2 = PyPushButton(
            text="Regresar",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_1
        ))
        self.ui.right_column.btn_return_layout.addWidget(self.right_btn_2)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)
