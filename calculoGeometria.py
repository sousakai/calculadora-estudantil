PI = 3.14159

def areaTriangulo(a, b):
    area = (a * b) / 2
    return area

def perimetroTriangulo(a, b, c):
    return a + b + c

def tipoTriangulo(a, b, c):
    if a == b and b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def areaCirculo(r):
    return PI * pow(r, 2)

def perimetroCirculo(r):
    return 2 * PI * r

def teoremaPitagoras(a, b):
    return pow(a, 2) + pow(b, 2)


