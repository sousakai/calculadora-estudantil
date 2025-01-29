import tkinter as tk
from tkinter import ttk

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora Estudantil")

# Definir tamanho da janela
root.geometry("400x500")

label_titulo = tk.Label(root, text="Calculadora Estudantil", font=("Arial", 18), anchor="center")
label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
# Combobox 1
tipo_calculo_selecionado = ttk.Combobox(root, values=["Escolha uma categoria", "Cálculos Simples", "Geometria", "Estatística"])
tipo_calculo_selecionado.grid(row=1, column=0, padx=10, pady=10)
tipo_calculo_selecionado.set("Escolha uma categoria")  # "placeholder" da combobox

def atualizar_operacoes(event):
    operacao_selecionada.set('')  # Limpa a seleção da segunda ComboBox

# Usa o .get() para buscar o valor selecionado na ComboBox anterior. 
    tipo_calculo = tipo_calculo_selecionado.get()

#altera as opções exibidas de acordo com o tipo de cálculo selecionado na primeira combobox.
    if tipo_calculo == "Cálculos Simples":
        operacao_selecionada['values'] = ["Adição", "Subtração", "Multiplicação", "Divisão"]
    elif tipo_calculo == "Geometria":
        operacao_selecionada['values'] = ["Área do Triângulo", "Perímetro do Triângulo"]
    elif tipo_calculo == "Estatística":
        operacao_selecionada['values'] = ["Média", "Mediana", "Moda"]
    else:
        operacao_selecionada['values'] = [""]

    # Adicionar a segunda ComboBox (para escolher a operação)
    operacao_selecionada = ttk.Combobox(root, values=[])
    operacao_selecionada.grid(row=1, column=0, padx=10, pady=10)

    # Adicionar o evento para atualizar as opções da segunda ComboBox
    tipo_calculo_selecionado.bind("<<ComboboxSelected>>", atualizar_operacoes)
    
# Rodar a interface
root.mainloop()
