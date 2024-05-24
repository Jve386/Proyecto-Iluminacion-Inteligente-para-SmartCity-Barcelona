import json
from datetime import datetime
import matplotlib.pyplot as plt
import random
import time


# Listas para almacenar datos
timestamps = []
persons_detected_values = []
light_intensity_values = []


# Función para generar datos aleatorios simulados
def generate_random_data():
    persons_detected = random.randint(0, 10)  # Generar un número aleatorio de personas detectadas
    light_intensity = random.uniform(0, 100)  # Generar una intensidad lumínica aleatoria
    return {"persons_detected": persons_detected, "light_intensity": light_intensity}


# Función para actualizar la visualización de los datos en tiempo real
def update_visualization():
    data = generate_random_data()  # Generar datos aleatorios
    timestamp = datetime.now()  # Marca de tiempo actual
    persons_detected = data["persons_detected"]
    light_intensity = data["light_intensity"]


    timestamps.append(timestamp)
    persons_detected_values.append(persons_detected)
    light_intensity_values.append(light_intensity)


    plt.clf()  # Limpiar el gráfico anterior


    # Plot personas detectadas
    plt.plot(timestamps, persons_detected_values, 'ro-', label="Personas detectadas")


    # Plot intensidad lumínica
    plt.plot(timestamps, light_intensity_values, 'bo-', label="Intensidad lumínica")


    plt.xlabel("Tiempo")
    plt.ylabel("Valor")
    plt.title("Datos en tiempo real")
    plt.legend()
    plt.grid(True)


    plt.pause(0.1)  # Actualizar gráfico cada 0.1 segundos


# Inicializar gráfico
plt.ion()  # Habilitar modo interactivo de matplotlib
plt.figure(figsize=(10, 5))
plt.show()  # Mostrar el gráfico inicial


# Actualizar y visualizar datos en bucle
while True:
    update_visualization()
    time.sleep(1)  # Esperar 1 segundo entre actualizaciones
