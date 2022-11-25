import os

# Funciones Básicas de la App
class Functions:
    # Uso de svg files para los iconos
    def set_svg_icon(self):
        app_path = os.path.abspath(os.getcwd())
        folder = "src/img/svg_icons"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, self))
        return icon

    def set_svg_image(self):
        app_path = os.path.abspath(os.getcwd())
        folder = "src/img/svg_images/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, self))
        return icon

    def set_image(self):
        app_path = os.path.abspath(os.getcwd())
        folder = "src/img/images/"
        path = os.path.join(app_path, folder)
        image = os.path.normpath(os.path.join(path, self))
        return image
