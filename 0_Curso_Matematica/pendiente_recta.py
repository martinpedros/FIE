# ###################################################################################
#
# Facu
# Materia: Taller de Introducción a la Matemática Universitaria
# Alumno: Martin Pedros
# Programa: Cálculo de la pendiente de una Recta
#
# Version: 1.0
# Fecha: 13/11/2024
#
# NOTA: Por el momento el programa no tienen deteccion de errores, por lo que los
# datos se deben ingresar correctamente, de lo contrario se debera volver a ejecutar
# dicho programa.
#
# ###################################################################################

def pendiente(x0, y0, x1, y1):
    """Calcula las pendiente de una Recta
    
    Dados los puntos P1(x0, y0) y P2(x1, y1), calcular la pendiente de una recta:
    pendiente = (y1 - y0) / (x1 - x0)

    Args:
        x0 (int): valor de x del punto P1
        y0 (int): valor de y del punto P1
        x1 (int): valor de x del punto P2
        y1 (int): valor de y del punto P2
    """
    return ((y1 - y0) / (x1 - x0))

x0 = int(input('Ingresar el valor de x del punto P1 (x0): '))
y0 = int(input('Ingresar el valor de y del punto P1 (y0): '))
x1 = int(input('Ingresar el valor de x del punto P2 (x1): '))
y1 = int(input('Ingresar el valor de y del punto P2 (y1): '))

print('\n##################################################')
print('Los puntos ingresados son')
print('##################################################')

print(f'El punto P1(x0, y0): ({x0},{y0})')
print(f'El punto P2(x1, y1): ({x1},{y1})')

print('\n##################################################')
print(f'La pendiente "a" es: {pendiente(x0, y0, x1, y1)}')
print('##################################################\n')
