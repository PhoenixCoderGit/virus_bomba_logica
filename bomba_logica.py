# ############################################################
# Autor: CoderPhoenix
# pagina facebook: https://www.facebook.com/groups/CodeFenix
# ############################################################

import time, datetime

explota_fecha_hora_objetivo = "2020-06-09 20:51:00"


while True:
    codigo_numeros = time.time()
    fecha_hora_explosion = datetime.datetime.fromtimestamp(codigo_numeros).strftime('%Y-%m-%d %H:%M:%S')

    print (fecha_hora_explosion)

    if fecha_hora_explosion == explota_fecha_hora_objetivo:

        print("LA BOMBA LOGICA EXPLOTO CON EXITO!")

        break

    else:

        pass