from omegaCN7800 import OmegaCN7800
import time


from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "YjEuQ5KAaDs3V3sDY-MX1AssjmC3yqkCfDBZg0xrwUpBW3RPmD1atryfTn8_AlYFeA3iinYzoHb2nCDm7eTcqQ=="
org = "LANMAC"
bucket = "lafrioc-monitoring"
 
client = InfluxDBClient(url="http://192.168.52.75:8086", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

update_interval = 3 # in seconds

omega1 = OmegaCN7800('COM4',1) # HAY QUE CAMBIAR ESTO
time.sleep(0.1)
omega2 = OmegaCN7800('COM4',2) # HAY QUE CAMBIAR ESTO

#print("Temperatura 1: %f"%omega1.get_temp_act())
#print("Temperatura 2: %f"%omega2.get_temp_act())
time.sleep(0.1)


#while True:
#    T1 = omega1.get_temp_act()
#    T2 = omega2.get_temp_act()
#    data = "horno temperatura1(°C)=%f,temperatura2(°C)=%f"%(T1,T2)
#    write_api.write(bucket, org, data)
#    print(T1,T2)
#    time.sleep(update_interval)
# Función para leer e imprimir la temperatura de ambos dispositivos
import time
from datetime import datetime

# Asegúrate de que omega1 y omega2 están correctamente configurados

while True:
    try:
        T1 = omega1.get_temp_act()
        time.sleep(0.1)
        T2 = omega2.get_temp_act()
        time.sleep(0.1)
        
        # Imprime ambas temperaturas
        print(f"{datetime.now()} - Temperatura 1: {T1}°C, Temperatura 2: {T2}°C")

        # Escribir en la base de datos
        data = f"horno temperatura1(°C)={T1},temperatura2(°C)={T2}"
        write_api.write(bucket, org, data)

    except Exception as e:
        print(f"Error al leer las temperaturas o escribir en la base de datos: {e}")
    
    # Esperar 5 segundos
    time.sleep(update_interval)