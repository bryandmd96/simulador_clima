import clima
import graficos

def simulador_clima():
    barcelona = clima.EstacionClimatica("barcelona")
    madrid = clima.EstacionClimatica("madrid")
    sevilla = clima.EstacionClimatica("sevilla")

    data_barcelona = (barcelona.temperatura_mes()).tolist()
    data_madrid = (madrid.temperatura_mes()).tolist()
    data_sevilla = (sevilla.temperatura_mes()).tolist()

    list_stations = [{"BARCELONA" : data_barcelona}, {"MADRID" : data_madrid}, {"SEVILLA" : data_sevilla}]

    list_estations_details = [{"BARCELONA" : barcelona.resumen()},
                            {"MADRID" : madrid.resumen()},
                                {"SEVILLA" : sevilla.resumen()}]

    graficar = graficos.graficas()
    graficar.comparar_estaciones(list_stations)

    continuos = input("Deseas ver la estacion de una ciudad en detalle (Y/N): ").strip().upper()
    if continuos == "Y":
        print("Lista de estaciones: ")
        for estacion in list_stations:
            for ciudad in estacion:
                print(ciudad)
        
        while True:
            select_search = input("Quieres seleccionar una ciudad de la lista o escribe <Q> para salir: ").strip().upper()
            
            if select_search == "Q":
                print("Saliendo del programa...")
                break
        
            for estacion in list_estations_details:
                if select_search in estacion:
                    details = estacion[select_search]
                    print("------" * 20)
                    print(f"Detalles de estación metereológica en {select_search}:")

                    for statistics, values in details.items():
                        print(f"{statistics} : {values}")
                    print("------" * 20)
                    graficar.graficar_temperaturas(select_search, list_stations)
                    break
            
            print(f"{(select_search).capitalize()} no esta en diccionario de estaciones")
    else:
        return print("Saliendo del programa...")
    
if __name__ == "__main__":
    simulador_clima()
        
           