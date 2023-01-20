# Importando Librerías necesarias
from src.core.libraries import *
import pyqtgraph as pg
# Importando configuraciones
from src.core.json_settings import Settings  # Archivo JSON de configuraciones
from src.core.json_themes import Themes  # Tema de color seleccionado

# Importando recursos gráficos
from main import MainWindow
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
        def visit_page():
            webbrowser.open_new("https://spiral-square-81f.notion.site/Proyecto-PEMS-e88a3f889a894bc7b089d58fd7fb9d92")

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
        self.left_btn_doc.clicked.connect(visit_page)

        # COLOR THEME 1
        self.lbl_theme = PyLabel(
            text="Tema de color",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["text_description"]
        )
        # THEME BUTTON
        def change_theme():
            self.btn_theme.is_active = True
            self.btn_theme.update()

        self.btn_theme = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_add_user.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Light",
            width=50,
            height=45,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=False
        )
        self.btn_theme.clicked.connect(change_theme)

        self.lbl_sizetext = PyLabel(
            text="Tamaño de texto",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["text_description"]
        )
        self.spin_text = PySpinBox(
            radius=8,
            color=self.themes["app_color"]["text_description"],
            bg_color=self.themes["app_color"]["dark_two"],
        )
        self.spin_text.setMaximumHeight(45)
        self.spin_text.setMaximumWidth(50)
        self.spin_text.setMinimum(7)
        self.spin_text.setValue(self.settings["font"]["text_size"])
        self.spin_text.setMaximum(22)

        def change_sizeText():
            value = self.spin_text.value()
            # load data from json file
            with open('src/core/settings.json', 'r') as file:
                data = json.load(file)

            # modify the value
            data['font']['text_size']=value
            with open('src/core/settings.json', 'w') as file:
                json.dump(data, file)

        self.spin_text.valueChanged.connect(change_sizeText)

        self.lbl_name = PyLabel(
            text="Nombre del Proyecto",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["text_description"]
        )
        with open('src/core/project_properties.json', 'r') as file:
            self.project = json.load(file)

        self.line_name = PyLineEdit(
            text="",
            place_holder_text=self.project['file_name'],
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_name.setMinimumHeight(40)

        self.lbl_note = PyLabel(
            text="Los cambios realizados estarán disponibles la siguiente vez que se cargue la aplicación",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["text_description"]
        )
        # self.text_1.setMaximumHeight(100)
        self.ui.left_column.menus.theme_Layout.addWidget(self.lbl_theme)
        self.ui.left_column.menus.theme_Layout.addWidget(self.btn_theme)
        self.ui.left_column.menus.sizetext_Layout.addWidget(self.lbl_sizetext)
        self.ui.left_column.menus.sizetext_Layout.addWidget(self.spin_text)
        self.ui.left_column.menus.name_Layout.addWidget(self.lbl_name)
        self.ui.left_column.menus.name_Layout.addWidget(self.line_name)
        self.ui.left_column.menus.name_Layout.addWidget(self.lbl_note)

        # PAGES
        # ///////////////////////////////////////////////////////////////
        # PAGE 1 - first page
        # new file button
        def creating_file():
            directory = QFileDialog.getExistingDirectory()
            with open('src/core/project_properties.json', 'r') as file:
                data_dir = json.load(file)
                if data_dir != " ":
                    data_dir['directory'] = directory
                else:
                    data_dir = json.load(file)
            with open('src/core/project_properties.json', 'w') as file:
                json.dump(data_dir, file)

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
        self.new_file_btn.clicked.connect(creating_file)

        def open_file():
            directory = QFileDialog.getExistingDirectory()
            with open('src/core/project_properties.json', 'r') as file:
                data_dir = json.load(file)
                if data_dir != " ":
                    data_dir['directory'] = directory
                else:
                    data_dir = json.load(file)
            with open('src/core/project_properties.json', 'w') as file:
                json.dump(data_dir, file)

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
        self.open_dir_btn.clicked.connect(open_file)

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
        self.user_guide_btn.clicked.connect(visit_page)

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
        self.lbl_eslabon = PyLabel(
            text="Un eslabón es un cuerpo rígido que posee al menos dos nodos por los cuales se une a eslabones.\nUna "
                 "junta es una conexión entre dos o más eslabones, lo cual permite su movimiento.",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.ui.load_pages.description_layout.addWidget(self.lbl_eslabon)

        self.lbl_gruebler = PyLabel(
            text="Los grados de libertad de mecanismos planares unidos por juntas comunes pueden ser calculados a "
                 "partir de la ecuación de Gruebler.",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.ui.load_pages.desc_gruebler_layout.addWidget(self.lbl_gruebler)

        self.lbl_mecanismo4 = PyLabel(
            text="Es un mecanismo plano compuesto por 4 sólidos rígidos conectados entre sí mediante 4 pares "
                 "cinemáticos de revolución. Usualmente uno de los sólidos está fijo durante su movimiento.",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.ui.load_pages.mecanismo4_layout.addWidget(self.lbl_mecanismo4)

        self.lbl_grashof = PyLabel(
            text="Es una relación que predice el comportamiento de rotación o rotabilidad de las inversiones de un "
                 "mecanismo de cuatro barras basado sólo en las longitudes de los eslabones.",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.ui.load_pages.desc_grashof_layout.addWidget(self.lbl_grashof)

        self.lbl_grashof2 = PyLabel(
            text="De cumplirse la condición, el eslabonamiento es de Grashof y por lo menos un eslabón será capaz de "
                 "realizar una revolución completa con respecto al plano de bancada.",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.ui.load_pages.grashof2_layout.addWidget(self.lbl_grashof2)


        self.eslabon_svg = QSvgWidget(Functions.set_svg_image("eslabon.svg"))
        self.ui.load_pages.eslabon_layout.addWidget(self.eslabon_svg)

        self.gruebler_svg = QSvgWidget(Functions.set_svg_image("gruebler.svg"))
        self.ui.load_pages.gruebler_layout.addWidget(self.gruebler_svg)

        self.grashof_svg = QSvgWidget(Functions.set_svg_image("grashof.svg"))
        self.ui.load_pages.grashof_layout.addWidget(self.grashof_svg)

        self.mecanismo_svg = QSvgWidget(Functions.set_svg_image("mecanismo.svg"))
        self.ui.load_pages.mecanismo_layout.addWidget(self.mecanismo_svg)

        # column 2
        self.lbl_position = PyLabel(
            text="La posición de un punto en el plano puede definirse por medio de un vector de posición. La elección "
                 "de ejes de referencia es arbitraria y se elige de conformidad con el observador.",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.ui.load_pages.pos_layout.addWidget(self.lbl_position)

        self.lbl_pos_analysis = PyLabel(
            text="El análisis de posición es uno de los pasos iniciales en la síntesis de mecanismos, donde la "
                 "generación de movimiento y de trayectoria son unos de los problemas principales en la síntesis "
                 "dimensional de mecanismos.\nLas ecuaciones necesarias para este procedimiento se detallan a "
                 "continuación:",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.ui.load_pages.pos_analysis_layout.addWidget(self.lbl_pos_analysis)

        self.ec_analisis1 = QSvgWidget(Functions.set_svg_image("ec_analisis1.svg"))
        self.ui.load_pages.Ec_pos_layout.addWidget(self.ec_analisis1)

        # column 3
        self.lbl_vel_analysis = PyLabel(
            text="El análisis gráfico de velocidad determina la velocidad de puntos de un mecanismo en una sola "
                 "configuración. Se debe hacer énfasis en que los resultados de este análisis corresponden a la "
                 "posición actual del mecanismo. Conforme el mecanismo se mueve, la configuración cambia al igual que "
                 "las velocidades.\nLas ecuaciones necesarias para este procedimiento se detallan a "
                 "continuación:",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.ui.load_pages.vel_analysis_layout.addWidget(self.lbl_vel_analysis)
        self.ec_analisis2 = QSvgWidget(Functions.set_svg_image("ec_analisis2.svg"))
        self.ui.load_pages.Ec_vel_layout.addWidget(self.ec_analisis2)

        # self.grashof = QSvgWidget(Functions.set_svg_image("mecanismo.svg"))
        # self.ui.load_pages.prueba_layout.addWidget(self.grashof)

        # PAGE 3
        # gráfica
        self.graph = pg.PlotWidget()
        self.graph.showGrid(x=True, y=True)

        x_s = [0, 10, 40, 60]
        y_s = [0, 50, 35, 0]
        self.graph = pg.PlotWidget()
        self.graph.showGrid(x=True, y=True)
        self.graph.plot(x_s, y_s, pen='r', symbol='o', symbolPen='b', symbolBrush=0.2)
        self.ui.load_pages.graph_layout.addWidget(self.graph)

        self.lbl_grashof_cond = PyLabel(
            text="",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.lbl_grashof_cond.setMinimumWidth(500)
        self.lbl_grashof_cond.setMaximumHeight(30)

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

        # delta3
        self.line_delta3 = PyLineEdit(
            text="",
            place_holder_text="Delta 3",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_delta3.setMinimumHeight(30)
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

        # PY LINE EDIT omega2
        self.line_alpha2 = PyLineEdit(
            text="",
            place_holder_text="alpha 2 (rad/s^2)",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_alpha2.setMinimumHeight(30)

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
        self.table_positions.setColumnCount(18)
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
        self.t1_column_8 = QTableWidgetItem()
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

        self.t1_column_14 = QTableWidgetItem()
        self.t1_column_14.setTextAlignment(Qt.AlignCenter)
        self.t1_column_14.setText("α3")

        self.t1_column_15 = QTableWidgetItem()
        self.t1_column_15.setTextAlignment(Qt.AlignCenter)
        self.t1_column_15.setText("α4")

        self.t1_column_16 = QTableWidgetItem()
        self.t1_column_16.setTextAlignment(Qt.AlignCenter)
        self.t1_column_16.setText("Ac_A")

        self.t1_column_17 = QTableWidgetItem()
        self.t1_column_17.setTextAlignment(Qt.AlignCenter)
        self.t1_column_17.setText("Ac_BA")

        self.t1_column_18 = QTableWidgetItem()
        self.t1_column_18.setTextAlignment(Qt.AlignCenter)
        self.t1_column_18.setText("Ac_B")

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
        self.table_positions.setHorizontalHeaderItem(13, self.t1_column_14)
        self.table_positions.setHorizontalHeaderItem(14, self.t1_column_15)
        self.table_positions.setHorizontalHeaderItem(15, self.t1_column_16)
        self.table_positions.setHorizontalHeaderItem(16, self.t1_column_17)
        self.table_positions.setHorizontalHeaderItem(17, self.t1_column_18)
        # Tabla de valores obtenidos mediante el análisis de Velocidad

        # Función para realizar el análisis del mecanismo
        def calculate():
            self.ui.load_pages.graph_layout.removeWidget(self.graph)
            self.lbl_grashof_cond.setText(" si es grasshof")
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
            alpha2 = self.line_alpha2.text()
            delta3 = self.line_delta3.text()

            theta2_values = [theta2, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180]
            tabla = []
            for value in theta2_values:
                data1 = analyze(O2x, O2y, O4x, O4y, L2, L3, L4, P, value, omega2, alpha2, delta3)
                tabla.append(data1)
                # data_initial = [] + data

            # Escribir los datos de la tabla en el archivo JSON del proyecto
            with open('src/core/project_properties.json', 'r') as file:
                data_dir = json.load(file)
                if data_dir != " ":
                    data_dir['tabla'] = tabla
                else:
                    data_dir = json.load(file)
            with open('src/core/project_properties.json', 'w') as file:
                json.dump(data_dir, file)

            # print(tabla)
            # para la primera tabla
            #self.table_positions.clear()
            #self.table_positions.setRowCount()
            self.table_positions.setColumnCount(18)

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
                self.table_positions.setItem(row_number, 12, QTableWidgetItem(str(x[12])))
                self.table_positions.setItem(row_number, 13, QTableWidgetItem(str(x[13])))
                self.table_positions.setItem(row_number, 14, QTableWidgetItem(str(x[14])))
                self.table_positions.setItem(row_number, 15, QTableWidgetItem(str(x[15])))
                self.table_positions.setItem(row_number, 16, QTableWidgetItem(str(x[16])))
                self.table_positions.setItem(row_number, 17, QTableWidgetItem(str(x[17])))
                self.table_positions.setRowHeight(row_number, 22)

            # ///////////////////////////////////////gráfica lineal///////////////////////////////////////////////
            # gráfica
            self.graph = pg.PlotWidget()
            self.graph.showGrid(x=True, y=True)

            x_s = [float(O2x), float(tabla[0][1]), float(tabla[0][3]), float(O4x)]
            y_s = [float(O2y), float(tabla[0][2]), float(tabla[0][4]), float(O4y)]
            self.graph = pg.PlotWidget()
            self.graph.showGrid(x=True, y=True)
            self.graph.plot(x_s, y_s, pen='r', symbol='o', symbolPen='b', symbolBrush=0.2)
            self.ui.load_pages.graph_layout.addWidget(self.graph)

        self.analyze_button.clicked.connect(calculate)
        # Agregando los widgets
        self.ui.load_pages.cond_grashof_layout.addWidget(self.lbl_grashof_cond)
        self.ui.load_pages.play_layout.addWidget(self.analyze_button)
        self.ui.load_pages.O2_layout.addWidget(self.line_O2x)
        self.ui.load_pages.O2_layout.addWidget(self.line_O2y)
        self.ui.load_pages.O4_layout.addWidget(self.line_O4x)
        self.ui.load_pages.O4_layout.addWidget(self.line_O4y)
        self.ui.load_pages.Eslabon_layout2.addWidget(self.line_eslabon2)
        self.ui.load_pages.Eslabon_layout3.addWidget(self.line_eslabon3)
        self.ui.load_pages.Eslabon_layout4.addWidget(self.line_eslabon4)
        self.ui.load_pages.P_layout.addWidget(self.line_distance)
        self.ui.load_pages.delta3_layout.addWidget(self.line_delta3)
        self.ui.load_pages.theta2_layout.addWidget(self.line_theta2)
        self.ui.load_pages.velocity_layout.addWidget(self.line_omega2)
        self.ui.load_pages.aceleration_layout.addWidget(self.line_alpha2)
        self.ui.load_pages.table1_layout.addWidget(self.table_positions)

        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.lbl_exportar = PyLabel(
            text="Seleccione el formato en el que desea exportar sus datos calculados",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.ui.right_column.exportar_layout.addWidget(self.lbl_exportar)

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



        self.ui.right_column.btn_export_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.lbl_return = PyLabel(
            text="Tu archivo ha sido exportado exitosamente, para revisar el archivo ingresa en la carpeta del "
                 "proyecto, gracias por usar PEMS, por favor deja tu comentario acerca de nuestra aplicación para "
                 "poder seguir mejorando",
            radius=8,
            bg_color=self.themes["app_color"]["bg_two"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            color=self.themes["app_color"]["white"]
        )
        self.ui.right_column.return_layout.addWidget(self.lbl_return)

        self.btn_comment = PyPushButton(
            text="Comentar App",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.right_column.comment_layout.addWidget(self.btn_comment)

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
