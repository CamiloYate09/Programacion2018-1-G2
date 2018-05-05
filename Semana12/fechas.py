from datetime import *

hoy = datetime.now().date()
ayer = date(hoy.year,hoy.month,hoy.day-1)
manana = date(hoy.year,hoy.month,hoy.day+1)

print(ayer,hoy,manana)


def to_date(fecha):
    respuesta = fecha.strip().split('/')
    respuesta = date(int(respuesta[0]),
                        int(respuesta[1]),
                        int(respuesta[2]))
    return respuesta

fecha_inicio = to_date(input('digite su fecha de entrada'
                             ' en formato yyyy/mm/dd'))
fecha_salida = to_date(input('digite su fecha de salida'
                             ' en formato yyyy/mm/dd'))

print('Su fecha de inicio es',fecha_inicio,'\n',
      'Su fecha de salida es',fecha_salida)

if fecha_inicio < fecha_salida or fecha_inicio > datetime.now().date():
    if ayer <= fecha_inicio <= manana or ayer <= fecha_salida <= manana:
        print('Reservada en esas fechas')
    else:
        print('Disponible')
else:
    print('La fecha de inicio no puede ser menor a la de salida'
          'o al dia de hoy')