from importlib import import_module
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont

class Utils:
    """Classe define um conjunto de funcoes, estilos e recursos que podem
       ser utilizados a qualquer momento."""

    def show_dialog(self, title, message, information) -> None:
        """Devolve uma janela para enviar mensagens ao usuario."""
        msg_box = QMessageBox()
        msg_box.setIcon(information) 
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.buttonClicked.connect(self.on_click)
        value = msg_box.exec()
        if value == QMessageBox.Ok:
            msg_box.close()

    def on_click(self):
        """pass"""

    def format_bold_text(self):
        """Devolve uma fonte em negrito."""
        my_font = QFont()
        my_font.setBold(True)
        return my_font

