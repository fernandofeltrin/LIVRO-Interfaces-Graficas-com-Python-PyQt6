import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Programa') # Define manualmente o título da janela.
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(150, 150, 480, 320) # Por justaposição, o primeiro parâmetro define a distância em pixels da lateral esquerda da tela até a janela, seguido do segundo parâmetro que define a distância em pixels do topo da tela até a borda superior da janela. Na sequência os dois últimos parâmetros se referem a largura e a altura da janela, respectivamente.
        self.Interface() # Instancia o método de classe Interface()

    def Interface(self):
        self.texto1 = QLabel('Olá Mundo!!!', self) # Será criada uma linha de texto na posição inicial da janela, que por padrão é o canto superior esquerdo
        self.texto1.move(100, 50) # Define manualmente a posição onde texto1 será inserida, nesse caso, 100 pixels a partir da esquerda, 50 pixels a partir do topo. Se não definir este parâmetro para os labels, seus respectivos textos aparecerão sobrepostos. O Método move( ) serve para qualquer elemento visual da janela.

        botao1 = QPushButton('Maiusculo', self)
        botao1.move(100, 200)
        botao1.clicked.connect(self.maiusculo)

        botao2 = QPushButton('Invertido', self)
        botao2.move(200, 200)
        botao2.clicked.connect(self.invertido)

        self.show()

    def maiusculo(self):
        self.texto1.setText('OLÁ MUNDO!!!') # Irá retornar OLÁ MUNDO! pois o tamanho da string excede o tamanho padrão da label
        self.texto1.resize(150, 15) # Aumenta o tamanho padrão da label para que a string não seja cortada
    def invertido(self):
        self.texto1.setText('!!!odnuM àlO')

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
