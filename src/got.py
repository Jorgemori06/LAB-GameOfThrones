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
            atac_raw = fila[5] or ""
            defs_raw = fila[6] or ""
            comandantes_atacantes = [c.strip() for c in atac_raw.split(',') if c.strip()]
            comandantes_atacados = [c.strip() for c in defs_raw.split(',') if c.strip()]
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


def batallas_mas_comandantes(batallas: list[BatallaGOT],regiones: set[str] | None = None,n: int | None = None) -> list[tuple[str, int]]:
    
    filtradas: list[tuple[str, int]] = []

    for b in batallas:
        if regiones is None or b.region in regiones:
            # Por si acaso, nos aseguramos de que no haya cadenas vacías
            atac = [c for c in (b.comandantes_atacantes or []) if c]
            defs = [c for c in (b.comandantes_atacados or []) if c]
            total = len(atac) + len(defs)
            filtradas.append((b.nombre, total))

    # Ordenar: primero por nº de comandantes (desc), luego por nombre (asc)
    filtradas.sort(key=lambda x: (-x[1], x[0]))

    # Si n no es None, nos quedamos con las n primeras
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

"""5.	**rey_mas_victorias_por_region**: recibe una lista de tuplas de tipo ``BatallaGOT`` y una cadena 
``rol``, con valor por defecto ``"ambos"``, y devuelve un diccionario que relaciona cada región con el nombre del rey que 
acumula más victorias en batallas ocurridas en esa región. El parámetro ``rol`` tiene el mismo significado que en la función 
anterior. Si para alguna región no hay ningún rey que haya ganado una batalla con el rol especificado, en el diccionario 
aparecerá el valor ``None`` asociado a dicha región. Puede usar la función ``rey_mas_victorias`` para resolver este ejercicio. 
Por ejemplo, si pasamos a la función la lista completa de batallas contenida en el CSV, y el parámetro ``rol`` contiene 
``"ambos"``, la función devuelve un diccionario que, entre otros ítems, asocia la clave ``"The Stormlands"`` a ``"Joffrey 
Baratheon"``; esto significa que dicho rey es el que ganó más batallas de entre las batallas ocurridas en "The Stormlands", 
sumando tanto las victorias en batallas en las que fue atacante, como las victorias en batallas en las que fue atacado. _(2 puntos)_"""

def rey_mas_victorias_por_region(batallas: list["BatallaGOT"], rol: str = "ambos") -> dict[str, str|None]:
    regiones = defaultdict(list)

    for b in batallas:
        regiones[b.region].append(b)

    resultado = {}
    for region, batallas_region in regiones.items():
        rey_ganador = rey_mas_victorias(batallas_region, rol)
        resultado[region] = rey_ganador

    return resultado
