import calculoSimples;
import calculoEquacoes;

print("""Escolha o tipo de cálculo a ser realizado:\n 
      1. Cálculos Simples (4 operações)\n
      2. Equações""")

tipoCalculo = int(input())

if(tipoCalculo == 1): #calculo simples
    print("Qual operação você deseja utilizar?\n")
    print(" 1. Adição\n 2. Subtração\n 3. Multiplicação\n 4. Divisão\n")

    operacao = int(input("Digite o valor correspondente:\n"))

    a = int(input("Digite o primeiro valor a ser calculado:\n"))
    b = int(input("Digite o segundo valor a ser calculado:\n"))

    if(operacao == 1): #adição
        resultado = calculoSimples.adicao(a, b)
        print(resultado)
    
    if(operacao == 2): #subtração
        resultado = calculoSimples.subtracao(a, b)
        print(resultado)
    
    if(operacao == 3): #multiplicação
        resultado = calculoSimples.multiplicacao(a, b)
        print(resultado)
    
    if(operacao == 4): #divisão
        resultado = calculoSimples.divisao(a, b)
        print(resultado)

elif(tipoCalculo == 2): #equações
    print("""Equações suportadas:\n
          1. Cálculo de área do triângulo.
          2. Perímetro do triângulo.""")
    
    operacao = int(input())
    


    if(operacao == 1): #area do triangulo
        a = int(input("Digite o primeiro valor a ser calculado:\n"))
        b = int(input("Digite o segundo valor a ser calculado:\n"))
        resultado = calculoEquacoes.areaTriangulo(a, b)
        print(resultado)
    
    if(operacao == 2): #perímetro do triangulo
        a = int(input("Digite valor do primeiro lado a ser calculado:\n"))
        b = int(input("Digite valor do segundo lado a ser calculado:\n"))
        c = int(input("Digite valor do terceiro lado a ser calculado:\n"))
        
        resultado = calculoEquacoes.perimetroTriangulo(a, b, c)
        print(resultado)
    

    