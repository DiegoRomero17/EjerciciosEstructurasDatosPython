'''
                            GRUPO DE TRABAJO PYGROUP
                            EJERCICIOS DE ESTRUCTURAS DE DATOS
                            DIEGO ANDRES ROMERO BLANCO - 20161020114

'''



'EJERCICIO #1'

DiasSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes","Sábado","Domingo"]
TuplaDias = ("Número no válido.",DiasSemana[0], DiasSemana[1], DiasSemana[2], DiasSemana[3], DiasSemana[4], DiasSemana[5],DiasSemana[6])
dia = int(input("¿Qué día de la semana deseas obtener? (1-7)"))
print("El día que corresponde al número ingresado es:"TuplaDias[dia])


'EJERCICIO #2'

Complejos = [4 + 3j, 3j, 8 * 6j, 5 - 5j, 5j]
MagnitudComplejo = [abs(elementos) for elementos in Complejos]
print("La magnitud es:",MagnitudComplejo)


'EJERCICIO #3'

Complejos = [4 + 3j, 3j, 8 + 6j, 5 - 5j, 5j]
ComplejoReal = [elementos.real for elementos in Complejos]
ComplejoImaginario = [elementos.imag for elementos in Complejos]
print("Lista de números complejos:",Complejos)
print("Parte real:",ComplejoReal)
print("Parte imaginaria:",ComplejoImaginario)


'EJERCICIO #4'

Vocales = ('a','e', 'i', 'o','u')
























