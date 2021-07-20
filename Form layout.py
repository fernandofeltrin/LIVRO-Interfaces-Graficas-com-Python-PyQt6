import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Programa') # Define manualmente o título da janela.
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(150, 150, 350, 300) # Por justaposição, o primeiro parâmetro define a distância em pixels da lateral esquerda da tela até a janela, seguido do segundo parâmetro que define a distância em pixels do topo da tela até a borda superior da janela. Na sequência os dois últimos parâmetros se referem a largura e a altura da janela, respectivamente.
        self.Interface() # Instancia o método de classe Interface()

    def Interface(self):
        layout = QFormLayout()

        texto_usuario = QLabel('Usuário: ')
        input_usuario = QLineEdit()
        input_usuario.setPlaceholderText('Digite seu nome de usuário')
        texto_senha = QLabel('Senha: ')
        input_senha = QLineEdit()
        input_senha.setPlaceholderText('Digite sua senha')
        seleciona_ambiente = QComboBox()  # Cria uma caixa de seleção inicialmente vazia.
        seleciona_ambiente.addItem('Ambiente Comum')  # Primeiro elemento da caixa de seleção
        seleciona_ambiente.addItem('Painel de Controle')  # Segundo elemento da caixa de seleção

        layout.addRow(texto_usuario, input_usuario) # Insere uma linha contendo o campo 'Usuário: ' seguido do campo para inserção de texto
        layout.addRow(texto_senha, input_senha) # Insere uma segunda linha, agora contendo os campos 'Senha: ' e o campo para inserção da senha
        layout.addRow(QLabel('Salvar Informações: '), seleciona_ambiente) # Ao criar a linha, já insere na mesma um texto/label e um campo para seleção

        layout_secundario = QHBoxLayout() # Contornando o problema, podemos criar uma estrutura de layout secundária, de outro formato, para que possamos reorganizar os elementos
        layout_secundario.addStretch() # Insere um espaço antes dos botões
        layout_secundario.addWidget(QPushButton('ENTRAR')) # Dentro desse layout secundário criamos os botões que queremos
        layout_secundario.addWidget(QPushButton('SAIR'))
        layout_secundario.addStretch() # Insere um espaço depois dos botões, assim, centralizando os mesmos dentro do layout
        layout.addRow(layout_secundario) # Instanciamos novamente o layout geral de nossa janela, incorporando na mesma, dentro de uma nova linha, o layout secundário e seus elementos.

        self.setLayout(layout)
        self.show()

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
