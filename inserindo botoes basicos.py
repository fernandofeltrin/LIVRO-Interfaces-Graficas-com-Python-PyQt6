import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Programa') # Define manualmente o título da janela.
        self.setGeometry(150, 150, 500, 500) # Por justaposição, o primeiro parâmetro define a distância em pixels da lateral esquerda da tela até a janela, seguido do segundo parâmetro que define a distância em pixels do topo da tela até a borda superior da janela. Na sequência os dois últimos parâmetros se referem a largura e a altura da janela, respectivamente.
        self.Interface() # Instancia o método de classe Interface()

    def Interface(self):
        layout = QFormLayout()

        texto_usuario = QLabel('Usuário: ')
        input_usuario = QLineEdit()
        input_usuario.setPlaceholderText('Digite seu nome de usuário')
        texto_senha = QLabel('Senha: ')
        input_senha = QLineEdit()
        input_senha.setPlaceholderText('Digite sua senha')

        layout.addRow(texto_usuario, input_usuario) # Insere uma linha contendo o campo 'Usuário: ' seguido do campo para inserção de texto
        layout.addRow(texto_senha, input_senha) # Insere uma segunda linha, agora contendo os campos 'Senha: ' e o campo para inserção da senha
        layout.addRow(QLabel('Salvar Informações: '), QComboBox()) # Ao criar a linha, já insere na mesma um texto/label e um campo para seleção

        layout_secundario = QHBoxLayout() # Contornando o problema, podemos criar uma estrutura de layout secundária, de outro formato, para que possamos reorganizar os elementos
        layout_secundario.addStretch()
        layout_secundario.addWidget(QPushButton('ENTRAR')) # Dentro desse layout secundário criamos os botões que queremos
        layout_secundario.addWidget(QPushButton('SAIR'))
        layout_secundario.addStretch()
        layout.addRow(layout_secundario) # Instanciamos novamente o layout geral de nossa janela, incorporando na mesma, dentro de uma nova linha, o layout secundário e seus elementos.

        layout_terciario = QVBoxLayout()
        layout_terciario.addWidget(QLabel('Quando de memória deseja alocar?'))
        self.slider = QSlider(Qt.Horizontal) # Cria um slider genérico, caso não seja repassado nenhum parâmetro, será um slider vertical
        self.slider.setMinimum(20)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.valueChanged.connect(self.recebe_valor) # No caso de um slider, o método que conecta o gatilho para executar uma ação em uma função é valueChanged.connect( )
        self.valor = QLabel('0')
        self.valor.setAlignment(Qt.AlignCenter)
        layout_terciario.addWidget(self.valor)
        layout_terciario.addWidget(self.slider)

        layout.addRow(layout_terciario)

        self.setLayout(layout)
        self.show()

    def recebe_valor(self):
        val_escolhido = self.slider.value()
        self.valor.setText(str(val_escolhido))
        print(f'Valor escolhido: {val_escolhido}%')

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec_())
