import urllib.parse
import requests

def calcular_consumo_combustible(distancia, eficiencia):
    consumo = distancia / eficiencia
    return consumo

while True:
    inicio = input("Por favor ingrese la ubicación de origen del viaje (o 'q' para salir): ")
    if inicio.lower() == 'q':
        break
    
    destino = input("Por favor ingrese la ubicación de destino del viaje (o 'q' para salir): ")
    if destino.lower() == 'q':
        break

    tipo_vehiculo = input("Por favor ingrese el tipo de vehículo en el que viaja: ")
    eficiencia = float(input("Por favor ingrese la eficiencia de combustible de su vehículo (km/l): "))

    api_key = "ReJI2akLmDH1HLRsNV4LsMuSxc1rdV7k"  # Reemplaza "TU_API_KEY" por tu propia clave de API de MapQuest
    url = f"http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={inicio}&to={destino}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error al obtener la información del viaje. Por favor, verifique los datos ingresados.")
        continue

    data = response.json()

    if data["info"]["statuscode"] != 0:
        print("No se pudo encontrar una ruta válida para el viaje. Por favor, verifique los datos ingresados.")
        continue

    distancia = data["route"]["distance"]
    tiempo = data["route"]["formattedTime"]
    maneuvers = data["route"]["legs"][0]["maneuvers"]

    consumo_combustible = calcular_consumo_combustible(distancia, eficiencia)
    print("////////////////////////////////////////////////////////////////////////////////////////")

    print("\nInformación de su viaje:")
    print("Origen:", inicio)
    print("Destino:", destino)
    print("Kilómetros recorridos:", "{:.2f}".format(distancia), "km")
    print("Duración del viaje:", tiempo)
    print("Tipo de vehículo:", tipo_vehiculo)
    print("Eficiencia de combustible:", eficiencia, "km/l")
    print("Consumo de combustible:", "{:.2f}".format(consumo_combustible), "litros")
 
    print("////////////////////////////////////////////////////////////////////////////////////////////////")
    print("\nIndicaciones de su viaje:")
    for index, maneuver in enumerate(maneuvers, start=1):
        print(f"{index}. {maneuver['narrative']}")

    print("\n")
print("////////////////////////////////////////////////////////////////////////////////////////////////////")
print("Gracias por preferirnos. ¡Hasta pronto!")
print("////////////////////////////////////////////////////////////////////////////////////////////////////")