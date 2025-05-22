import math

# Limites do intervalo onde as funções estão definidas
a = 3
b = 12

# Várias funções para experimentar os métodos de integração
f1 = lambda x: math.log(1 + x) * math.sin(0.1 * x) / (x * (1 + x)) * math.exp(x)
f2 = lambda x: math.sin(x) * math.exp(x / 10) * math.cos(1 / x)
f3 = lambda x: x**2 + 2
f4 = lambda x: math.log(1 + x) * math.sin(0.1 * x) / (x * (1 + x)) * math.exp(x)  # Igual à f1
f5 = lambda x: math.exp(2 * x) - x**10

# Função valor absoluto (só para prática)
def abs(x):
    if x > 0:
        return x
    else:
        return -x

# 1. Trapézio simples
def trapezio_simples(f, c, d):
    return (d - c) * (f(c) + f(d)) / 2

# 2. Trapézio recursivo
def trapezio_recursivo(f, c, d, n):
    if n == 0:
        return trapezio_simples(f, c, d)
    else:
        meio = (c + d) / 2
        return trapezio_recursivo(f, c, meio, n-1) + trapezio_recursivo(f, meio, d, n-1)

# 3. Trapézio iterativo (mais simples)
def trapezio_iterativo(f, c, d, n):
    partes = 2**n
    h = (d - c) / partes
    soma = 0

    for i in range(partes):
        x0 = c + i * h
        x1 = x0 + h
        soma += trapezio_simples(f, x0, x1)

    return soma

# 4. Força bruta: para quando o resultado para de mudar
def trapezio_forca_bruta(f, c, d, max_n=50, tol=1e-10):
    anterior = trapezio_iterativo(f, c, d, 0)

    for n in range(1, max_n):
        atual = trapezio_iterativo(f, c, d, n)
        if abs(atual - anterior) < tol:
            return atual
        anterior = atual

    return None  # Não estabilizou

# 5. Simpson simples
def simpson_simples(f, c, d):
    meio = (c + d) / 2
    return (d - c) * (f(c) + 4 * f(meio) + f(d)) / 6

# 6. Simpson recursivo
def simpson_recursivo(f, c, d, n):
    if n == 0:
        return simpson_simples(f, c, d)
    else:
        meio = (c + d) / 2
        return simpson_recursivo(f, c, meio, n-1) + simpson_recursivo(f, meio, d, n-1)

# 7. Greedy: para quando Tn está perto de Tn-1 E de Sn
def trapezio_greedy(f, c, d, epsilon=1e-6, max_n=30):
    anterior = trapezio_iterativo(f, c, d, 0)

    for n in range(1, max_n):
        atual = trapezio_iterativo(f, c, d, n)
        sn = simpson_recursivo(f, c, d, n)

        if abs(atual - anterior) < epsilon and abs(atual - sn) < epsilon:
            return atual

        anterior = atual

    return None

# ----------------------------
# Testar as funções
# ----------------------------
if __name__ == "__main__":
    c = 3  # Início do subintervalo
    d = 12 # Fim do subintervalo

    print("Função f3(x) = x^2 + 2 no intervalo [3,12]")

    print("1. Trapézio simples:", trapezio_simples(f3, c, d))
    print("2. Trapézio recursivo (n=3):", trapezio_recursivo(f3, c, d, 3))
    print("3. Trapézio iterativo (n=3):", trapezio_iterativo(f3, c, d, 3))
    print("4. Força bruta:", trapezio_forca_bruta(f3, c, d))
    print("5. Simpson simples:", simpson_simples(f3, c, d))
    print("6. Simpson recursivo (n=3):", simpson_recursivo(f3, c, d, 3))
    print("7. Greedy (ε=1e-6):", trapezio_greedy(f3, c, d))
