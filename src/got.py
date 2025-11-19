from typing import List 
from typing import NamedTuple
from collections import defaultdict
import csv

BatallaGOT = NamedTuple('BatallaGOT',                         
                        [
                            ('nombre', str),
                            ('rey_atacante', str),
                            ('rey_atacado', str),
                            ('gana_atacante', bool),
                            ('muertes_principales', bool),
                            ('comandantes_atacantes', list[str]),
                            ('comandantes_atacados', list[str]),
                            ('region', str),
                            ('num_atacantes', int|None),
                            ('num_atacados',int|None)
                        ])

def lee_batallas(fichero:str)->list[BatallaGOT]:
    Batallas=[]
    with open (fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)  # Saltar la cabecera
        for fila in lector:
            nombre = fila[0]
            rey_atacante = fila[1]
            rey_atacado = fila[2]
            gana_atacante = fila[3].lower() == 'win'
            muertes_principales = fila[4].lower() == 'true'
            comandantes_atacantes = fila[5].split(';')
            comandantes_atacados = fila[6].split(';')
            region = fila[7]
            num_atacantes = int(fila[8]) if fila[8] else None
            num_atacados = int(fila[9]) if fila[9] else None
            batalla = BatallaGOT(nombre,rey_atacante,rey_atacado,gana_atacante, muertes_principales,comandantes_atacantes,
                                 comandantes_atacados,region,num_atacantes,num_atacados)
            Batallas.append(batalla)
    return Batallas

def reyes_mayor_menor_ejercito(batallas: list["BatallaGOT"]) -> tuple[str, str]:
    totales = defaultdict(int)  # cada rey empieza en 0

    for b in batallas:
        # Suma al rey atacante si hay nombre y número
        if b.rey_atacante and b.num_atacantes is not None:
            totales[b.rey_atacante] += b.num_atacantes
        # Suma al rey defensor si hay nombre y número
        if b.rey_atacado and b.num_atacados is not None:
            totales[b.rey_atacado] += b.num_atacados

    rey_mayor = max(totales, key=totales.get)
    rey_menor = min(totales, key=totales.get)
    return rey_mayor, rey_menor

"""3.	**batallas_mas_comandantes**: recibe una lista de tuplas de tipo ``BatallaGOT``, un conjunto de cadenas 
``regiones``, con valor por defecto ``None``, y un valor entero ``n`` con valor por defecto ``None``, y devuelve
 una lista de tuplas ``(str, int)`` con los nombres y el total de comandantes participantes de aquellas n batallas
   con mayor número de comandantes participantes (tanto atacantes como atacados), llevadas a cabo en alguna de las 
   regiones indicadas en el parámetro regiones. Si el parámetro ``regiones`` es ``None`` se considerarán todas las
     regiones; por su parte, si el parámetro ``n`` es ``None`` se devolverán las tuplas correspondientes a todas las
       batallas de las regiones escogidas. En todos los casos, la lista devuelta estará ordenada de mayor a menor número 
       de comandantes. Por ejemplo, si la función recibe la lista completa de batallas contenida en el CSV, y si 
       ``regiones`` es `{'The North', 'The Riverlands'}` y ``n`` es ``4``, la función devuelve ``[('Battle of the Green Fork', 9)
       , ('Battle of the Fords', 9), ('Battle of the Camps', 5), ('Sack of Winterfell', 5)]``. _(2 puntos)_"""


def batallas_mas_comandantes(batallas: list["BatallaGOT"],regiones: set[str] = None,n: int = None) -> list[tuple[str, int]]:
    filtradas = []
    for b in batallas:
        if regiones is None or b.region in regiones:
            atac = b.comandantes_atacantes or []
            defs = b.comandantes_atacados or []
            total = len(atac) + len(defs)
            filtradas.append((b.nombre, total))

    # Ordenar de mayor a menor número de comandantes
    filtradas.sort(key=lambda x: (-x[1], x[0]))
    if n is not None:
        filtradas = filtradas[:n]

    return filtradas
"""4.	**rey_mas_victorias**: recibe una lista de tuplas de tipo ``BatallaGOT`` y una cadena ``rol``, 
con valor por defecto ``"ambos"``, y devuelve el nombre del rey que acumula más victorias. Tenga en cuenta 
que un rey puede ganar una batalla en la que actúa como atacante, en cuyo caso el campo ``gana_atacante`` será
 ``True``, o una batalla en la que actúa como atacado, en cuyo caso el campo ``gana_atacante`` será ``False``.
Si el parámetro ``rol`` es igual a ``"atacante"``, se devolverá el nombre del rey que acumula más victorias
como atacante; si ``rol`` es igual a ``"atacado"``, se devolverá el nombre del rey que acumula más victorias 
como atacado; si ``rol`` es igual a ``"ambos"``, se devolveré el nombre del rey que acumula más victorias en
todas las batallas en las que ha participado (sumando sus victorias como atacante y como atacado). 
Si ningún rey acumula victorias del rol especificado en la lista de batallas recibida, la función devuelve ``None``. 
Por ejemplo, si el parámetro rol contiene ``"ambos"`` y la función devuelve ``"Stannis Baratheon"``, significa que dicho 
rey es el que ha ganado más batallas de la lista de batallas recibida, sumando tanto las victorias en batallas en las que 
fue atacante, como las victorias en batallas en las que fue atacado. _(2,75 puntos)_
"""
def rey_mas_victorias(batallas: list["BatallaGOT"], rol: str = "ambos") -> str|None:
    victorias = defaultdict(int)

    for b in batallas:
        if rol in ("atacante", "ambos") and b.gana_atacante:
            victorias[b.rey_atacante] += 1
        if rol in ("atacado", "ambos") and not b.gana_atacante:
            victorias[b.rey_atacado] += 1

    if not victorias:
        return None

    rey_ganador = max(victorias, key=victorias.get)
    return rey_ganador