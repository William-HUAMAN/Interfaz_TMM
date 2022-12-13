from src.core.libraries import *

# Funciones internas de la App para trabajar con imágenes
class Functions:
    def set_svg_icon(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "src/img/svg_icons/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon
    
    def set_svg_image(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "src/img/svg_images/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    def set_image(image_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "src/img/images/"
        path = os.path.join(app_path, folder)
        image = os.path.normpath(os.path.join(path, image_name))
        return image

# Funciones para trabajar con archivos
# Funciones para redactar documentos
class Word_document(object):
    def __init__(self):
        pass
