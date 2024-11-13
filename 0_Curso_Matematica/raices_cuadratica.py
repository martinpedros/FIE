# ###################################################################################
#
# FIE (Facultad de Ingenieria del Ejercito)
# Materia: Taller de Introducción a la Matemática Universitaria
# Alumno: Martin Pedros
# Programa: Cálculo de raíces de una Parabola
#
# ###################################################################################

def raiz(a, b, c):
    """Calcula las raíces de una Parabola
    
    Dados los coeficientes de una funcion cuadratica: a, b y c; calcula las raices si
    existen de: f(x) = a*x^2 + b*x + c

    Args:
        a (int): coeficiente cuadratico
        b (int): coeficiente lineal
        a (int): termino independiente
    """
    raiz1 = (-b+(b**2-4*a*c)**(1/2))/2*a
    raiz2 = (-b-(b**2-4*a*c)**(1/2))/2*a
    return raiz1, raiz2

print('\n##################################################')
print('Calculo de raices de una Parabola')
print('##################################################')

a = int(input('\nIngrese coeficiente cuadratico: '))
b = int(input('Ingrese coeficiente lineal: '))
c = int(input('Ingrese termino independiente: '))

raiz1, raiz2 = raiz(a, b, c)

if ((b**2-4*a*c) >= 0):
    print(f'\nLas raíces de f(x) = a*(x)^2 + b*x + c son: {raiz1, raiz2}\n')
    
else:
    print('\n##################################################')
    print('No hay raices reales')
    print('##################################################\n')
