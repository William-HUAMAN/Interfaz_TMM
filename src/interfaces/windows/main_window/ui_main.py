# Importando Librerías necesarias
from src.core.libraries import *

# Importando archivos de configuración
from src.core.functions import Functions                    # Importando Funciones internas de la App
from src.core.json_settings import Settings                 # Importando Configuraciones desde el archivo JSON
from src.core.json_themes import Themes                     # Importando el tema de color

# Importando archivos gráficos
from src.widgets import *                                   # Importando Widgets
from . setup_main_window import *                           # Importando setup para la ventana principal
from src.interfaces.pages.ui_main_pages import Ui_MainPages # Importando la ventana principal de páginas

# RIGHT COLUMN
from src.interfaces.columns.ui_right_column import Ui_RightColumn

# PY WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        settings = Settings()               # Cargando las configuraciones
        self.settings = settings.items

        themes = Themes()                   # Cargando el tema de color
        self.themes = themes.items

        # Introduciendo los parámetros iniciales
        parent.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
        parent.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])

        # SET CENTRAL WIDGET
        # Añadiendo el widget central
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(f'''
            font: {self.settings["font"]["text_size"]}pt "{self.settings["font"]["family"]}";
            color: {self.themes["app_color"]["text_foreground"]};
        ''')
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        if self.settings["custom_title_bar"]:
            self.central_widget_layout.setContentsMargins(10,10,10,10)
        else:
            self.central_widget_layout.setContentsMargins(0,0,0,0)
        
        # LOAD PY WINDOW CUSTOM WIDGET
        # Add inside PyWindow "layout" all Widgets
        # ///////////////////////////////////////////////////////////////
        self.window = PyWindow(
            parent,
            bg_color = self.themes["app_color"]["bg_one"],
            border_color = self.themes["app_color"]["bg_two"],
            text_color = self.themes["app_color"]["text_foreground"]
        )
        
        # If disable custom title bar
        if not self.settings["custom_title_bar"]:
            self.window.set_stylesheet(border_radius = 0, border_size = 0)
        
        # ADD PY WINDOW TO CENTRAL WIDGET
        self.central_widget_layout.addWidget(self.window)

        # ADD FRAME LEFT MENU
        # Add here the custom left menu bar
        # ///////////////////////////////////////////////////////////////
        left_menu_margin = self.settings["left_menu_content_margins"]
        left_menu_minimum = self.settings["lef_menu_size"]["minimum"]
        self.left_menu_frame = QFrame()
        self.left_menu_frame.setMaximumSize(left_menu_minimum + (left_menu_margin * 2), 17280)
        self.left_menu_frame.setMinimumSize(left_menu_minimum + (left_menu_margin * 2), 0)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setContentsMargins(
            left_menu_margin,
            left_menu_margin,
            left_menu_margin,
            left_menu_margin
        )

        # ADD LEFT MENU
        # Add custom left menu here
        # ///////////////////////////////////////////////////////////////
        self.left_menu = PyLeftMenu(
            parent = self.left_menu_frame,
            app_parent = self.central_widget, # For tooltip parent
            dark_one = self.themes["app_color"]["dark_one"],
            dark_three = self.themes["app_color"]["dark_three"],
            dark_four = self.themes["app_color"]["dark_four"],
            bg_one = self.themes["app_color"]["bg_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_pressed"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            context_color = self.themes["app_color"]["context_color"],
            text_foreground = self.themes["app_color"]["text_foreground"],
            text_active = self.themes["app_color"]["text_active"]
        )
        self.left_menu_layout.addWidget(self.left_menu)

        # ADD LEFT COLUMN
        # Add here the left column with Stacked Widgets
        # ///////////////////////////////////////////////////////////////
        self.left_column_frame = QFrame()
        self.left_column_frame.setMaximumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setMinimumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setStyleSheet(f"background: {self.themes['app_color']['bg_two']}")

        # ADD LAYOUT TO LEFT COLUMN
        self.left_column_layout = QVBoxLayout(self.left_column_frame)
        self.left_column_layout.setContentsMargins(0,0,0,0)

        # ADD CUSTOM LEFT MENU WIDGET
        self.left_column = PyLeftColumn(
            parent,
            app_parent = self.central_widget,
            text_title = "Settings Left Frame",
            text_title_size = self.settings["font"]["title_size"],
            text_title_color = self.themes['app_color']['text_foreground'],
            icon_path = Functions.set_svg_icon("icon_settings.svg"),
            dark_one = self.themes['app_color']['dark_one'],
            bg_color = self.themes['app_color']['bg_three'],
            btn_color = self.themes['app_color']['bg_three'],
            btn_color_hover = self.themes['app_color']['bg_two'],
            btn_color_pressed = self.themes['app_color']['bg_one'],
            icon_color = self.themes['app_color']['icon_color'],
            icon_color_hover = self.themes['app_color']['icon_hover'],
            context_color = self.themes['app_color']['context_color'],
            icon_color_pressed = self.themes['app_color']['icon_pressed'],
            icon_close_path = Functions.set_svg_icon("icon_close.svg")
        )
        self.left_column_layout.addWidget(self.left_column)

        # ADD RIGHT WIDGETS
        # Add here the right widgets
        # ///////////////////////////////////////////////////////////////
        self.right_app_frame = QFrame()

        # ADD RIGHT APP LAYOUT
        self.right_app_layout = QVBoxLayout(self.right_app_frame)
        self.right_app_layout.setContentsMargins(3,3,3,3)
        self.right_app_layout.setSpacing(6)

        # ADD TITLE BAR FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setMinimumHeight(40)
        self.title_bar_frame.setMaximumHeight(40)
        self.title_bar_layout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_layout.setContentsMargins(0,0,0,0)
        
        # ADD CUSTOM TITLE BAR TO LAYOUT
        self.title_bar = PyTitleBar(
            parent,
            logo_width = 100,
            app_parent = self.central_widget,
            logo_image = "logo_top_100x22.svg",
            bg_color = self.themes["app_color"]["bg_two"],
            div_color = self.themes["app_color"]["bg_three"],
            btn_bg_color = self.themes["app_color"]["bg_two"],
            btn_bg_color_hover = self.themes["app_color"]["bg_three"],
            btn_bg_color_pressed = self.themes["app_color"]["bg_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_pressed"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            context_color = self.themes["app_color"]["context_color"],
            dark_one = self.themes["app_color"]["dark_one"],
            text_foreground = self.themes["app_color"]["text_foreground"],
            radius = 8,
            font_family = self.settings["font"]["family"],
            title_size = self.settings["font"]["title_size"],
            is_custom_title_bar = self.settings["custom_title_bar"]
        )
        self.title_bar_layout.addWidget(self.title_bar)

        # ADD CONTENT AREA
        # ///////////////////////////////////////////////////////////////
        self.content_area_frame = QFrame()

        # CREATE LAYOUT
        self.content_area_layout = QHBoxLayout(self.content_area_frame)
        self.content_area_layout.setContentsMargins(0,0,0,0)
        self.content_area_layout.setSpacing(0)

        # LEFT CONTENT
        self.content_area_left_frame = QFrame()

        # IMPORT MAIN PAGES TO CONTENT AREA
        self.load_pages = Ui_MainPages()
        self.load_pages.setupUi(self.content_area_left_frame)

        # RIGHT BAR
        self.right_column_frame = QFrame()
        self.right_column_frame.setMinimumWidth(self.settings["right_column_size"]["minimum"])
        self.right_column_frame.setMaximumWidth(self.settings["right_column_size"]["minimum"])

        # IMPORT RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////
        self.content_area_right_layout = QVBoxLayout(self.right_column_frame)
        self.content_area_right_layout.setContentsMargins(5,5,5,5)
        self.content_area_right_layout.setSpacing(0)

        # RIGHT BG
        self.content_area_right_bg_frame = QFrame()
        self.content_area_right_bg_frame.setObjectName("content_area_right_bg_frame")
        self.content_area_right_bg_frame.setStyleSheet(f'''
        #content_area_right_bg_frame {{
            border-radius: 8px;
            background-color: {self.themes["app_color"]["bg_two"]};
        }}
        ''')

        # ADD BG
        self.content_area_right_layout.addWidget(self.content_area_right_bg_frame)

        # ADD RIGHT PAGES TO RIGHT COLUMN
        self.right_column = Ui_RightColumn()
        self.right_column.setupUi(self.content_area_right_bg_frame)

        # ADD TO LAYOUTS
        self.content_area_layout.addWidget(self.content_area_left_frame)
        self.content_area_layout.addWidget(self.right_column_frame)

        # ADD WIDGETS TO RIGHT LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.right_app_layout.addWidget(self.title_bar_frame)
        self.right_app_layout.addWidget(self.content_area_frame)
        
        # ADD WIDGETS TO "PyWindow"
        # Add here your custom widgets or default widgets
        # ///////////////////////////////////////////////////////////////
        self.window.layout.addWidget(self.left_menu_frame)
        self.window.layout.addWidget(self.left_column_frame)
        self.window.layout.addWidget(self.right_app_frame)

        # ADD CENTRAL WIDGET AND SET CONTENT MARGINS
        # ///////////////////////////////////////////////////////////////
        parent.setCentralWidget(self.central_widget)