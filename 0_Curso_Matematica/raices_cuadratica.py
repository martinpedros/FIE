# ###################################################################################
#
# Martin Pedros
# Dados los coeficientes de una funcion cuadratica: a, b y c; calcula las raices si
# existen: f(x) = a*x^2 + b*x + c
#
# ###################################################################################

def raiz(a, b, c):
    return ((-b+(b**2-4*a*c)**(1/2))/2*a)

print('\n##################################################')
print('Calculo de raices de una Parabola')
print('##################################################')

a = int(input('\nIngrese coeficiente cuadratico: '))
b = int(input('Ingrese coeficiente lineal: '))
c = int(input('Ingrese termino independiente: '))

if ((b**2-4*a*c) >= 0):
    print(f'\nUna raiz de f(x) = a*(x)^2 + b*x + c: {raiz(a, b, c)}\n')
else:
    print('\n##################################################')
    print('No hay raices reales')
    print('##################################################\n')
