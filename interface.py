## python -m auto_py_to_exe
import tkinter as tk
from tkinter import ttk
import calculoSimples

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora Estudantil")

# Definir tamanho da janela
root.geometry("300x500")

label_titulo = tk.Label(root, text="Calculadora Estudantil", font=("Arial", 18), anchor="center")
label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Campo de Entrada para os números  (Frame)
frame_inputs = tk.Frame(root)
frame_inputs.grid(row=3, column=0, padx=10, pady=10)

# Botão de Calcular (fora de exibir_campos para não ser removido)
botao_calcular = tk.Button(frame_inputs, text="Calcular", command=lambda: calcular_resultado())
botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

##label do resultado 

label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 14))
label_resultado.grid(row=4, column=0, padx=10, pady=10)


# Marca D'água (Label) TODO: Fixar no fim da tela.

marca_dagua = tk.Label(root, text="© 2025 Kayke Gonçalves de Sousa", fg="gray", font=("Arial", 8))
marca_dagua.grid(row=10, column=0, padx=10, pady=10)


## COMBOBOXES 

# Combobox 1
tipo_calculo_selecionado = ttk.Combobox(root, values=["Cálculos Simples"])

## TODO: INCLUIR ESSAS FUNÇÕES NO FUTURO: "Escolha uma categoria", "Geometria", "Estatística"

tipo_calculo_selecionado.grid(row=1, column=0, padx=10, pady=10)
tipo_calculo_selecionado.set("Escolha uma categoria")  # "placeholder" da combobox

# Criar a segunda ComboBox (para escolher a operação) fora da função para evitar recriação
operacao_selecionada = ttk.Combobox(root, values=[])
operacao_selecionada.grid(row=2, column=0, padx=10, pady=10)  # Alterado para row=2 para evitar sobreposição

def atualizar_operacoes(event):
    operacao_selecionada.set('')  # Limpa a seleção da segunda ComboBox
    operacao_selecionada.bind("<<ComboboxSelected>>", exibir_campos) ## Adiciona evento para exibir campos

    # Usa o .get() para buscar o valor selecionado na ComboBox anterior. 
    tipo_calculo = tipo_calculo_selecionado.get()

    # Altera as opções exibidas de acordo com o tipo de cálculo selecionado na primeira combobox.
    if tipo_calculo == "Cálculos Simples":
        operacao_selecionada['values'] = ["Adição", "Subtração", "Multiplicação", "Divisão"]
    elif tipo_calculo == "Geometria":
        operacao_selecionada['values'] = ["Área do Triângulo", "Perímetro do Triângulo"]
    elif tipo_calculo == "Estatística":
        operacao_selecionada['values'] = ["Média", "Mediana", "Moda"]
    else:
        operacao_selecionada['values'] = [""]

# Adicionar o evento para atualizar as opções da segunda ComboBox
tipo_calculo_selecionado.bind("<<ComboboxSelected>>", atualizar_operacoes)

    
def exibir_campos(event):
    operacao = operacao_selecionada.get()

    # Remover campos antigos antes de adicionar novos
    for widget in frame_inputs.winfo_children():
        if widget != botao_calcular:  # Evitar remover o botão de calcular
            widget.destroy()

    global entrada1, entrada2
    if operacao in ["Adição", "Subtração", "Multiplicação", "Divisão"]:
        tk.Label(frame_inputs, text="Número 1:").grid(row=0, column=0)
        entrada1 = tk.Entry(frame_inputs)
        entrada1.grid(row=0, column=1)

        tk.Label(frame_inputs, text="Número 2:").grid(row=1, column=0)
        entrada2 = tk.Entry(frame_inputs)
        entrada2.grid(row=1, column=1)

        # Atualizar o botão de calcular após os campos estarem definidos
        botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Cálculo do Resultado
def calcular_resultado():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
    except ValueError:
        tk.messagebox.showerror("Erro", "Por favor, insira apenas números válidos.")
        return 
        
    tipoCalculo = tipo_calculo_selecionado.get()
    tipoOperacao = operacao_selecionada.get()

    if(tipoCalculo == "Cálculos Simples"):
        if(tipoOperacao == "Adição"):
            resultado = calculoSimples.adicao(num1, num2)
        elif(tipoOperacao == "Subtração"):
            resultado = calculoSimples.subtracao(num1, num2)
        elif(tipoOperacao == "Multiplicação"):
            resultado = calculoSimples.multiplicacao(num1, num2)    
        elif(tipoOperacao == "Divisão"):    
            resultado = calculoSimples.divisao(num1, num2)
        
        
        
        
    if resultado is not None:
            label_resultado.config(text=f"Resultado: {resultado}")
    else:
            label_resultado.config(text="Operação inválida ou incompleta.")
# Rodar a interface
root.mainloop()
