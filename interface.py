import tkinter as tk
from tkinter import ttk, messagebox
import calculoSimples
import calculoGeometria

# Configurações da janela principal

root = tk.Tk() #abre a tela
root.title("Calculadora Estudantil") # nome da aba
root.geometry("300x500") # tamanho da janela
root.configure(bg="#a6a4a4")  # cor de fundo


# Título 
label_titulo = tk.Label(root, text="Calculadora Estudantil", font=("Times New Roman", 18, "italic"), anchor="center", width=20, bg=root.cget('bg'))
label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")


# Campo de Entrada para os números  (Frame)
frame_inputs = tk.Frame(root)
frame_inputs.grid(row=3, column=0, padx=10, pady=10)

# Botão de Calcular (fora de exibir_campos para não ser removido)
botao_calcular = tk.Button(frame_inputs, text="Calcular", command=lambda: calcular_resultado(),
    bg="#525050", fg="white",  # bg: cor de fundo; fg: cor da fonte
                           font=("Helvetica", 10, "bold"),  # Fonte do botão;
                           bd=0,  # Visibilidade da borda;
                           relief="raised",  # Estilo de borda 
                           highlightthickness=3,  # Espessura da borda
                           activebackground="black",  # Cor quando o botão for pressionado
                           activeforeground="white")  # Cor do texto quando pressionado
                            


# md: Coloquei o botão fora do 'frame_inputs' para evitar sobreposição
botao_calcular.grid(row=4, column=0, columnspan=2, pady=0)


##label do resultado 

label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 14), bg=root.cget('bg'))
label_resultado.grid(row=4, column=0, padx=10, pady=10)



#marca d'água
marca_dagua = tk.Label(root, text="© 2025 Kayke Gonçalves de Sousa", fg="gray", font=("Arial", 8), bg=root.cget('bg'))
marca_dagua.grid(row=10, column=0, padx=10, pady=10)


## COMBOBOXES 

# Combobox 1
tipo_calculo_selecionado = ttk.Combobox(root, values=["Cálculos Simples", "Geometria"])

## TODO: INCLUIR ESSAS FUNÇÕES NO FUTURO: "Escolha uma categoria", "Estatística"

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

    global entrada1, entrada2, entrada3  # Declarar variáveis globais para serem acessadas em calcular_resultado()
    
    if operacao in ["Adição", "Subtração", "Multiplicação", "Divisão"]:
        tk.Label(frame_inputs, text="Número 1:").grid(row=0, column=0)
        entrada1 = tk.Entry(frame_inputs)
        entrada1.grid(row=0, column=1)

        tk.Label(frame_inputs, text="Número 2:").grid(row=1, column=0)
        entrada2 = tk.Entry(frame_inputs)
        entrada2.grid(row=1, column=1)

        # Atualizar o botão de calcular após os campos estarem definidos
        botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)
    
    elif operacao == "Área do Triângulo":
        tk.Label(frame_inputs, text="Base:").grid(row=0, column=0)
        entrada1 = tk.Entry(frame_inputs)
        entrada1.grid(row=0, column=1)

        tk.Label(frame_inputs, text="Altura:").grid(row=1, column=0)
        entrada2 = tk.Entry(frame_inputs)
        entrada2.grid(row=1, column=1)
        
    elif operacao == "Perímetro do Triângulo":
        tk.Label(frame_inputs, text="Lado 1:").grid(row=0, column=0)
        entrada1 = tk.Entry(frame_inputs)
        entrada1.grid(row=0, column=1)
        
        tk.Label(frame_inputs, text="Lado 2:").grid(row=1, column=0)
        entrada2 = tk.Entry(frame_inputs)
        entrada2.grid(row=1, column=1)
        
        tk.Label(frame_inputs, text="Lado 3:").grid(row=2, column=0)
        entrada3 = tk.Entry(frame_inputs)
        entrada3.grid(row=2, column=1)

    # *md: Botão de calcular em posição fixa**
    botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

# Cálculo do Resultado
def calcular_resultado():
    try:
        num1 = float(entrada1.get())  # Obtém o primeiro número
        num2 = float(entrada2.get())  # Obtém o segundo número

        # *md: Verificação antes de acessar entrada3**
        if 'entrada3' in globals() and entrada3.winfo_exists():
            num3 = float(entrada3.get())  # Obtém o terceiro número, se existir
        else:
            num3 = None  # Define como None se não existir

    except ValueError:
        tk.messagebox.showerror("Erro", "Por favor, insira apenas números válidos.")
        return 
        
    tipoCalculo = tipo_calculo_selecionado.get()
    tipoOperacao = operacao_selecionada.get()

    if tipoCalculo == "Cálculos Simples":
        if tipoOperacao == "Adição":
            resultado = calculoSimples.adicao(num1, num2)
        elif tipoOperacao == "Subtração":
            resultado = calculoSimples.subtracao(num1, num2)
        elif tipoOperacao == "Multiplicação":
            resultado = calculoSimples.multiplicacao(num1, num2)    
        elif tipoOperacao == "Divisão":    
            resultado = calculoSimples.divisao(num1, num2)
    
    elif tipoCalculo == "Geometria":
        if tipoOperacao == "Área do Triângulo":
            resultado = calculoGeometria.areaTriangulo(num1, num2)
        elif tipoOperacao == "Perímetro do Triângulo":
            
            # *md: Usa num3 apenas se não for None**
            if num3 is not None:
                resultado = calculoGeometria.perimetroTriangulo(num1, num2, num3)
            else:
                tk.messagebox.showerror("Erro", "Todos os lados devem ser informados para calcular o perímetro.")
                return
            
    if resultado is not None:
        label_resultado.config(text=f"Resultado: {resultado}")
    else:
        label_resultado.config(text="Operação inválida ou incompleta.")

# Rodar a interface
root.mainloop()
