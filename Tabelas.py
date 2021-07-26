import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Programa') # Define manualmente o título da janela.
        self.setGeometry(150, 150, 500, 500) # Por justaposição, o primeiro parâmetro define a distância em pixels da lateral esquerda da tela até a janela, seguido do segundo parâmetro que define a distância em pixels do topo da tela até a borda superior da janela. Na sequência os dois últimos parâmetros se referem a largura e a altura da janela, respectivamente.
        self.Interface() # Instancia o método de classe Interface()

    def Interface(self):
        layout = QVBoxLayout()

        self.tabela = QTableWidget() # Irá gerar campo primitivo para inserção de linhas, colunas e dados para uma tabela
        self.tabela.setRowCount(10) # Insere na tabela um índice numerado à esquerda, com o número de linhas definido no parâmetro
        self.tabela.setColumnCount(4) # Insere na tabela o número de colunas definido no parâmetro, e a partir deste ponto automaticamente já temos uma tabela funcional onde é possível selecionar com o mouse uma linha, ou uma coluna, ou apenas uma célula
        self.tabela.setHorizontalHeaderItem(0, QTableWidgetItem('Nome'))
        self.tabela.setHorizontalHeaderItem(1, QTableWidgetItem('Idade'))
        self.tabela.setHorizontalHeaderItem(2, QTableWidgetItem('Telefone'))
        self.tabela.setHorizontalHeaderItem(3, QTableWidgetItem('E-mail'))

        botao1 = QPushButton('Salvar')
        botao1.clicked.connect(self.salva_dados)

        self.tabela.setItem(0, 0, QTableWidgetItem('Fernando')) # Insere na linha 0, coluna 0, o elemento 'Fernando'
        self.tabela.setItem(0, 1, QTableWidgetItem('34'))
        self.tabela.setItem(0, 2, QTableWidgetItem('55991357259'))
        self.tabela.setItem(0, 3, QTableWidgetItem('fernando2rad@gmail.com'))
        self.tabela.setItem(2, 0, QTableWidgetItem('Maria')) # Insere na terceira linha, na primeira coluna, o nome 'Maria'

        #self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers) # Define a regra para que nenhum elemento da tabela possa ser modificado via interface gráfica
        
        self.tabela.doubleClicked.connect(self.instancia_elemento)

        layout.addWidget(self.tabela)
        layout.addWidget(botao1)

        self.setLayout(layout)
        self.show()

    def instancia_elemento(self):
        for dado in self.tabela.selectedItems():
            print(f'O elemento {dado.text()} está localizado na linha {dado.row()} e na coluna {dado.column()}.')


    def salva_dados(self):
        base = []
        for dado in self.tabela.selectedItems(): # Salva na base apenas os elementos que estiverem selecionados na tabela. Se der um Ctrl + A e salvar, salva toda a tabela, inclusive as células em branco
            base.append(dado)
            #print(base) # Retornará apenas a referência para cada objeto alocado em memória
            print(f'O elemento {dado.text()} está localizado na linha {dado.row()} e na coluna {dado.column()}.')

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
