import inquirer as inq
meses = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}


questions = [inq.Text("format" , message="Por favor ingrese la fecha en el formato dd/mm/yy: ")]
answers = inq.prompt(questions)


day, month_index, year = answers.get("format").split("/")

month = meses.get( int(month_index ))

print(f"{day} de {month} de {year}")
