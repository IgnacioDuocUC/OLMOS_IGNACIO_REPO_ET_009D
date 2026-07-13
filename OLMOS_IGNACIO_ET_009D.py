#Examen de Fundamentos de Programación Ignacio Olmos
#Importaciones
import time
import sys

#Listas y diccionarios
#planes = {
#    'F001': ['nombre_plan': 'Plan Básico', 'tipo': 'mensual', 'duracion_meses': 1, 'acceso_piscina': False, 'incluye_clases': False, 'horario': 'libre'],
#    'F002': ['nombre_plan': 'Plan Full', 'tipo': 'mensual', 'duracion_meses': 1, 'acceso_piscina': True, 'incluye_clases': True, 'horario': 'libre'],
#    'F003': ['nombre_plan': 'Plan Estudiante', 'tipo': 'trimestral', 'duracion_meses': 3, 'acceso_piscina': False, 'incluye_clases': True, 'horario': 'tarde'],
#    'F004': ['nombre_plan': 'Plan Senior', 'tipo': 'trimestral', 'duracion_meses': 3, 'acceso_piscina': True, 'incluye_clases': False, 'horario': 'mañana'],
#    'F005': ['nombre_plan': 'Plan Anual Pro', 'tipo': 'anual', 'duracion_meses': 12, 'acceso_piscina': True, 'incluye_clases': True, 'horario': 'libre'],
#    'F006': ['nombre_plan': 'Plan Nocturno', 'tipo': 'mensual', 'duracion_meses': 1, 'acceso_piscina': False, 'incluye_clases': True, 'horario': 'noche']
#}
#código sin utilizar, tiene fallos.

planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
}


inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15]
}



#Funciones
def Bievenida():
    print('Bienvenido al sistema de gestión de cupos de FitPass')
    time.sleep(1)

def LeerOpcion():
    print('========== MENÚ PRINCIPAL ==========')
    print('1. Cupos por tipo de plan.')
    print('2. Búsqueda de planes por rango de precio.')
    print('3. Actualizar precio de plan.')
    print('4. Agregar plan.')
    print('5. Eliminar plan.')
    print('6. Salir.')

def cupos_Tipo(tipo):
    opcion = input()
    tipo == planes['F001']
    if opcion == 1:
        print('Los planes disponibles son: ', planes)

def Salir():
    opcion = input()
    if opcion == 6:
        print('Programa finalizado.')
        sys.exit(0)

def busqueda_precio(p_min, p_max):
    p_min >= 0
    p_max <= 200000

def buscar_codigo(codigo):
