import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Programa')
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(150, 150, 350, 300)
        self.Interface()

    def Interface(self):
        layout = QFormLayout()

        texto_usuario = QLabel('Usuário: ')
        input_usuario = QLineEdit()
        input_usuario.setPlaceholderText('Digite seu nome de usuário')
        texto_senha = QLabel('Senha: ')
        input_senha = QLineEdit()
        input_senha.setPlaceholderText('Digite sua senha')
        input_senha.setEchoMode(QLineEdit.EchoMode.Password)
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
