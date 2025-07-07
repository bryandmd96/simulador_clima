# Proyecto: Simulador de Clima

Este proyecto tiene como objetivo que practiques **programación modular** usando **clases**, la **librería NumPy** para trabajar con datos y **Matplotlib** para representar gráficamente la información.

Vas a construir una pequeña aplicación que simula datos de temperatura diaria durante un mes en distintas estaciones climáticas (ciudades) y permite visualizar estos datos mediante gráficas.

---

## Estructura del Proyecto

Crea una carpeta con el siguiente contenido:

```
simulador_clima/
│
├── clima.py         ← Clases relacionadas con los datos climáticos
├── graficos.py      ← Funciones de visualización con Matplotlib
└── main.py          ← Archivo principal que ejecuta el programa
```

---

## 1. `clima.py` – Clases y simulación

Debes crear una clase llamada `EstacionClimatica` que:

- Tenga un atributo `nombre` (por ejemplo, "Barcelona").
- Genere automáticamente un array con temperaturas aleatorias de entre 15°C y 35°C para 30 días usando **NumPy**.
- Implemente los siguientes métodos:

  ```python
  media()     → devuelve la temperatura media
  maxima()    → devuelve la temperatura máxima
  minima()    → devuelve la temperatura mínima
  resumen()   → devuelve un diccionario con Media, Máxima y Mínima
  ```

---

## 2. `graficos.py` – Gráficas de datos

Crea dos funciones utilizando **Matplotlib**:

- `graficar_temperaturas(estacion)`

  - Recibe un objeto `EstacionClimatica` y muestra un gráfico de líneas con las temperaturas por día.

- `comparar_estaciones(lista_estaciones)`
  - Recibe una lista de varias estaciones y muestra un gráfico donde se comparan todas las curvas de temperatura.

---

## 3. `main.py` – Ejecución del programa

- Importa las clases y funciones necesarias.
- Crea varias estaciones (`Barcelona`, `Madrid`, `Sevilla`, etc.).
- Muestra por consola el resumen de cada estación.
- Llama a `comparar_estaciones(...)` para visualizar las diferencias entre ciudades.
- Pregunta al usuario si quiere ver una ciudad en detalle, y si responde "sí", muestra su gráfico individual.

---

## Requisitos Técnicos

- Usa programación modular: separa tu código en los archivos `clima.py`, `graficos.py` y `main.py`.
- Usa NumPy para generar y manipular los datos.
- Usa Matplotlib para visualizar los resultados.
- Organiza bien tu código y utiliza funciones y clases correctamente.

---

## Extras (Opcionales)

- Permite elegir el número de días de simulación.
- Añade otras variables como humedad o viento.
- Exporta los datos simulados a un archivo `.csv`.

---

¡Buena suerte y a simular el clima como un auténtico científico de datos!
