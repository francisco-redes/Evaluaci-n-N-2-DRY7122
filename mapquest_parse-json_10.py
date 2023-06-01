import urllib.parse
import requests

def calcular_consumo_combustible(distancia, eficiencia):
    consumo = distancia / eficiencia
    return consumo

# Obtener coordenadas de inicio y destino del usuario
inicio = input("Ingrese la ubicación de origen del viaje: ")
destino = input("Ingrese la ubicación de destino del viaje: ")

# Obtener información del viaje utilizando la API de direcciones de MapQuest
api_key = "TU_API_KEY"  # Reemplaza "TU_API_KEY" por tu propia clave de API de MapQuest
url = f"http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={inicio}&to={destino}"
response = requests.get(url)

# Verificar el estado de la respuesta
if response.status_code != 200:
    print("Error al obtener la información del viaje. Por favor, verifica los datos ingresados.")
    exit()

data = response.json()

# Verificar si se encontró una ruta válida
if data["info"]["statuscode"] != 0:
    print("No se pudo encontrar una ruta válida para el viaje. Por favor, verifica los datos ingresados.")
    exit()

# Extraer información del viaje de la respuesta JSON
distancia = data["route"]["distance"]  # Distancia en kilómetros
tiempo = data["route"]["formattedTime"]  # Duración del viaje
maneuvers = data["route"]["legs"][0]["maneuvers"]  # Indicaciones del viaje

# Calcular el consumo de combustible utilizando la distancia y la eficiencia de tu vehículo
eficiencia = 10  # Eficiencia de combustible en kilómetros por litro (ajusta este valor según tu vehículo)
consumo_combustible = calcular_consumo_combustible(distancia, eficiencia)

# Imprimir la información del viaje
print("Origen:", inicio)
print("Destino:", destino)
print("Kilómetros recorridos:", distancia, "km")
print("Duración del viaje:", tiempo)
print("Consumo de combustible:", consumo_combustible, "litros")

# Imprimir las indicaciones del viaje
print("\nIndicaciones del viaje:")
for index, maneuver in enumerate(maneuvers, start=1):
    print(f"{index}. {maneuver['narrative']}")


