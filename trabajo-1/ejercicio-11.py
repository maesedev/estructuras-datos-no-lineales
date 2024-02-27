import random
import string

nombres = ["Juan", "Carlos", "Luis", "Ana", "María", "Elena", "Pedro", "Diego", "Laura", "Sofía", "Alejandro", "Marta", "Javier", "Isabel", "Daniel", "Raquel", "Roberto", "Lucía", "Pablo", "Carmen"]
apellidos = ["Gonzales", "Azaustre", "Pérez", "Martínez", "López", "Fernández", "García", "Rodríguez", "Díaz", "Sánchez", "Torres", "Ramírez", "Hernández", "Vargas", "Jiménez", "Ruiz", "Gómez", "Moreno", "Alonso", "Ortega"]

def generar_nombre():
    nombres_completos = []
    # Ejemplo de uso

    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    nombre_completo = f"{nombre} {apellido}"

    return nombre_completo

def generar_identificacion():
    identificacion = random.randint(10**9, 10**10 - 1)
    return f"{identificacion}"

def generar_numero_telefonico():
    primer_digito = 3
    otros_digitos = random.randint(10**8, 10**9 - 1)
    return f"{primer_digito}{otros_digitos}"


def generar_correo_aleatorio(nombre = random.choice(nombres)):
    
    dominios = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "example.com"]

    usuario = nombre + random.choice(apellidos)[:3] + str(random.randint(10, 999))
    usuario = usuario.lower()  
    dominio = random.choice(dominios)

    return f"{usuario}@{dominio}"


##########################################################################
################ Generar el directorio aleatoriamente ####################
##########################################################################

directorio_raw = ""
for i in range(999):
    directorio_raw += generar_identificacion() + ";"
    directorio_raw += generar_nombre() + ";"
    directorio_raw += generar_correo_aleatorio() + ";"
    directorio_raw += generar_numero_telefonico() + ";"
    # Maximo descuento del 40%
    directorio_raw += str(random.randint(0,40)) + "\n"
    
# Obtenemos el directorio
clients = directorio_raw.split("\n")


##########################################################################
######################## Parsear a un objeto #############################
##########################################################################

clients_parsed = {}
for client in clients:
    
    if not client:
        continue
    
    id, name , email, phone, discount = client.split(";")
    clients_parsed[id] ={
        "name":name,
        "email":email,
        "phone":phone,
        "discount":discount,
    }
    
    
    
print(clients_parsed)