from got import *

ruta = 'data/battles.csv'
def funcion_principal():
    batallas = lee_batallas(ruta)
    print("La última batalla es:", batallas[-1])
    print("Rey con mayor y menor ejército:", reyes_mayor_menor_ejercito(batallas))
    print("Batallas con más comandantes:", batallas_mas_comandantes(batallas, regiones={'The North', 'The Riverlands'}, n=3))

if __name__ == "__main__":
    funcion_principal()
