# Importando paquetes y módulos
from src.core.libraries import json,os

# Importando las configuraciones
from src.core.json_settings import Settings

# Temas de la Aplicación
class Themes(object):
    # Cargar las configuraciones
    setup_settings = Settings()
    _settings = setup_settings.items

    # Acceso al PATH
    json_file = f"src/themes/{_settings['theme_name']}.json"
    app_path = os.path.abspath(os.getcwd())
    settings_path = os.path.normpath(os.path.join(app_path, json_file))
    if not os.path.isfile(settings_path):
        print(f"WARNING: \"src/themes/{_settings['theme_name']}.json\" not found! check in the folder {settings_path}")

    # INIT SETTINGS
    def __init__(self):
        super(Themes, self).__init__()
        self.items = {} # Diccionario con las configuraciones
        self.deserialize() # Deserializar
    
    # Escritura del archivo JSON
    def serialize(self):
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(self.items, write, indent=4)

    # Lectura del archivo jSON
    def deserialize(self):
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            settings = json.loads(reader.read())
            self.items = settings