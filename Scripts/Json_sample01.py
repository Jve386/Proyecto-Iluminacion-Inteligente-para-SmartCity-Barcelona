import json
from datetime import datetime
import matplotlib.pyplot as plt


# Función para cargar datos desde un archivo JSON
def load_data_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


# Función para actualizar la visualización de los datos en tiempo real
def update_visualization(data):
    timestamp = [datetime.now().strftime("%H:%M:%S")] * len(data["persons_detected"])  # Lista de marcas de tiempo con la misma longitud que personas detectadas e intensidad lumínica
    persons_detected = data.get("persons_detected", [])
    light_intensity = data.get("light_intensity", [])


    plt.clf()  # Limpiar el gráfico anterior


    # Subgráfico para personas detectadas
    plt.subplot(2, 1, 1)
    plt.plot(timestamp, persons_detected, 'ro-', label="Personas detectadas")
    plt.xlabel("Tiempo")
    plt.ylabel("Personas")
    plt.title("Personas detectadas en tiempo real")
    plt.grid(True)


    # Subgráfico para intensidad lumínica
    plt.subplot(2, 1, 2)
    plt.plot(timestamp, light_intensity, 'bo-', label="Intensidad lumínica")
    plt.xlabel("Tiempo")
    plt.ylabel("Intensidad")
    plt.title("Intensidad lumínica en tiempo real")
    plt.grid(True)


    plt.tight_layout()  # Ajustar el diseño de los subgráficos para superposiciones
    plt.pause(0.1)  # Actualizar gráfico cada 0.1 segundos


# Inicializar gráfico
plt.ion()  # Habilitar modo interactivo de matplotlib
plt.figure(figsize=(10, 5))
plt.show()  # Mostrar el gráfico inicial


# Cargar datos desde el archivo JSON
file_path = "datasensor.json"  # Ruta del archivo JSON
data = load_data_from_json(file_path)
# Procesar y visualizar los datos
update_visualization(data)