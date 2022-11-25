# Importamos los paquetes y modulos de project_core
from project_core import *

# Importamos los widgets
from src.widgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interfaz = UI_MainWindow()
        self.interfaz.setup_ui(self)

        settings = Settings()
        self.settings = settings.items

        self.hide_grips = True
        SetupMainWindow.setup_gui(self)

        # Mostrar la pantalla principal
        self.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app
