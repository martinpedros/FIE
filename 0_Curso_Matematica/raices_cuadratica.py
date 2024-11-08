def raiz(a, b, c):
    return ((-b+(b**2-4*a*c)**(1/2))/2*a)

a = int(input('Ingrese coeficiente cuadratico: '))
b = int(input('Ingrese coeficiente lineal: '))
c = int(input('Ingrese termino independiente: '))

if ((b**2-4*a*c) > 0):
    print(f'Una raiz de a(x): {raiz(a, b, c)}')
else:
    print(f'No hay raices reales')
