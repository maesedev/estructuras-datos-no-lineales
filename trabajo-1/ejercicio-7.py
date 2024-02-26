import inquirer as inq

carrito = {}
checkout = False

def validate_price(price):
    
    no_point_price = price.replace(".","",1)
    no_coma_price = no_point_price.replace(",","",1)
    return no_coma_price.isnumeric()

def print_carrito(carrito):
    print("\nCarrito")
    if not carrito:
        return
    total = 0
    for item in carrito:
        price = carrito[item]
        print(f"{item} \t\t{price}" )
        total += price
    print("-------------------------------")
    print(f"total:\t\t {total}\n")


while not checkout :
    questions = [
        inq.Text("tag",message="Ingrese el nombre de articulo",validate = lambda _,x: len(x) > 2),
        inq.Text("price",message="Ingrese el precio del articulo", validate=lambda _,x: validate_price(x)),
    ]
    answers = inq.prompt(questions)
    
    
    if answers["tag"] in carrito:
        print("\n\nEl articulo ya fue recientemente agregado")
        questions = [
        inq.Confirm("overwrite",message="¿Quieres sobre escribir el precio del articulo?"),
        ]
        confirm = inq.prompt(questions)
        if confirm["overwrite"] :
            carrito[answers["tag"]] = float(answers["price"].replace(",",".",1)) 
    else:
        carrito[answers["tag"]] = float(answers["price"].replace(",",".",1)) 
        
    checkout = not bool(inq.prompt([
        inq.Confirm( "continuar" , message="¿Seguir comprando?" ,default="y")
    ])["continuar"])
    
    print_carrito(carrito=carrito)