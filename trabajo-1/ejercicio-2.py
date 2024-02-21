import inquirer as inq


questions = [
    inq.Text("name",message="Hola, ¿cuál es tu nombre?"),
    inq.Text("age", message="¿Cuál es tu edad?"),
    inq.Text("address", message="¿Cuál es tu dirección?"),
    inq.Text("phone", message="¿Cuál es tu número telefonico?"),
    ]

answers = inq.prompt(questions)

name = answers.get("name")
age = answers.get("age")
address = answers.get("address")
phone = answers.get("phone")

print(f"{name} tiene {age} años, vive en {address} y su número de teléfono es {phone}")