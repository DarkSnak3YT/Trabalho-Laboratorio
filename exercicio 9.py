# 9º Exercício
def TiDinamico(f, c, d, epsilon, n=0):
    """
    Calcula a integral de f de c a d usando integração adaptativa:
    Subdivide apenas quando T e S diferem mais do que epsilon/2^(n+1).
    """
    # Condição de subdivisão
    Tval = T(f, c, d)
    Smid = S(f, c, (c + d)/2)
    if abs(Tval - Smid) < epsilon / (2**(n+1)):
        return Tval
    else:
        # Subdivide recursivamente o intervalo
        meio = (c + d)/2
        esquerda = TiDinamico(f, c, meio, epsilon, n+1)
        direita = TiDinamico(f, meio, d, epsilon, n+1)
        return esquerda + direita

'''
# TEST 9:
c = float(input("Limite esquerda: "))
d = float(input("Limite direita: "))
epsilon = float(input("Precisão (epsilon): "))
f = input("A função: ")
print("TiDinamico(",f,",",c,",",d,",",epsilon,") =", TiDinamico(eval(f), c, d, epsilon))
'''
