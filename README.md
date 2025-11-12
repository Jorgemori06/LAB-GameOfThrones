## Fundamentos de Programación
# Ejercicio de laboratorio: Juego de Tronos
### Autor: Fermín L. Cruz
### Revisores: José C. Riquelme, Mariano González, Toñi Reina
### Adaptación para laboratorio: Toñi Reina

Este proyecto es una adaptación del primer parcial del curso 2021/22. 

## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **got.py**: Contiene funciones para explotar los datos de juego de tronos.
    * **got_test.py**: Contiene funciones de test para probar las funciones del módulo `got.py`. En este módulo está el main.
    * **parsers.py**: Contiene funciones de conversión de tipos.
* **/data**: Contiene el dataset o datasets del proyecto
    * **battles.csv**: Archivo con los datos de batallas de Juego de tronos.

## Ejercicios a realizar

Disponemos de datos sobre las batallas libradas en la serie de libros de Game of Thrones. Para cada batalla, tenemos en un fichero CSV la siguiente información (los campos aparecen separados por punto y coma):
-	**nombre**: nombre de la batalla, de tipo ``str``.
-	**rey atacante**: nombre del rey que inicia la batalla, de tipo ``str``.
-	**rey atacado**: nombre del rey que es atacado, de tipo ``str``.
-	**gana atacante**: indica si los atacantes ganaron la batalla, de tipo ``bool`` (en el fichero consta "win" si ganaron, "loss" si ganaron los atacados).
-	**muertes principales**: indica si murieron personajes principales de la trama, de tipo ``bool`` (en el fichero consta "1" si murieron, "0" si no).
-	**comandantes atacantes y comandantes atacados**: lista de nombres de los personajes que lideraron el ataque y la defensa, respectivamente, ambos de tipo ``list`` de ``str``. Los nombres aparecen separados por comas, si hay más de uno. Estos campos pueden estar vacíos, en cuyo caso se deben inicializar con una lista vacía.
-	**region**: nombre de la región donde se llevó a cabo la batalla, de tipo ``str``.
-	**número de atacantes y número de atacados**: indica el número aproximado de integrantes de los ejércitos atacante y atacado, respectivamente, ambos de tipo ``int``. Estos campos pueden estar vacíos, en cuyo caso se deben inicializar con el valor ``None``.
Por ejemplo, la siguiente línea del fichero:

```
Battle of Torrhen's Square, Robb Stark, Greyjoy, win, 0, Rodrik Cassel, Cley Cerwyn, Dagmer Cleftjaw, The North, 244, 900 
```

indica que la batalla conocida como "Battle of Torrhen’s Square" fue iniciada por el rey "Robb Stark", contra el rey "Greyjoy"; la batalla fue ganada por el rey atacante, y no se produjeron muertes entre los personajes principales que participaron en la misma; los comandantes que lideraron el ataque fueron "Rodrik Cassel" y "Cley Cerwyn", mientras que hubo un único comandante liderando la defensa, "Dagmer Cleftjaw"; por último, la batalla transcurrió en la región "The North", y en ella participaron 244 atacantes y 900 defensores.

Para almacenar los datos de un entrenamiento se usará obligatoriamente la siguiente ``NamedTuple``:
```python 
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

```

Cree un módulo **got.py** e implemente en él las funciones que se piden. Utilice *typing* para definir el tipo de los parámetros y el tipo de devolución de cada función. Implemente los tests correspondientes en el módulo **got_test.py**; las puntuaciones indicadas para cada ejercicio incluyen la realización de dicho test.

1.	**lee_batallas**: lee un fichero de entrada en formato CSV codificado en utf-8 y devuelve una lista de tuplas de tipo ``BatallaGOT`` conteniendo todos los datos almacenados en el fichero. Use el método de cadenas ``split`` para separar los comandantes atacantes y atacados, y el método de cadenas ``strip`` para eliminar los espacios al inicio o final de los nombres de los comandantes. 
Por ejemplo, el último elemento de la lista devuelta debe ser:
```
BatallaGOT(nombre='Siege of Raventree', rey_atacante='Joffrey Baratheon', rey_atacado='Robb Stark', gana_atacante=True, muertes_principales=False, comandantes_atacantes=['Jonos Bracken', 'Jaime Lannister'], comandantes_atacados=['Tytos Blackwood'], region='The Riverlands', num_atacantes=1500, num_atacados=None).
```
_(1,25 puntos)_

