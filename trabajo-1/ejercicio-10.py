import inquirer as inq
import re
# {<user_nif> : { data } }

users = {}

def add_client(NIF,name, address, phone, email, preference):
    if NIF in users:
        print("\n\nLa usuario ya existe")
        questions = [
        inq.Confirm("overwrite",message="¿Estas seguro que quieres sobre escribir la informacion del usuario, esta acción es irreversible?"),
        ]
        overwrite = inq.prompt(questions)["overwrite"]
        
        if overwrite:
            users[NIF] = {
                "name":name,
                "address":address,
                "phone":phone,
                "email":email,
                "preference":preference
            }
            print("\nUsuario modificado correctamente\n")
    else:
        users[NIF] = {
                "name":name,
                "address":address,
                "phone":phone,
                "email":email,
                "preference":preference
            }
        print("\nUsuario creado correctamente\n")
        
def delete_client(NIF):
    if NIF in users:
        user = users.get(NIF)
        username = user["name"]
        questions = [
            inq.Confirm("delete",message=f"¿Estas seguro que quieres eliminar el usuario {username} y con NIF {NIF} , esta acción es irreversible?"),
        ]
        
        answer = inq.prompt(questions=questions)
        
        if answer.get("delete"):   
            del users[NIF]
            print(f"Usuario {username} eliminado correctamente")
        else: 
            print("Acción Cancelada...")
    else:
        print("Usuario no encontrado.")

def list_client(NIF):
    if NIF in users:
        for item in users[NIF]:
            print(f" {item}: {users[NIF][item]} ")
    else:
        print("\nUsuario no encontrado.\n")
        
def list_all_clients():
    if not users:
        print("No existen clientes")
        return 
    for NIF in users.keys():
        print(f"usuario { users.get(NIF)['name'] } con NIF {NIF}")
    print("\n")

def list_preferents():
    filtered_clients = filter(lambda x : users[x]['preference']  ,users)
    
    if not filtered_clients:
        print("No existen clientes preferentes")
        return
    
    for client_nif in filtered_clients:
        name = users[client_nif]["name"]
        preference = users[client_nif]["preference"]
        print(f"El usuario {name} con NIF {client_nif} \n\tpreferencial: {'si' if preference else 'no'}")
    print("\n")

        
def validar_correo(correo):
    return re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', correo) is not None

choices = ["Añadir cliente",
           "Eliminar cliente", 
           "Mostrar cliente",
           "Listar todos los clientes",
           "Listar clientes preferentes",
           "Salir"]

quit =  False
while not quit:
    questions =[
        inq.List("option",message="Base de datos, ¿que acción quieres hacer?",choices=choices)]
    
    option = inq.prompt(questions)["option"]
    
    
    ###########################################
    ############# Añadir cliente ##############
    ###########################################
    if option == choices[0]:
        questions = [
            inq.Text("nif",message="Por favor ingrese el NIF del cliente"),
            inq.Text("name",message="Por favor ingrese el nombre del cliente", validate=lambda _,x: len(x) >= 3),
            inq.Text("address",message="Por favor ingrese la direccion del cliente"),
            inq.Text("phone",message="Por favor ingrese el numero de telefono del cliente"),
            inq.Text("email",message="Por favor ingrese el email del cliente", validate=lambda _,x: validar_correo(x)),
            inq.Confirm("preference",message="¿El cliente es preferencial?", default=False),
                     ]
        ans = inq.prompt(questions)
        add_client(
            NIF = ans["nif"] , 
            name = ans["name"],
            email = ans["email"],
            address = ans["address"],
            phone = ans["phone"],
            preference = ans["preference"]
            )
        
    
    
    ###########################################
    ############ Eliminar cliente #############
    ###########################################
    if option == choices[1]:
        questions  = [inq.Text("nif",message="Ingrese el NIF del cliente a eliminar")]
        nif = inq.prompt(questions)["nif"]
        delete_client(NIF=nif)
        
    
    ###########################################
    ############# Mostrar cliente #############
    ###########################################
    if option == choices[2]:
        questions  = [inq.Text("nif",message="Ingrese el NIF del cliente a mostrar")]
        nif = inq.prompt(questions)["nif"]
        list_client(nif)
        
    
    ###########################################
    ######## Listar todos los clientes ########
    ###########################################
    if option == choices[3]:
        list_all_clients()
        
    ###########################################
    ############ Listar preferentes ###########
    ###########################################
    
    if option == choices [4]:
        list_preferents()
    
        
    ###########################################
    ################# Salir ###################
    ###########################################
    
    if option == choices [5]:
        quit = True
    
    
print("Quiting...")    
    
        
    
    


