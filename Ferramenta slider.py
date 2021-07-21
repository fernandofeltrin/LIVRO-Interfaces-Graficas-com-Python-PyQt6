import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Programa') # Define manualmente o título da janela.
        self.setGeometry(150, 150, 350, 100) # Por justaposição, o primeiro parâmetro define a distância em pixels da lateral esquerda da tela até a janela, seguido do segundo parâmetro que define a distância em pixels do topo da tela até a borda superior da janela. Na sequência os dois últimos parâmetros se referem a largura e a altura da janela, respectivamente.
        self.Interface() # Instancia o método de classe Interface()

    def Interface(self):
        texto_slider = QLabel('Quando de memória deseja alocar?', self)
        texto_slider.move(10, 20)
        self.slider = QSlider(Qt.Orientation.Horizontal, self) # Cria um slider genérico, caso não seja repassado nenhum parâmetro, será um slider vertical
        self.slider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.slider.setGeometry(10, 40, 330, 30)
        self.slider.setMinimum(20)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.valueChanged.connect(self.recebe_valor) # No caso de um slider, o método que conecta o gatilho para executar uma ação em uma função é valueChanged.connect( )
        self.valor = QLabel('0')
        self.valor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.show()

    def recebe_valor(self):
        val_escolhido = self.slider.value()
        self.valor.setText(str(val_escolhido))
        print(f'Valor escolhido: {val_escolhido}%')

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