Resultado esperado:
```
Se han leido 34 batallas
Tres primeros registros:
1-BatallaGOT(nombre='Battle of the Golden Tooth', rey_atacante='Joffrey/Tommen Baratheon', rey_atacado='Robb Stark', gana_atacante=True, muertes_principales=True, comandantes_atacantes=['Jaime Lannister'], comandantes_atacados=['Clement Piper', 'Vance'], region='The Westerlands', num_atacantes=15000, num_atacados=4000)
2-BatallaGOT(nombre="Battle at the Mummer's Ford", rey_atacante='Joffrey/Tommen Baratheon', rey_atacado='Robb Stark', gana_atacante=True, muertes_principales=True, comandantes_atacantes=['Gregor Clegane'], comandantes_atacados=['Beric Dondarrion'], region='The Riverlands', num_atacantes=None, num_atacados=120)
3-BatallaGOT(nombre='Battle of Riverrun', rey_atacante='Joffrey/Tommen Baratheon', rey_atacado='Robb Stark', gana_atacante=True, muertes_principales=False, comandantes_atacantes=['Jaime Lannister', 'Andros Brax'], comandantes_atacados=['Edmure Tully', 'Tytos Blackwood'], region='The Riverlands', num_atacantes=15000, num_atacados=10000)
Tres últimos registros:
1-BatallaGOT(nombre='Siege of Dragonstone', rey_atacante='Joffrey/Tommen Baratheon', rey_atacado='Stannis Baratheon', gana_atacante=True, muertes_principales=False, comandantes_atacantes=['Loras Tyrell', 'Raxter Redwyne'], comandantes_atacados=['Rolland Storm'], region='The Stormlands', num_atacantes=2000, num_atacados=None)
2-BatallaGOT(nombre='Siege of Riverrun', rey_atacante='Joffrey/Tommen Baratheon', rey_atacado='Robb Stark', gana_atacante=True, muertes_principales=False, comandantes_atacantes=['Daven Lannister', 'Ryman Fey', 'Jaime Lannister'], comandantes_atacados=['Brynden Tully'], region='The Riverlands', num_atacantes=3000, num_atacados=None)
3-BatallaGOT(nombre='Siege of Raventree', rey_atacante='Joffrey/Tommen Baratheon', rey_atacado='Robb Stark', gana_atacante=True, muertes_principales=False, comandantes_atacantes=['Jonos Bracken', 'Jaime Lannister'], comandantes_atacados=['Tytos Blackwood'], region='The Riverlands', num_atacantes=1500, num_atacados=None)
```
2.	**reyes_mayor_menor_ejercito**: recibe una lista de tuplas de tipo ``BatallaGOT`` y devuelve una tupla con dos cadenas correspondientes a los nombres de los reyes con el mayor y el menor ejército, respectivamente, del acumulado de todas las batallas. Para estimar el tamaño del ejército de un rey se deben sumar los números de atacantes o de atacados de todas las batallas en las que ha participado dicho rey como atacante o como atacado. _(2 puntos)_

Resultado esperado:
```
Los reyes con menor y mayor ejercito son: ('Mance Rayder', 'Stannis Baratheon')
```
3.	**batallas_mas_comandantes**: recibe una lista de tuplas de tipo ``BatallaGOT``, un conjunto de cadenas ``regiones``, con valor por defecto ``None``, y un valor entero ``n`` con valor por defecto ``None``, y devuelve una lista de tuplas ``(str, int)`` con los nombres y el total de comandantes participantes de aquellas n batallas con mayor número de comandantes participantes (tanto atacantes como atacados), llevadas a cabo en alguna de las regiones indicadas en el parámetro regiones. Si el parámetro ``regiones`` es ``None`` se considerarán todas las regiones; por su parte, si el parámetro ``n`` es ``None`` se devolverán las tuplas correspondientes a todas las batallas de las regiones escogidas. En todos los casos, la lista devuelta estará ordenada de mayor a menor número de comandantes. Por ejemplo, si la función recibe la lista completa de batallas contenida en el CSV, y si ``regiones`` es `{'The North', 'The Riverlands'}` y ``n`` es ``4``, la función devuelve ``[('Battle of the Green Fork', 9), ('Battle of the Fords', 9), ('Battle of the Camps', 5), ('Sack of Winterfell', 5)]``. _(2 puntos)_

