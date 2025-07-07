import numpy as np



class EstacionClimatica:
    def __init__(self, ciudad):
        """
        Inicializa los atributos
        Argumentos posicionales:
        nombre - str nombre de la ciudad
        """
        self._ciudad = str(ciudad).upper()
        self._temperturas_mes = np.random.randint(15,35, 30)
        self._media = {}
        self._max = {}
        self._min = {}
        self._resumen = {}
        

    def temperatura_mes(self):
        print(f"TEMPERATURA DE {self._ciudad} EN EL ULTIMO MES")
        print(self._temperturas_mes)
        print("----------" * 10)
        return self._temperturas_mes

    def media(self):
        print("--- Temp. MEDIA ---")
        self._media.update({f"Media" : int(self._temperturas_mes.mean())}) #Media
        for product_search, quantity_search in self._media.items():
                print(f"{product_search} : {quantity_search}")
        print("-------------------")
        
    
    def maxima(self):
        print("--- Temp. MAXIMA ---")
        self._max.update({f"Maxima" : int(self._temperturas_mes.max())}) #Max
        for product_search, quantity_search in self._max.items():
                print(f"{product_search} : {quantity_search}")
        print("--------------------")

    def minima(self):
        print("--- Temp. MINIMA ---")
        self._min.update({f"Minima" : int(self._temperturas_mes.min())}) #min
        for product_search, quantity_search in self._min.items():
                print(f"{product_search} : {quantity_search}")
        print("--------------------")

    def resumen(self):
        self._media.update({f"Media" : int(self._temperturas_mes.mean())}) #Media
        self._max.update({f"Maxima" : int(self._temperturas_mes.max())}) #Max
        self._min.update({f"Minima" : int(self._temperturas_mes.min())}) #min

        self._resumen.update({**self._media, **self._max, **self._min})
        return self._resumen

    

