from PyQt5.QtWidgets import (QFormLayout, QHBoxLayout, QLineEdit,
                             QWidget, QPushButton)
from PyQt5.QtCore import Qt
#import sys
class GetVideoById:

    def __init__(self, *args, **kargs):
        super(GetVideoById, self).__init__(*args, **kargs)
        self.window = QWidget()
        self.window.setWindowTitle("get_video post vídeo")
        self.form_lay = QFormLayout()
        self.le_name = QLineEdit()
        self.le_password = QLineEdit()
        self.le_password.setEchoMode(QLineEdit.Password)
        self.pb_yes = QPushButton('Confirmar')
        self.pb_no = QPushButton('Cancelar')
        self.hb_lay = QHBoxLayout()
        self.pb_yes.setFixedSize(100, 25)
        self.pb_no.setFixedSize(100, 25)
        self.form_lay.addRow('post_id: ', self.le_name)
        self.hb_lay.addWidget(self.pb_yes)
        self.hb_lay.addWidget(self.pb_no)
        self.form_lay.addRow(self.hb_lay)
        self.window.setLayout(self.form_lay)
        self.form_lay.setFormAlignment(Qt.AlignHCenter)

    def screem_get_video(self):
        """
        Carrega a janela de get_video, defindo suas dimensões.
        """
        self.window.setGeometry(400, 800, 300, 110)
        self.window.show()
    
        
    