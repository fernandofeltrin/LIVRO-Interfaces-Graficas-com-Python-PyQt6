import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Programa') # Define manualmente o título da janela.
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(150, 150, 300, 320) # Por justaposição, o primeiro parâmetro define a distância em pixels da lateral esquerda da tela até a janela, seguido do segundo parâmetro que define a distância em pixels do topo da tela até a borda superior da janela. Na sequência os dois últimos parâmetros se referem a largura e a altura da janela, respectivamente.
        self.Interface() # Instancia o método de classe Interface()

    def Interface(self):
        self.logo = QLabel(self) # Cria um novo campo para inserção de conteúdo
        self.logo.setPixmap(QPixmap('python.png')) # Importa a imagem e a posiciona na janela
        self.logo.move(100, 150) # Define a posição da imagem na janela, lembrando que uma umagem pode ser colocada como fundo dos demais elementos da janela.

        texto1 = QLabel('Login: ', self) # Será criada uma linha de texto na posição inicial da janela, que por padrão é o canto superior esquerdo
        texto1.move(40, 50) # Define manualmente a posição onde texto1 será inserida, nesse caso, 100 pixels a partir da esquerda, 50 pixels a partir do topo. Se não definir este parâmetro para os labels, seus respectivos textos aparecerão sobrepostos. O Método move( ) serve para qualquer elemento visual da janela.

        botao1 = QPushButton('SAIR', self) # Será inserido um botão na posição inicial da janela (canto superior esquerdo) que neste momento ao clicar não realiza nenhuma ação, pois o botão inicial é apenas um botão, sem nada pré-configurado para o mesmo.
        botao1.move(117, 270)
        botao1.clicked.connect(self.sair) # Quando botao1 for clicado, executará a função sair() que deve ser definida manualmente ou usada a partir de alguma função embutida do sistema

        self.caixa_texto1 = QLineEdit(self) # Cria uma caixa de texto padrão para que o usuário digite alguma coisa
        self.caixa_texto1.setPlaceholderText('Digite seu nome de usuário')
        self.caixa_texto1.move(90, 48) # Define a posição da caixa de texto

        texto2 = QLabel('Senha: ', self)
        texto2.move(40, 74)
        self.caixa_texto2 = QLineEdit(self)
        self.caixa_texto2.setPlaceholderText('Digite sua senha')
        self.caixa_texto2.setEchoMode(QLineEdit.EchoMode.Password) # Irá esconder o conteúdo digitado, exibindo apenas asteriscos em seu lugar
        self.caixa_texto2.move(90, 72)

        self.salvar_checkbox = QCheckBox('Salvar informações', self) # Cria uma checkbox com a instrução ao lado
        self.salvar_checkbox.move(90, 94) # Define a posição da checkbox
        self.salvar_checkbox.clicked.connect(self.salva_dados) # Associa a checkbox como um botão ligado a função salva_dados( )

        botao2 = QPushButton('ENTRAR', self)
        botao2.clicked.connect(self.salva_dados)  # Ao clicar, aciona a função salva_dados( )
        botao2.move(117, 114)

        self.show()

    def sair(self):
        sys.exit(qt.exec()) # Aciona a função do sistema para fechar a janela principal do programa

    def salva_dados(self):
        if self.salvar_checkbox.isChecked(): # Caso a checkbox esteja marcada...
            base = []
            base.append(self.caixa_texto1.text()) # Recebe o texto digitado pelo usuário para Login
            base.append(self.caixa_texto2.text()) # Recebe o texto digitado pelo usuário para Senha
            print(f'Nome de usuário: {base[0]} \nSenha: {base[1]}')
        else: # Caso a checkbox esteja desmarcada...
            print(f'Usuário optou por não salvar os dados.')

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
