from omegaCN7800 import OmegaCN7800     #Se importan dos módulos: OmegaCN7800 (presumiblemente una clase para controlar 
                                        #un dispositivo de la marca Omega CN7800) 
import time                             #y time (para gestionar tiempos de espera).

from libreria_bake import listas_temperatura, input_values

omega_1 = OmegaCN7800('COM4',1)   #Se crea una instancia del dispositivo conectado al puerto COMXX con un identificador 1

omega_1.stop()      #Se detiene el dispositivo (probablemente para asegurarse de que no esté en funcionamiento al inicio). 

# Obtiene la temperatura actual
current_temp_1 = omega_1.get_temp_act()
print(f"La temperatura actual es: {current_temp_1} grados")

actual_value_C1 = omega_1.get_temp_act()  # Ejemplo de temperatura actual
temp_agregada = 0  # Ejemplo de temperatura agregada (solo aplica cuando sube la temperatura)

# Solicitar inputs
setpoint, step, t_step = input_values()

# Llamada a la función
listas_C1 = listas_temperatura(actual_value_C1, temp_agregada, setpoint, step, t_step)

# Imprimir cada lista por renglones
#for lista in listas_C1:35
#    print(lista)

for i in range(len(listas_C1)):
    time.sleep(0.1)
    if i == len(listas_C1) - 1:  # Si es la última iteración
        omega_1.set_program(listas_C1[i], i, 0, 8)
        print(listas_C1[i], i, 0, 8)
    else:
        omega_1.set_program(listas_C1[i], i, 0, i+1) 
        print(listas_C1[i], i, 0, i+1)


omega_1.stop()
omega_1.run_current_program()     ## Inicia el programa de control de temperatura. Se ejecuta el programa 
                                 # actualmente configurado (program0).
