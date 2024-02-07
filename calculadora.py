import tkinter as tk
from tkinter import ttk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resultado = 0
        self.operacao = None
        self.memoria = 0

        self.inicializar_interface()

    def inicializar_interface(self):
        self.geometry("570x250")  # Define as dimensões da janela
        self.title("Calculadora")
        self.resizable(width=False, height=False)  # Impede o redimensionamento da janela

        self.criar_componentes()

    def criar_componentes(self):
        self.tela = ttk.Entry(self, font=("Arial", 20))
        self.tela.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        botoes_numericos = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("0", 4, 0),
        ]

        botoes_operacao = [
            ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3)
        ]

        for numero, row, column in botoes_numericos:
            btn = ttk.Button(self, text=numero, command=lambda num=numero: self.atualizar_tela(num))
            btn.grid(row=row, column=column, padx=5, pady=5, sticky="ew")

        for operacao, row, column in botoes_operacao:
            btn = ttk.Button(self, text=operacao, command=lambda op=operacao: self.realizar_operacao(op))
            btn.grid(row=row, column=column, padx=5, pady=5, sticky="ew")

        btn_igual = ttk.Button(self, text="=", command=self.calcular_resultado)
        btn_igual.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

        btn_limpar = ttk.Button(self, text="C", command=self.limpar)
        btn_limpar.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        self.configurar_estilos()

    def configurar_estilos(self):
        style = ttk.Style(self)
        style.configure("TButton", font=("Arial", 14))

    def atualizar_tela(self, valor):
        self.tela.insert(tk.END, valor)

    def realizar_operacao(self, operacao):
        self.operacao = operacao
        self.memoria = float(self.tela.get())
        self.tela.delete(0, tk.END)
        self.atualizar_tela(str(self.memoria) + " " + operacao + " ")

    def calcular_resultado(self):
        expressao = self.tela.get()
        operador = self.operacao
        partes = expressao.split(operador)

        if len(partes) != 2:
            self.tela.insert(tk.END, "Erro de expressão")
            return

        primeiro_numero = float(partes[0].strip())
        segundo_numero = float(partes[1].strip())

        self.tela.delete(0, tk.END)

        if operador == "+":
            self.resultado = primeiro_numero + segundo_numero
        elif operador == "-":
            self.resultado = primeiro_numero - segundo_numero
        elif operador == "*":
            self.resultado = primeiro_numero * segundo_numero
        elif operador == "/":
            if segundo_numero != 0:
                self.resultado = primeiro_numero / segundo_numero
            else:
                self.tela.insert(tk.END, "Erro: Divisão por zero")
                return

        self.tela.insert(tk.END, str(self.resultado))

    def limpar(self):
        self.tela.delete(0, tk.END)
        self.resultado = 0
        self.operacao = None
        self.memoria = 0

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
