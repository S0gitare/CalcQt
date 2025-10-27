def adicionar_numero(self, numero):

    if self.resetar_tela:
        self.valor_atual = numero
        self.resetar_tela = False
    else:
        if self.valor_atual == "0":
            self.valor_atual = numero
        else:
            self.valor_atual += numero

    atualizar_tela(self)


def limpar_tela(self):

    self.valor_atual = "0"
    self.operador = None
    atualizar_tela(self)


def backspace(self):

    if self.reseta_tela:
        self.limpar_tela()
        return

    self.valor_atual = self.valor_atual[:-1]
    if not self.valor_atual:
        self.valor_atual = "0"

    atualizar_tela(self)


def ponto_decimal(self):

    if self.resetar_tela:
        self.valor_atual = "0."
        self.resetar_tela = False
        self.atualizar_tela(self)
        return


def operacao(self, operador):

    if self.resetar_tela:
        self.resetar_tela = False

    if not self.valor_atual:
        self.valor_atual = "0"

    if self.valor_atual == "0" and operador == "-":
        self.valor_atual = "-"
        atualizar_tela(self)
        return

    last_char = self.valor_atual[-1]
    if last_char in ["+", "-", "*", "/"]:
        self.valor_atual = self.valor_atual[:-1] + operador
    else:
        self.valor_atual += operador
    atualizar_tela(self)


def calcular(self):
    expressao = self.valor_atual

    caracteres_permitidos = "0123456789+-*/.() "

    if any(char not in caracteres_permitidos for char in expressao):
        self.valor_atual = "Erro"
    else:
        try:
            resultado = eval(expressao)
            if resultado == int(resultado):
                self.valor_atual = str(int(resultado))
            else:
                self.valorr_atual = str(resultado)
        except:
            self.valor_atual = "Erro"
    self.resetar_tela = True
    atualizar_tela(self)


def atualizar_tela(self):
    self.ui.display.setText(self.valor_atual)
