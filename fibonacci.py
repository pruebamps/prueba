# Funcion que genera numeros de la serie de Fibonacci
# Comentario para otra rama
def fibo(cantidad):
    a,b=0,1
    serie= list()
    for i in range(cantidad):
        serie.append(a)
        a,b=b,a+b
    return serie
cantidad= int(input("Indique la cantidad de numeros de la secuencia que desea generar: "))
print(fibo(cantidad))

