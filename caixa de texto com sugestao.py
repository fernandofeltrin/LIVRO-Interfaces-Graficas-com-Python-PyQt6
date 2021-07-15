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
        texto1 = QLabel('Login: ', self)
        texto1.move(40, 50) # Define manualmente a posição onde texto1 será inserida, nesse caso, 100 pixels a partir da esquerda, 50 pixels a partir do topo. Se não definir este parâmetro para os labels, seus respectivos textos aparecerão sobrepostos. O Método move( ) serve para qualquer elemento visual da janela.

        botao1 = QPushButton('SAIR', self) # Será inserido um botão na posição inicial da janela (canto superior esquerdo) que neste momento ao clicar não realiza nenhuma ação, pois o botão inicial é apenas um botão, sem nada pré-configurado para o mesmo.
        botao1.move(100, 200)
        botao1.clicked.connect(self.sair) # Quando botao1 for clicado, executará a função sair() que deve ser definida manualmente ou usada a partir de alguma função embutida do sistema

        self.caixa_texto1 = QLineEdit(self) # Cria uma caixa de texto padrão para que o usuário digite alguma coisa
        self.caixa_texto1.setPlaceholderText('Digite seu nome de usuário')
        self.caixa_texto1.move(90, 48) # Define a posição da caixa de texto

        texto2 = QLabel('Senha: ', self)
        texto2.move(40, 74)
        self.caixa_texto2 = QLineEdit(self)
        self.caixa_texto2.setPlaceholderText('Digite sua senha')
        self.caixa_texto2.move(90, 72)

        self.show()

    def sair(self):
        sys.exit(qt.exec()) # Aciona a função do sistema para fechar a janela principal do programa

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