Resultado esperado:
```
Las 3 batallas con más comandantes son:
1-('Battle of the Green Fork', 9)
2-('Battle of the Fords', 9)
3-('Battle of the Camps', 5)
Las None batallas con más comandantes son:
1-('Battle of the Blackwater', 13)
2-('Battle of the Green Fork', 9)
3-('Battle of the Fords', 9)
4-('Battle of Castle Black', 9)
5-("Siege of Storm's End", 7)
6-('Battle of the Camps', 5)
7-('Sack of Winterfell', 5)
8-('Battle of Oxcross', 5)
9-('Battle of Riverrun', 4)
10-('Sack of Harrenhal', 4)
11-('Battle of the Crag', 4)
12-('Battle of Duskendale', 4)
13-('The Red Wedding', 4)
14-('Siege of Riverrun', 4)
15-('Battle of the Golden Tooth', 3)
16-('Battle of the Whispering Wood', 3)
17-("Battle of Torrhen's Square", 3)
18-('Battle of the Ruby Ford', 3)
19-('Retaking of Deepwood Motte', 3)
20-('Battle of the Shield Islands', 3)
21-('Invasion of Ryamsport, Vinetown, and Starfish Harbor', 3)
22-("Second Seige of Storm's End", 3)
23-('Siege of Dragonstone', 3)
24-('Siege of Raventree', 3)
25-("Battle at the Mummer's Ford", 2)
26-('Sack of Darry', 2)
27-('Battle of Moat Cailin', 2)
28-('Battle of Deepwood Motte', 2)
29-('Battle of the Stony Shore', 2)
30-('Battle of Winterfell', 2)
31-("Sack of Torrhen's Square", 2)
32-('Siege of Darry', 2)
33-('Siege of Seagard', 2)
34-('Fall of Moat Cailin', 2)
```
4.	**rey_mas_victorias**: recibe una lista de tuplas de tipo ``BatallaGOT`` y una cadena ``rol``, con valor por defecto ``"ambos"``, y devuelve el nombre del rey que acumula más victorias. Tenga en cuenta que un rey puede ganar una batalla en la que actúa como atacante, en cuyo caso el campo ``gana_atacante`` será ``True``, o una batalla en la que actúa como atacado, en cuyo caso el campo ``gana_atacante`` será ``False``. Si el parámetro ``rol`` es igual a ``"atacante"``, se devolverá el nombre del rey que acumula más victorias como atacante; si ``rol`` es igual a ``"atacado"``, se devolverá el nombre del rey que acumula más victorias como atacado; si ``rol`` es igual a ``"ambos"``, se devolveré el nombre del rey que acumula más victorias en todas las batallas en las que ha participado (sumando sus victorias como atacante y como atacado). Si ningún rey acumula victorias del rol especificado en la lista de batallas recibida, la función devuelve ``None``. Por ejemplo, si el parámetro rol contiene ``"ambos"`` y la función devuelve ``"Stannis Baratheon"``, significa que dicho rey es el que ha ganado más batallas de la lista de batallas recibida, sumando tanto las victorias en batallas en las que fue atacante, como las victorias en batallas en las que fue atacado. _(2,75 puntos)_

Resultado esperado:
```
El rey con más victorias es ('Joffrey/Tommen Baratheon', 15)
```
5.	**rey_mas_victorias_por_region**: recibe una lista de tuplas de tipo ``BatallaGOT`` y una cadena ``rol``, con valor por defecto ``"ambos"``, y devuelve un diccionario que relaciona cada región con el nombre del rey que acumula más victorias en batallas ocurridas en esa región. El parámetro ``rol`` tiene el mismo significado que en la función anterior. Si para alguna región no hay ningún rey que haya ganado una batalla con el rol especificado, en el diccionario aparecerá el valor ``None`` asociado a dicha región. Puede usar la función ``rey_mas_victorias`` para resolver este ejercicio. 
Por ejemplo, si pasamos a la función la lista completa de batallas contenida en el CSV, y el parámetro ``rol`` contiene ``"ambos"``, la función devuelve un diccionario que, entre otros ítems, asocia la clave ``"The Stormlands"`` a ``"Joffrey Baratheon"``; esto significa que dicho rey es el que ganó más batallas de entre las batallas ocurridas en "The Stormlands", sumando tanto las victorias en batallas en las que fue atacante, como las victorias en batallas en las que fue atacado. _(2 puntos)_

Resultado esperado:
```
Los reyes con más victorias por region con rol ambos son:
1-('The Westerlands', ('Robb Stark', 2))
2-('The Riverlands', ('Joffrey/Tommen Baratheon', 8))
3-('The North', ('Balon/Euron Greyjoy', 5))
4-('The Stormlands', ('Joffrey/Tommen Baratheon', 2))
5-('The Crownlands', ('Joffrey/Tommen Baratheon', 2))
6-('Beyond the Wall', ('Mance Rayder', 1))
7-('The Reach', ('Balon/Euron Greyjoy', 2))
Los reyes con más victorias por region con rol atacante son:
1-('The Westerlands', ('Robb Stark', 2))
2-('The Riverlands', ('Joffrey/Tommen Baratheon', 7))
3-('The North', ('Balon/Euron Greyjoy', 5))
4-('The Stormlands', ('Joffrey/Tommen Baratheon', 2))
5-('The Crownlands', None)
6-('Beyond the Wall', None)
7-('The Reach', ('Balon/Euron Greyjoy', 2))
Los reyes con más victorias por region con rol atacado son:
1-('The Westerlands', None)
2-('The Riverlands', ('Joffrey/Tommen Baratheon', 1))
3-('The North', None)
4-('The Stormlands', None)
5-('The Crownlands', ('Joffrey/Tommen Baratheon', 2))
6-('Beyond the Wall', ('Mance Rayder', 1))
7-('The Reach', None)
```

