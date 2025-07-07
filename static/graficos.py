import matplotlib.pyplot as plt
import numpy as np

class graficas:

    def __init__(self): # inicializacion "Poner comentarios"
        self._lista_estaciones = []

    def graficar_temperaturas(self, estacion, list_stations): # grafricar una sola estacion meterologica
        """toma las temperaturas de una estacion y las gráfica en un tabla"""
        x = np.arange(1, 31) # rango de dias 
        for estation in list_stations:
            for ciudad, temperaturas in estation.items():
                y = temperaturas

        plt.plot(x, y, marker = "o", label=f"{estacion}") # definicion de tabla en (X.Y), marcador de punto, texto del sub indice de linea
        plt.title(f"TEMPERATURAS DE {estacion} EN 30 DÍAS") # titulo de la tabla
        plt.xlabel("Días") # titula en x
        plt.ylabel("Temperatura (°C)") # titulo en y
        
        plt.grid() # cuadrilla de tabla
        plt.legend() # sub indice de linea
        plt.show() # imprimir en pantalla

    def comparar_estaciones(self, lista_estaciones): # compara graficamente las estaciones metereologicas
        """toma las temperaturas de las estaciones y las gráfica en un tabla"""
        x = np.arange(1, 31) # rango de dias 

        fig, nx = plt.subplots() # se da valor de la funcion a una variable

        for estacion in lista_estaciones:
            for ciudad, temperaturas in estacion.items():
                nx.plot(x, temperaturas, marker='o', label=ciudad)

        plt.title(f"TEMPERATURAS EN 30 DÍAS") # titulo de la tabla
        plt.xlabel("Días") # titula en x
        plt.ylabel("Temperatura (°C)") # titulo en y
        
        plt.grid() # cuadrilla de tabla
        plt.legend() # sub indice de linea
        plt.show() # imprimir en pantalla
        self._lista_estaciones = lista_estaciones
        return

        
 

