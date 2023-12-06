# Importar modulos
import empleFunc as f

# Declarar variables
seguir_en_programa = True

# 1 Leer los datos del archivo CSV y guardarlo como una lista de diccionarios. Cada diccionario debe representar un 
# empleado con llaves correspondientes al nombre de las columnas

f.leer_csv()

# Menú principal
while seguir_en_programa:
    print("")
    print("---> BIENVENIDO <---")
    print("Que desea hacer?")
    print("1. Ver el nombre de los empleados")
    print("2. Ver los departamentos con sus respectivos salarios totales")
    print("3. Ver el nombre del empleado con el mayor salario")
    print("4. Salir")
    print("")
    
    opcion = input("Seleccione una opción válida ")
    
    # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú
    if opcion.isdigit() == False:
        print("Seleccione un tipo de valor válido")
    else:
        opcion = int(opcion)

    if opcion == 1:
        f.get_employee_names()

    if opcion == 2:
        f.get_department_salaries()
    
    if opcion == 3:
        f.get_highest_paid_employee()

    if opcion == 4:
        seguir_en_programa = False
        print("Eso ha sido todo, vuelva pronto!")        
    else:
        print("Seleccione una opción válida.")
