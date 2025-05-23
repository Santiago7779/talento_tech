from datetime import datetime

def saludo_segun_hora():
    hora_actual = datetime.now().hour

    if 5 <= hora_actual < 12:
        return "Buenos días"
    elif 12 <= hora_actual < 18:
        return "Buenas tardes"
    elif 18 <= hora_actual < 24:
        return "Buenas noches"
    else:
        return "Es de madrugada"

print(saludo_segun_hora())
