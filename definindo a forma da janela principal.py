import sys
from PyQt6.QtWidgets import *

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 150, 480, 320)
        # Por justaposição, o primeiro parâmetro define a distância em pixels da lateral esquerda da tela até a janela, seguido do segundo parâmetro que define a distância em pixels do topo da tela até a borda superior da janela. Na sequência os dois últimos parâmetros se referem a largura e a altura da janela, respectivamente.

        self.show()

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
