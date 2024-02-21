

import inquirer


tasas_cambio_divisa= {
    "USD": 3996.2,
    "EUR": 4421.7,
    "GBP": 4850.9,
    "JPY": 36.54,
    "CAD": 3124.8,
    "AUD": 2790.6,
    "CHF": 4372.1,
    "SEK": 412.89,
    "NZD": 2627.5,
    "NOK": 436.15,
    "DKK": 640.28,
    "SGD": 2951.3,
    "MXN": 195.68,
    "INR": 54.78,
    "BRL": 720.45,
    "ZAR": 271.31,
    "CNY": 619.83,
    "HKD": 514.62,
    "KRW": 3575.4,
    "TRY": 485.97,
    "RUB": 53.28,
    "IDR": 0.28,
    "MYR": 953.74,
    "THB": 125.72,
    "PHP": 78.82,
    "PLN": 1044.6,
    "HUF": 13.66,
    "CZK": 183.14,
    "ILS": 1202.3,
    "ARS": 42.85,
    "CAD": 3124.8,
    "AUD": 2790.6,
    "CHF": 4372.1,
    "SEK": 412.89,
    "NZD": 2627.5,
    "NOK": 436.15,
    "DKK": 640.28,
    "SGD": 2951.3,
    "MXN": 195.68,
    "INR": 54.78,
    "BRL": 720.45,
    "ZAR": 271.31,
    "CNY": 619.83,
    "HKD": 514.62,
    "KRW": 3575.4,
    "TRY": 485.97,
    "RUB": 53.28,
    "IDR": 0.28,
    "MYR": 953.74,
    "THB": 125.72,
    "PHP": 78.82,
    "PLN": 1044.6,
    "HUF": 13.66,
    "CZK": 183.14,
    "ILS": 1202.3,
    "ARS": 42.85,
    "CLP": 5.26,
    "COP": 1,
    "VND": 0.17,
    "UAH": 149.64,
    "EGP": 253.12,
    "YEN":26.04,
}


def mostrar_conversion(COP, tasa_divisa,code_divisa):
    cop_formated = f"{COP:,.2f}"
    divisa_formated = f"{round(COP / tasa_divisa,2):,.2f}"
    print(f"${ cop_formated} COP equivalen a  ${divisa_formated} {code_divisa}")
    

    
questions = [
inquirer.Text('divisa', message="Introduce la divisa (EUR, USD, YEN, SEK, ...)"),
inquirer.Text('cantidad', message="Cantidad a convertir ( COP --> X )")
]
answers = inquirer.prompt(questions)

cantidad_cop = answers.get("cantidad")
code_divisa = answers.get("divisa").upper()
tasa_divisa = tasas_cambio_divisa.get(code_divisa, 0 )

if not tasa_divisa:
    print("Lo sentimos, no contamos con esta divisa en nuestro diccionario, intente con otra divisa.") 
    exit()

try:
    mostrar_conversion(int(cantidad_cop), tasa_divisa,code_divisa)
except ValueError:
    print("Por favor ingrese datos validos en la cantidad a convertir(COP)")



