# ############################################################
# Autor: CoderPhoenix
# pagina facebook: https://www.facebook.com/groups/CodeFenix
# ############################################################

import time, datetime

explota = "2020-06-09 20:51:00"


while True:
    numero = time.time()
    fecha_actual = datetime.datetime.fromtimestamp(numero).strftime('%Y-%m-%d %H:%M:%S')

    print (fecha_actual)

    if fecha_actual == explota:

        print("LA BOMBA LOGICA EXPLOTO CON EXITO!")

        break

    else:

        pass