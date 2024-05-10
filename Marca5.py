import datetime
#Comentario nuevo
#Funcion para convertir una moneda
def ConvertirMoneda(CambioMonedaDestino, CantidadMonetaria):
    return CantidadMonetaria * CambioMonedaDestino
#Funcion que comprueba si existe una moneda
def ComprobarExistenciaMoneda(MonedaOrigen):
    monedas = [
        "USD",
        "EUR",
        "GBP",
        "CHF",
        "JPY",
        "AUD",
        # Agrega más monedas aquí
    ]
    
    if MonedaOrigen in monedas:
        return True
    else:
        return False
#Funcion que comprueba que dos monedas introducidas no son la misma
def ComprobarSiMonedasDiferentes(Moneda1, Moneda2):
    if Moneda1 != Moneda2:
        return True
    else:
        return False

Entrada = input()
monedas = [
    "USD",
    "EUR",
    "GBP",
    "CHF",
    "JPY",
    "AUD",
    # Add more currencies here
]
if Entrada == "ayuda":
    # Code to be executed if the condition is true
    print("Este programa es capaz de convertir monedas con los cambios en tiempo real. Comandos soportados:\n convertir (MONEDA DE ORIGEN) (MONEDA DESTINO) (CANTIDAD MONETARIA)\n fecha\n version\n monedas soportadas\n")
elif Entrada == "2":
    # Code to be executed if the condition is true
    print("Versión: 1.0")
elif Entrada == "3":
    # Code to be executed if the condition is true
    print("Fecha:", datetime.date.today())
elif Entrada == "4":
    # Code to be executed if none of the conditions are true
    print("Monedas soportadas:")
    for moneda in monedas:
        print(moneda)
