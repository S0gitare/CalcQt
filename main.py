import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6 import QtUiTools
from PySide6.QtWidgets import QPushButton
import functions


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load("layout.ui", self)

        self.valor_atual = "0"
        self.resetar_tela = False

        for i in range(10):
            btn = self.ui.findChild(QPushButton, f"btn{i}")
            if btn:
                btn.clicked.connect(
                    lambda checked, x=str(i): functions.adicionar_numero(self, str(x))
                )
            else:
                print(f"Botão btn{i} não encontrado!")

        btn_limpar = self.ui.findChild(QPushButton, "btnLimpar")
        if btn_limpar:
            btn_limpar.clicked.connect(lambda: functions.limpar_tela(self))
        else:
            print("Botão btnLimpar não encontrado!")

        btn_backspace = self.ui.findChild(QPushButton, "btnBackspace")
        if btn_backspace:
            btn_backspace.clicked.connect(lambda: functions.backspace(self))
        else:
            print("Botão btnBackspace não encontrado!")

        btn_ponto = self.ui.findChild(QPushButton, "btnPonto")
        if btn_ponto:
            btn_ponto.clicked.connect(lambda: functions.ponto_decimal(self))
        else:
            print("Botão btnPonto não encontrado!")

        operadores = {
            "btnAdicao": "+",
            "btnSubtracao": "-",
            "btnMultiplicacao": "*",
            "btnDivisao": "/",
        }

        for btn_name, operador in operadores.items():
            btn = self.ui.findChild(QPushButton, btn_name)
            if btn:
                btn.clicked.connect(
                    lambda checked, op=operador: functions.operacao(self, op)
                )
            else:
                print(f"Botão {btn_name} não encontrado!")

        btn_igual = self.ui.findChild(QPushButton, "btnIgual")
        if btn_igual:
            btn_igual.clicked.connect(lambda: functions.calcular(self))
        else:
            print("Botão btnIgual não encontrado!")

        functions.atualizar_tela(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Calculadora()
    janela.ui.show()
    sys.exit(app.exec())
