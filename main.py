import requests
from decorator import random_number_fake
# Esta función recibe como parámetro un número,una fecha en formato día-mes o
# nada. Si recibe un número retorna un dato curioso de ese número, si reciba una
# fecha retorna un dato curioso de esa fecha, por último si no recibe nada,
# retorna un dato matemático de un número al azar.


@random_number_fake
def random_number_fact(number=None):
    response = requests.get("http://numbersapi.com/random/math")
    return response.content.decode('utf-8')


print(f"Dato curioso relacionado a un número: {random_number_fact(26)}\n")
print(f"Dato curioso de una fecha: {random_number_fact('17-2')}\n")
print(f"Dato curioso matemático aleatorio: {random_number_fact()}")
