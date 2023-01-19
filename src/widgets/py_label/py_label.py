# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from src.core.libraries import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QLabel {{
	border: none;
    text_size: {_text_size};
    font: {_text_size}pt "{_font_family}";
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius}px;
	background-color: {_bg_color};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyLabel(QLabel):
    def __init__(
            self,
            text,
            font_family,
            text_size,
            radius,
            color,
            bg_color,
            parent=None,
    ):
        super().__init__()

        # SET PARAMETRES
        self.setText(text)
        self.setWordWrap(True)

        if parent != None:
            self.setParent(parent)

        # SET STYLESHEET
        custom_style = style.format(
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _font_family=font_family,
            _text_size=text_size,
        )
        self.setStyleSheet(custom_style)

