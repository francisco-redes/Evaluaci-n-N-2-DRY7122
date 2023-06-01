import urllib.parse
import requests
# Obtener coordenadas de inicio y destino del usuario
inicio = input("Ingrese la ubicación de inicio del viaje: ")
destino = input("Ingrese la ubicación de destino del viaje: ")

while True:
   orig = inicio
   if orig == "quit" or orig == "q":
        break

   dest = destino
   if dest == "quit" or dest == "q":
        break


  
   json_data = requests.get(url).json()

   

   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   def calcular_consumo_combustible(distancia, eficiencia):
    consumo = distancia / eficiencia
    return consumo



# Obtener la ruta y la distancia utilizando la API de direcciones de MapQuest
api_key = "ReJI2akLmDH1HLRsNV4LsMuSxc1rdV7k"  # Reemplaza "TU_API_KEY" por tu propia clave de API de MapQuest
url = f"http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={inicio}&to={destino}"
response = requests.get(url)
data = response.json()

# Obtener la distancia del viaje en kilómetros
distancia = data["route"]["distance"]

# Calcular el consumo de combustible utilizando la distancia y la eficiencia de tu vehículo
eficiencia = 10  # Eficiencia de combustible en kilómetros por litro (ajusta este valor según tu vehículo)
consumo_combustible = calcular_consumo_combustible(distancia, eficiencia)

# Mostrar el consumo de combustible en litros para el viaje
print("El consumo de combustible en el viaje es de", consumo_combustible, "litros.")

    if json_status == 0:
          print("API Status: " + str(json_status) + " = A successful route call.\n")
          print("=============================================")
          print("Directions from " + (orig) + " to " + (dest))
          print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
          print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       


          print("=============================================")
      for each in json_data["route"]["legs"][0]["maneuvers"]:
           print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
      print("=============================================\n")
      elif json_status == 402:
          print("**********************************************")
          print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
          print("**********************************************\n")
      elif json_status == 611:
          print("**********************************************")
          print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
          print("**********************************************\n")
      else:
          print("************************************************************************")
          print("For Staus Code: " + str(json_status) + "; Refer to:") 
          print("https://developer.mapquest.com/documentation/directions-api/status-codes")
          print("************************************************************************\n")




