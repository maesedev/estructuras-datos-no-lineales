import re
import inquirer as inq

usuario =  {}

def print_usuario(dict):
    print("")
    for item in dict:
        print(f"{item} es {dict.get(item)}")
    print("")
        
def validar_correo(correo):
    return re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', correo) is not None

questions = [
    inq.Text("nombre",message="Digita tu nombre"),
    inq.Text("edad",message="Digita tu edad", validate=lambda _,x: x.isnumeric() ),
    inq.Text('correo', message="Ingrese su correo electrónico", validate=lambda _,correo: validar_correo(correo)),
    inq.Text("telefono",message="Por favor ingresa tu numero de telefono"),
    inq.Text("sexo",message="Ingresa tu sexo"),
]

for question in questions:
    answer =  inq.prompt([question])
    key = list(answer)[0]
    usuario[key] = answer.get(key)
    
    print_usuario(usuario)

