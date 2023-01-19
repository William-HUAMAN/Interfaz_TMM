# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from src.core.libraries import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QSpinBox {{
    border: none;
	background-color: {_bg_color};
	border-radius: {_radius}px;
	padding-left: 1px;
    padding-right: 5px;
    color: {_color};
}}
'''

# PY SPINBOX
# ///////////////////////////////////////////////////////////////
class PySpinBox(QSpinBox):
    def __init__(
        self,
        radius,
        color,
        bg_color,
    ):
        super().__init__()

        # APPLY STYLESHEET
        style_format = style.format(
            _radius = radius,
            _color = color,
            _bg_color = bg_color
        )
        self.setStyleSheet(style_format)

