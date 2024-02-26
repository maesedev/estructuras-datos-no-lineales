import inquirer

## {<numero factura 1> : Valor , <numero factura 2> : Valor, ... , <numero factura n> : Valor , }



facturas = {}

def pagar_factura(ID):
    if ID in facturas:
        del facturas[ID]
        print("\nFactura Pagada correctamente\n")
    else:
        print("Esta factura no existe")
        
        
def crear_factura(ID,valor):
    if ID in facturas:
        print("\n\nLa factura ya fue recientemente creada")
        questions = [
        inquirer.Confirm("overwrite",message="¿Estas seguro que quieres sobre escribir la factura, esta acción es irreversible?"),
        ]
        overwrite = inquirer.prompt(questions)["overwrite"]
        
        if overwrite:
            facturas[ID] = valor
    else:
        facturas[ID] = valor
        print("\nFactura creada correctamente\n")
    
def ask_for_id_and_value():
    questions = [
        inquirer.Text("id",message="Ingresa el ID de la factura"),
        inquirer.Text("cost",message="Ingresa el valor de la factura", validate=lambda _,x:x.isdigit())
        ]
    answers =  inquirer.prompt(questions)
    return answers["id"] , answers["cost"] 
    
salir = False
while not salir:
    questions = [
        inquirer.List(
            "option",
            message="Que quieres hacer con tus facturas",
            choices=["crear", "pagar","listar", "salir"],
        ),
    ]
    option = inquirer.prompt(questions)["option"]
    
    if option == "crear":
        id, cost = ask_for_id_and_value()
        crear_factura(id, cost)
        
    if option == "pagar":
        questions = [
            inquirer.Text("id",message="Ingresa el ID de la factura")
            ]
        ID =  inquirer.prompt(questions)["id"]
        pagar_factura(ID)
        
    if option == "listar":
        print("\n")
        for factura in facturas:
            print(f"Factura { factura } --> ${ facturas[factura] }")
        
        print("\n")
    if option == "salir":
        salir = True
        
print("Saliendo del programa...")