# ###################################################################################
#
# Martin Pedros
# Dados los puntos P1(x0, y0) y P2(x1, y1), calcular la pendiente de una recta:
# pendiente = (y1 - y0) / (x1 - x0)
#
# ###################################################################################

def pendiente(x0, y0, x1, y1):
    return ((y1 - y0) / (x1 - x0))

x0 = int(input('Ingresar el valor de x del punto P1 (x0): '))
y0 = int(input('Ingresar el valor de y del punto P1 (y0): '))
x1 = int(input('Ingresar el valor de x del punto P2 (x1): '))
y1 = int(input('Ingresar el valor de y del punto P2 (y1): '))

print('##################################################')
print('Los puntos ingresados son')
print('##################################################')

print(f'El punto P1(x0, y0): ({x0},{y0})')
print(f'El punto P2(x1, y1): ({x1},{y1})')

print('\n##################################################')
print(f'La pendiente "a" es: {pendiente(x0, y0, x1, y1)}')
print('##################################################\n')
