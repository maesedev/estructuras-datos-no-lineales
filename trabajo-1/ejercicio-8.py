import inquirer as inq
import re
# {"español:"ingles"}

traducciones = {}
more_words = True


def validate_traduction(str):
    words = str.split(":")
    if len(words) == 1 or len(words) > 2:  return False
    word_es,word_en = words
    if not word_en.isalpha() or  not word_en.isalpha(): return False
    return True
    

def brake_trad(str):
    return str.split(":")

def parse_sentense(sentense):
    patron = r'[.,!?;\'"(){}\[\]:—-]'
    cadena_sin_puntuacion = re.sub(patron, ' ', sentense)
    return cadena_sin_puntuacion






##################################################################
#################### registro de palabras ########################
##################################################################
while more_words :
    questions = [
        inq.Text("cantidad",message="la cantidad de palabras que vas a agregar",validate = lambda _,x: x.isnumeric()),
    ]
    answers = inq.prompt(questions)
    
    for i in range(int(answers["cantidad"])):
        word_inquirer = [
            inq.Text("traduction",message="Por favor ingrese la traduccion en el formato \"<palabra> : <palabra traducida>\" ",validate = lambda _,x: validate_traduction(x)),
        ]
        palabra = inq.prompt(word_inquirer)["traduction"]
        
        word_es , word_en = brake_trad(palabra)
        
        word_es = word_es.lower()
        word_en = word_en.lower()
        
        if word_es in traducciones:
            print("\n\nLa palabra ya fue recientemente agregada")
            questions = [
            inq.Confirm("overwrite",message="¿Quieres sobre escribir la traducción?" , default=False)
            ]
            overwrite = inq.prompt(questions)["overwrite"]
            if overwrite:
                traducciones[word_es] =  word_en
                
            print("\n\tLa palabra" + (" no" if not overwrite else "" ) + " fue sobre escribida.\n")
        else:
            traducciones[word_es] = word_en
            
    more_words = bool(inq.prompt([
        inq.Confirm( "continuar" , message="¿Seguir agregando palabras?" ,default="y")
    ])["continuar"])
    
    

##################################################################
###################### TRADUCIR ORACIÓN ##########################
##################################################################

more_traductions = True
while more_traductions:
    questions = [
        inq.Text("sentense",message="Ingresa la frase a traducir"),
    ]
    sentense = inq.prompt(questions)["sentense"]
    
    parsed_sentense = parse_sentense(sentense)
    
    traduced = ""
    for word in parsed_sentense.split(" "):
        if word.lower() in traducciones: 
            traduced += traducciones[word.lower()] + " " 
        else:
            traduced += word + " " 
            
    
    
    print(f"La frase :\n\"{sentense}\" \n\tES --> EN\n \"{traduced}\"")
    more_traductions = bool(inq.prompt([
        inq.Confirm( "continuar" , message="¿Quieres traducir otra frase?" ,default="y")
    ])["continuar"])
    
    
    
print("Hasta la proxima ;)")