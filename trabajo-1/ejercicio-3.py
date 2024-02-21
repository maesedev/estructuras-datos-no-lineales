
import inquirer as inq
spare ={
    "bujia" : 1.4,
    "pastillas de freno":5.8,
    "radiador":300.5,
    "rodamiento":10.70 
}

items = []
for item in spare.keys():
    items.append(item)  
    
question = [inq.List("spare",message="¿Que repuesto necesitas?", choices=items),
            inq.Text("cantidad",message="¿Cuantos repuestos necesitas?", validate=lambda _, x: int(x) >=1 )]
choice = inq.prompt(question)

question = []
cantidad = inq.prompt(question)


