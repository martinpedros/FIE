# ###################################################################################
#
# FIE (Facultad de Ingenieria del Ejercito)
# Materia: Taller de Introducción a la Matemática Universitaria
# Alumno: Martin Pedros
# Programa: Cálculo de sistemas lineales por método de determinantes de 2x2
#
# ###################################################################################

def solucion_x(a, b, c, d, e, f):
    """Cálculo de la variable (x) de un sistema lineal por método de determinantes de 2x2
    
    Ingresando los valores de "a", "b", "c", "d", "e" y "f"; se resuelve el sistema
    de ecuaciones de 2x2:
    
    Ecuación 1: (a)x + (b)y = (e) /
    Ecuación 2: (c)x + (d)y = (f)

    Args:
        x0 (int): valor de x de la ecuación 1
        y0 (int): valor de y de la ecuación 1
        term.ind.0 (int): valor del termino independiente de la ecuación 1
        x1 (int): valor de x de la ecuación 2
        y1 (int): valor de y de la ecuación 2
        term.ind.1 (int): valor del termino independiente de la ecuación 2
    """
    return ((d*e - b*f) / (a*d - b*c))

def solucion_y(a, b, e, c, d, f):
    """Cálculo de la variable (y) de un sistema lineal por método de determinantes de 2x2
    
    Ingresando los valores de "a", "b", "c", "d", "e" y "f"; se resuelve el sistema
    de ecuaciones de 2x2:
    
    Ecuación 1: (a)x + (b)y = (e) /
    Ecuación 2: (c)x + (d)y = (f)

    Args:
        x0 (int): valor de x de la ecuación 1
        y0 (int): valor de y de la ecuación 1
        term.ind.0 (int): valor del termino independiente de la ecuación 1
        x1 (int): valor de x de la ecuación 2
        y1 (int): valor de y de la ecuación 2
        term.ind.1 (int): valor del termino independiente de la ecuación 2
    """
    return ((a*f - c*e) / (a*d - c*b))

print('\n##################################################')
print('Los valores que debe ingresar a continuación son:')
print('##################################################\n')
print(f'Ecuación 1: (a)x + (b)y = (e)\n')
print(f'Ecuación 2: (c)x + (d)y = (f)\n')
print('##################################################\n')

a = int(input('\nIngresar el valor de x0 (a): '))
b = int(input('Ingresar el valor de y0 (b): '))
e = int(input('Ingresar el valor de termino independiente0 (e): '))
c = int(input('Ingresar el valor de x1 (c): '))
d = int(input('Ingresar el valor de y1 (d): '))
f = int(input('Ingresar el valor de termino independiente1 (f): '))

if (a*d - b*c) == 0:
    print('El sistema de ecuaciones no tiene solución en Numeros Reales')
else:
    print('\n##################################################')
    print('El sistema de ecuaciones ingresado es:')
    print('##################################################\n')
    print(f'Ecuación 1: {a}x + {b}y = {e}\n')
    print(f'Ecuación 2: {c}x + {d}y = {f}\n')
    print('\n##################################################')
    print('La solución del sistema es:')
    print('##################################################\n')
    print(f'x = {solucion_x(a, b, c, d, e, f)}, y = {solucion_y(a, b, e, c, d, f)}\n')
