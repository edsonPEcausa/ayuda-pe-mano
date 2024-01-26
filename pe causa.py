class Usuario:
    def __init__(self, nombre, apellidos, edad, asignatura, rol, seccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.asignatura = asignatura
        self.rol = rol
        self.seccion = seccion
        self.notas = [0]
    
    asignaturas = [ "PROGRAMACION", "BASE DE DATOS", "ANALISIS-PROGRAMACION", "BASE DE DATOS-ANALISIS", "PROGRAMACION-BASE DE DATOS"]

usuarios_registrados = [
    {"nombre": "JORGE", "apellido": "ALIAGA", "edad": 31, "asignatura": "ANALISIS", "rol": "ESTUDIANTE", "secciones": ["61"]},
    {"nombre": "RAMIRO", "apellido": "ALVAREZ", "edad": 22, "asignatura": "ANALISIS", "rol": "ESTUDIANTE", "secciones": ["61"]},
    {"nombre": "JUAN", "apellido": "AYALA", "edad": 28, "asignatura": "ANALISIS", "rol": "ESTUDIANTE", "secciones": ["62"]},
    {"nombre": "MIGUEL", "apellido": "BRAVO", "edad": 36, "asignatura": "PROGRAMACION", "rol": "ESTUDIANTE", "secciones": ["61"]},
    {"nombre": "CRISTIAN", "apellido": "BUSTOS", "edad": 34, "asignatura": "PROGRAMACION", "rol": "ESTUDIANTE", "secciones": ["61"]},
    {"nombre": "EDUARDO", "apellido": "DOMINGUEZ", "edad": 26, "asignatura": "PROGRAMACION", "rol": "ESTUDIANTE", "secciones": ["61"]},
    {"nombre": "CRISTHIAN", "apellido": "ECHEVERRÍA", "edad": 38, "asignatura": "PROGRAMACION", "rol": "ESTUDIANTE", "secciones": ["61"]},
    {"nombre": "NICOLAS", "apellido": "ESPINOZA", "edad": 33, "asignatura": "PROGRAMACION", "rol": "ESTUDIANTE", "secciones": ["62"]},
    {"nombre": "JAVIER", "apellido": "FIGUEROA", "edad": 31, "asignatura": "BASE DE DATOS", "rol": "ESTUDIANTE", "secciones": ["62"]},
    {"nombre": "FRANKLIN", "apellido": "MARTINEZ", "edad": 20, "asignatura": "BASE DE DATOS", "rol": "ESTUDIANTE", "secciones": ["1"]},
    {"nombre": "FRANCISCO", "apellido": "MEDINA", "edad": 28, "asignatura": "BASE DE DATOS", "rol": "ESTUDIANTE", "secciones": ["1"]},
    {"nombre": "OMAR", "apellido": "MENA", "edad": 33, "asignatura": "BASE DE DATOS", "rol": "ESTUDIANTE", "secciones": ["2"]},
    {"nombre": "SAMUEL", "apellido": "MENDOZA", "edad": 34, "asignatura": "BASE DE DATOS", "rol": "ESTUDIANTE", "secciones": ["2"]},
  
]
profesores_registrados = [
     {"nombre": "PATRICIO", "apellido": "VERGARA", "edad": 33, "asignatura": "ANALISIS - PROGRAMACION", "rol": "PROFESOR", "secciones": ["61", "62"]},
    {"nombre": "DIEGO", "apellido": "YAÑEZ", "edad": 40, "asignatura": "BASE DE DATOS - ANALISIS", "rol": "PROFESOR", "secciones": ["62", "1", "2"]},
    {"nombre": "FELIPE", "apellido": "ARAYA", "edad": 40, "asignatura": "PROGRAMACIÓN - BASE DE DATOS", "rol": "PROFESOR", "secciones": ["62", "1", "2"]},
]

def ingresar_usuario():
    print("\nIngresar Usuario:")
    nombre = input("Ingrese el nombre del usuario: ")
    apellidos = input("Ingrese los apellidos del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))
    asignatura = input("Ingrese la asignatura: ")
    rol = input("Ingrese el rol del usuario (profesor/alumno): ").lower()
    seccion = input("Ingrese la sección: ")
    
    for usuario in usuarios_registrados:
        if usuario["nombre"] == nombre and usuario["apellidos"] == apellidos:
            print("El usuario ya se encuentra registrado.")
            return
        
    
    nuevo_usuario = Usuario(nombre, apellidos, edad, asignatura, rol, seccion)
    usuarios_registrados.append(nuevo_usuario)
    print(f"Usuario {rol} agregado con éxito.")
    
    
    def mostrar_usuarios():
        print("\nLista de Usuarios:")
    for usuario in usuarios_registrados:
        print("\nNombre:", usuario.nombre)
        print("Apellidos:", usuario.apellidos)
        print("Edad:", usuario.edad)
        print("Asignatura:", usuario.asignatura)
        print("Rol:", usuario.rol)
        print("Sección:", usuario.seccion)
        print("\nFin de la lista.")



    for profesor in profesores_registrados:
        if (
            profesor["nombre"] == profesores_registrados["nombre"]
            and profesor["apellido"] == apellidos
            and profesor["asignatura"] == asignatura
            and seccion in profesor["secciones"]
        ):
            print("Profesor validado con éxito.")
            return True

    print("Profesor no validado. Verifique sus credenciales.")
    return False



def ingresar_notas():
    if not  validar_docente():
       return
    asignatura = input("Ingrese la asignatura:")
    seccion = input("Ingrese la seccion:")
    
    print ("\n=========LISTA DE ALUMNOS=========")
    for alumno in usuarios_registrados:
        if(
            alumno.rol == "ESTUDIANTE"
            and alumno.asignatura == asignatura
            and seccion in alumno.seccion
        ):
            
            print("\nNombre: {alumno.nombre} {alumno.apellidos}")
             
            nota1 = float(input("Ingrese Nota 1 (35%): "))
            nota2 = float(input("Ingrese Nota 2 (35%): "))
            nota3 = float(input("Ingrese Nota 3 (30%): "))
            promedio = (nota1 * 0.35) + (nota2 * 0.35) + (nota3 * 0.3)
            alumno.notas.append({"asignatura": asignatura, "promedio": promedio})
     
            print("\n Notas ingresadas con éxito.")
            


def actualizar_alumno():
   
    if not profesores_registrados():
        return

    nombre_alumno = input("Ingrese el nombre del alumno que desea actualizar: ")
    apellido_alumno = input("Ingrese el apellido del alumno que desea actualizar: ")

    alumno_encontrado = None
    for alumno in usuarios_registrados:
        if (
            alumno["rol"] == "ESTUDIANTE"
            and alumno["nombre"] == nombre_alumno
            and alumno["apellidos"] == apellido_alumno
        ):
            alumno_encontrado = alumno
            break

    if alumno_encontrado is None:
        print("El alumno no existe.")
        return

    print("\nDatos del Alumno:")
    print(f"Nombre: {alumno_encontrado.nombre} {alumno_encontrado.apellidos}")
    print(f"Sección: {alumno_encontrado.seccion}")
    print(f"Asignatura: {alumno_encontrado.asignatura}")

    if (
         validar_docente()
        and alumno_encontrado.asignatura == profesores_registrados.asignatura
        and alumno_encontrado.seccion == profesores_registrados.seccion
    ):
        confirmacion = input("¿Está seguro de actualizar este alumno? (s/n): ").lower()
        if confirmacion == "s":
            # Actualizar datos del alumno
            nuevo_nombre = input("Nuevo nombre del alumno: ")
            nuevo_apellido = input("Nuevo apellido del alumno: ")
            nueva_seccion = input("Nueva sección del alumno: ")
            nueva_asignatura = input("Nueva asignatura del alumno: ")

            # Actualizar datos
            alumno_encontrado.nombre = nuevo_nombre
            alumno_encontrado.apellidos = nuevo_apellido
            alumno_encontrado.seccion = nueva_seccion
            alumno_encontrado.asignatura = nueva_asignatura

            print("Alumno actualizado con éxito.")
        else:
            print("Actualización cancelada.")
    else:
       print("No tiene permisos para actualizar a este alumno.")






def eliminar_alumno():
    docente = validar_docente()
    if docente:
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        apellidos = input("Ingrese los apellidos del alumno a eliminar: ")

        alumno_encontrado = None
        for usuario in usuarios_registrados:
            if (
                usuario.rol == 'ALUMNO' 
                and usuario.nombre == nombre 
                and usuario.apellidos == apellidos
                and docente.asignatura == usuario.asignatura
                
            ): 
                alumno_encontrado = usuario
                break

        if alumno_encontrado:
            if docente.seccion == alumno_encontrado.seccion and docente.asignatura == alumno_encontrado.asignatura:
                print("\nDatos del alumno" ,  nombre , apellidos , "a eliminar:")
                print("Sección: ", alumno_encontrado.seccion)
                print("Asignatura:", alumno_encontrado.asignatura)
                print("Edad:" ,alumno_encontrado.edad)

                confirmacion = input("¿Está seguro de eliminar este alumno? (SI/NO): ").upper()
                if confirmacion == "SI":
                    usuarios_registrados.remove(alumno_encontrado)
                    print("Alumno eliminado con éxito.")
                else:
                    print("Eliminación cancelada.")
            else:
                print("No tiene permisos para eliminar a este alumno.")
        else:
            print("Alumno no encontrado o no tiene permiso para eliminarlo.")

def listar_por_secciones():
    docente = validar_docente()
    if docente:
        seccion = input("Ingrese la sección a listar: ")
        asignatura = input("Ingrese la asignatura (opcional): ")

        alumnos_seccion = [u for u in usuarios_registrados if u.rol == 'alumno' and u.seccion == seccion and (not asignatura or u.asignatura == asignatura)]

        if alumnos_seccion:
            print("\nLista de Alumnos:")
            for alumno in alumnos_seccion:
                print("\nNombre: " ,alumno.nombre, alumno.apellidos)
                print("Sección:" ,alumno.seccion)
                print("Asignatura:",alumno.asignatura)
                if hasattr(alumno, 'notas'):
                    print("Notas: ", alumno.notas)
                else:
                    print("Notas: No ingresadas")
            print("\nDocente a cargo: " ,docente.nombre, docente.apellidos)
        else:
            print("No hay alumnos en la sección o asignatura especificada.")

def mostrar_por_alumnos():
    docente = validar_docente()
    if docente:
        nombre = input("Ingrese el nombre del alumno a mostrar: ")
        apellidos = input("Ingrese los apellidos del alumno a mostrar: ")

        alumno_encontrado = None
        for usuario in usuarios_registrados:
            if usuario["rol"] == 'alumno' and usuario.nombre == nombre and usuario.apellidos == apellidos:
                alumno_encontrado = usuario
                break

        if alumno_encontrado:
            if docente.seccion == alumno_encontrado.seccion and docente.asignatura == alumno_encontrado.asignatura:
                print("\nDatos del alumno ", nombre, apellidos ,":")
                print("Sección: " ,alumno_encontrado.seccion)
                print("Asignatura: " , alumno_encontrado.asignatura)
                if hasattr(alumno_encontrado, 'notas'):
                    print("Notas:" ,alumno_encontrado.notas)
                else:
                    print("Notas: No ingresadas")
            else:
                print("No tiene permisos para mostrar a este alumno.")
        else:
            print("Alumno no encontrado.")

def mostrar_por_docentes():
    docente = validar_docente()
    if docente:
        print("\nLista de Docentes:")
        for profesor in profesores_registrados:
              profesor.rol == 'PROFESOR'
        if (
                profesor.rol == 'PROFESOR'
                and docente.nombre == profesor.nombre
                and docente.apellidos == profesor.apellidos
                and docente.asignatura == profesor.asignatura
                and docente.seccion in profesor.seccion
            ):
                print("\nNombre: ", profesor.nombre, profesor.apellido)
                print("Asignatura: ", profesor.asignatura)
                print("Sección: ", profesor.seccion)
        print("\nFin de la lista.")


def validar_docente():
    nombre = input("Ingrese su nombre como docente: ")
    apellidos = input("Ingrese sus apellidos como docente: ")
    asignatura = input("Ingrese la asignatura: ")
    seccion = input("Ingrese la sección: ")

    docente_encontrado = None
    for profesor in profesores_registrados:
         if (
            profesor["rol"] == 'PROFESOR'
            and profesor["nombre"] == nombre
            and profesor["apellido"] == apellidos
            and profesor["asignatura"] == asignatura
            and seccion in profesor.seccion
        ):
            docente_encontrado = profesor
            break

    if docente_encontrado:
        return docente_encontrado
    else:
        print("Docente no encontrado o datos incorrectos.")
        return False

    
while True:
    print("\n ==========MENU PRINCIPAL==========:")
    print("1. Ingresar Usuario")
    print("2. Ingresar Notas")
    print("3. Actualizar Alumno")
    print("4. Eliminar Alumno")
    print("5. Mostrar")
    print("6. Salir del Programa")

    opcion_principal = input("Ingrese la opción deseada (1, 2, 3, 4, 5, 6): ")

    if opcion_principal == "1":
        ingresar_usuario()
    elif opcion_principal == "2":
        ingresar_notas()
    elif opcion_principal == "3":
        actualizar_alumno()
        
    elif opcion_principal == "4":
        eliminar_alumno()
    elif opcion_principal == "5":
        while True:
            print("\nMenú Mostrar:")
            print("A. Listar por Secciones")
            print("B. Mostrar por Alumnos")
            print("C. Mostrar por Docentes")
            print("D. Volver al Menú Principal")

            opcion_mostrar = input("Ingrese la opción deseada (A, B, C, D): ").upper()

            if opcion_mostrar == "A":
                listar_por_secciones()
            elif opcion_mostrar == "B":
                mostrar_por_alumnos()
            elif opcion_mostrar == "C":
                mostrar_por_docentes()
            elif opcion_mostrar == "D":
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    elif opcion_principal == "6":
        salir = input("¿Desea salir del programa? (SI/NO): ").upper()
        if salir == "SI":
            print("¡Hasta luego!")
            break
        elif salir == "NO":
            continue
        else:
            print("Opción no válida. Volviendo al Menú Principal.")
    else:
        print("Opción no válida. Intente nuevamente.")
