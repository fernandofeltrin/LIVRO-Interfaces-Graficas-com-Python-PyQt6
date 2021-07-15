import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

fonte = QFont('Times', 12) # Primeiro parâmetro justaposto é a família da fonte, seguido do tamanho da fonte

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Programa') # Define manualmente o título da janela.
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(150, 150, 300, 278) # Por justaposição, o primeiro parâmetro define a distância em pixels da lateral esquerda da tela até a janela, seguido do segundo parâmetro que define a distância em pixels do topo da tela até a borda superior da janela. Na sequência os dois últimos parâmetros se referem a largura e a altura da janela, respectivamente.
        self.Interface() # Instancia o método de classe Interface()

    def Interface(self):
        texto1 = QLabel('Login: ', self) # Será criada uma linha de texto na posição inicial da janela, que por padrão é o canto superior esquerdo
        texto1.move(40, 10) # Define manualmente a posição onde texto1 será inserida, nesse caso, 100 pixels a partir da esquerda, 50 pixels a partir do topo. Se não definir este parâmetro para os labels, seus respectivos textos aparecerão sobrepostos. O Método move( ) serve para qualquer elemento visual da janela.

        botao1 = QPushButton('SAIR', self) # Será inserido um botão na posição inicial da janela (canto superior esquerdo) que neste momento ao clicar não realiza nenhuma ação, pois o botão inicial é apenas um botão, sem nada pré-configurado para o mesmo.
        botao1.move(117, 220)
        botao1.clicked.connect(self.confirma_saida)

        self.caixa_texto1 = QLineEdit(self) # Cria uma caixa de texto padrão para que o usuário digite alguma coisa
        self.caixa_texto1.setPlaceholderText('Digite seu nome de usuário')
        self.caixa_texto1.move(90, 8) # Define a posição da caixa de texto

        texto2 = QLabel('Senha: ', self)
        texto2.move(40, 34)
        self.caixa_texto2 = QLineEdit(self)
        self.caixa_texto2.setPlaceholderText('Digite sua senha')
        self.caixa_texto2.setEchoMode(QLineEdit.EchoMode.Password) # Irá esconder o conteúdo digitado, exibindo apenas asteriscos em seu lugar
        self.caixa_texto2.move(90, 32)

        self.salvar_checkbox = QCheckBox('Salvar informações', self) # Cria uma checkbox com a instrução ao lado
        self.salvar_checkbox.move(90, 74) # Define a posição da checkbox
        self.salvar_checkbox.clicked.connect(self.salva_dados) # Associa a checkbox como um botão ligado a função salva_dados( )

        self.seleciona_ambiente = QComboBox(self) # Cria uma caixa de seleção inicialmente vazia.
        self.seleciona_ambiente.move(90, 92) # Define a posição
        self.seleciona_ambiente.addItems(['Ambiente Comum',
                                          'Painel de Controle']) # addItems( ) suporte lista com todas as opções desejadas

        self.seleciona_tema1 = QRadioButton('Tema Claro', self) # Cria um botão de escolha única, inicialmente desmarcado
        self.seleciona_tema1.move(90, 54)
        self.seleciona_tema1.setChecked(True) # Define que inicialmente este botão já estará marcado
        self.seleciona_tema2 = QRadioButton('Tema Escuro', self) # Cria um segundo botão de escolha, que quando marcado, desmarca o botão 1
        self.seleciona_tema2.move(170, 54)

        botao2 = QPushButton('ENTRAR', self)
        botao2.setFont(fonte) # Aplica o estilo de fonte setado no escopo global do código.
        botao2.clicked.connect(self.salva_dados)  # Ao clicar, aciona a função salva_dados( )
        botao2.clicked.connect(self.sel_ambiente) # Ao clicar, aciona a função sel_ambiente( )
        botao2.clicked.connect(self.sel_tema) # Ao clicar, aciona a função sel_tema( )
        botao2.clicked.connect(self.envia_argumento) # Ao clicar, enviará o texto digitado pelo usuário para uma base de dados programada em enviar_argumento( )
        botao2.move(117, 114)

        botao_sobre = QPushButton('Sobre', self)
        botao_sobre.move(220, 250)
        botao_sobre.clicked.connect(self.sobre)

        # Caixa de controle de valor
        self.tamanho_fonte = QSpinBox(self) # Gera uma caixa de controle de valor
        self.tamanho_fonte.move(107, 250)
        texto_tamanho_fonte = QLabel('Tamanho da Fonte:', self)
        texto_tamanho_fonte.move(5, 253)
        self.tamanho_fonte.setMinimum(100) # Define o valor mínimo
        self.tamanho_fonte.setMaximum(150) # Define o valor máximo
        # pode ser reduzido por self.tamanho_fonte.setRange(1, 10)
        self.tamanho_fonte.setSuffix('%') # Define um sufixo que aparecerá junto ao valor
        self.tamanho_fonte.setSingleStep(10) # Define de quantos em quantos elementos os valores são exibidos
        self.tamanho_fonte.valueChanged.connect(self.tam_fonte)

        # Campo para inserção de texto
        self.texto = QTextEdit(self) # Cria um campo onde o usuário pode livremente digitar um texto
        self.texto.setFixedWidth(280)
        self.texto.setFixedHeight(40)
        self.texto.move(10, 158)
        # self.texto.setAcceptRichText() permite que no campo de texto seja colado um texto da área de transferência.
        argumentos = QLabel('Insira suas observações abaixo:', self)
        argumentos.move(10, 143)
        self.texto_checkbox = QCheckBox('Salvar observações', self)
        self.texto_checkbox.move(10, 198)

        self.show()

    def sair(self):
        sys.exit(qt.exec_()) # Aciona a função do sistema para fechar a janela principal do programa

    def sel_tema(self):
        if self.seleciona_tema1.isChecked(): # Se o botão de escolha estiver marcado em Tema Claro...
            print(f'Tema Claro escolhido')
        else:
            print(f'Tema Escuro Escolhido')

    def sel_ambiente(self):
        ambiente_selecionado = self.seleciona_ambiente.currentText() # currentText( ) recebe a opção selecionada da caixa de seleção
        print(f'O ambiente escolhido é: {ambiente_selecionado}')

    def salva_dados(self):
        if self.salvar_checkbox.isChecked(): # Caso a checkbox esteja marcada...
            base = []
            base.append(self.caixa_texto1.text()) # Recebe o texto digitado pelo usuário para Login
            base.append(self.caixa_texto2.text()) # Recebe o texto digitado pelo usuário para Senha
            print(f'Nome de usuário: {base[0]} \nSenha: {base[1]}')
        else:
            print(f'Usuário optou por não salvar os dados.')

    def confirma_saida(self):
        opcoes =  QMessageBox.critical(self,
                                       'ATENÇÃO',
                                       'Deseja mesmo sair?',
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        if opcoes == QMessageBox.StandardButton.Yes:
            sys.exit(qt.exec())
        if opcoes == QMessageBox.StandardButton.Cancel:
            pass

    def envia_argumento(self):
        if self.texto_checkbox.isChecked(): # Se a caixa de verificação estiver marcada...
            observacoes = []
            observacoes.append(self.texto.toPlainText()) # Recebe o texto digitado pelo usuario no campo de texto
            print('Observações salvas com sucesso.')
            print(f'{observacoes}')
        else:
            print('O usuário não inseriu nenhuma observação.')

    def sobre(self):
        sobre = QMessageBox.information(self, 'Meu Programa', 'Versão 1.0.2') # information gera uma janela de aviso simples, apenas com um botão OK que fecha tal janela

    def tam_fonte(self):
        valor = self.tamanho_fonte.value()
        fonte0 = QFont('Times', 10)
        fonte1 = QFont('Times', 11)
        fonte2 = QFont('Times', 12)
        fonte3 = QFont('Times', 13)
        fonte4 = QFont('Times', 14)
        fonte5 = QFont('Times', 15)
        if valor == 110:
            self.caixa_texto1.setFont(fonte1)
            self.caixa_texto2.setFont(fonte1)
        elif valor == 120:
            self.caixa_texto1.setFont(fonte2)
            self.caixa_texto2.setFont(fonte2)
        elif valor == 130:
            self.caixa_texto1.setFont(fonte3)
            self.caixa_texto2.setFont(fonte3)
        elif valor == 140:
            self.caixa_texto1.setFont(fonte4)
            self.caixa_texto2.setFont(fonte4)
        elif valor == 150:
            self.caixa_texto1.setFont(fonte5)
            self.caixa_texto2.setFont(fonte5)
        else:
            self.caixa_texto1.setFont(fonte0)
            self.caixa_texto2.setFont(fonte0)

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
