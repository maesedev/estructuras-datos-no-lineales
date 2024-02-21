materias = {
    "Introducción a la Programación": 4,
    "Estructuras de Datos": 3,
    "Algoritmos y Complejidad": 4,
    "Arquitectura de Computadoras": 3,
    "Bases de Datos": 3,
    "Redes de Computadoras": 3,
    "Sistemas Operativos": 4,
    "Ingeniería de Software": 4,
    "Inteligencia Artificial": 3,
    "Proyecto de Fin de Carrera": 4
}

sum_creditos = 0
for materia in materias:
    creditos_materia = materias.get(materia) 
    sum_creditos += creditos_materia
    print(f"La materia {materia.upper()} tiene { creditos_materia } créditos")
    
print(f"\nEn total tienes {sum_creditos} créditos ")