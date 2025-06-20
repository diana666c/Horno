from omegaCN7800 import OmegaCN7800     #Se importan dos módulos: OmegaCN7800 (presumiblemente una clase para controlar 
                                        #un dispositivo de la marca Omega CN7800) 
import time  

from libreria_bake import listas_temperatura, input_values                           #y time (para gestionar tiempos de espera).

omega_2 = OmegaCN7800('COM4',2)

omega_2.stop() 

# Obtiene la temperatura actual
current_temp_2 = omega_2.get_temp_act()
print(f"La temperatura actual es: {current_temp_2} grados")

actual_value_C2 = omega_2.get_temp_act()  # Ejemplo de temperatura actual
temp_agregada = 0  # Ejemplo de temperatura agregada (solo aplica cuando sube la temperatura)

# Solicitar inputs
setpoint, step, t_step = input_values()

# Llamada a la función
listas_C2 = listas_temperatura(actual_value_C2, temp_agregada, setpoint, step, t_step)

# Imprimir cada lista por renglones
#for lista in listas:
#    print(lista)

for i in range(len(listas_C2)):
    time.sleep(0.1)
    if i == len(listas_C2) - 1:  # Si es la última iteración
        omega_2.set_program(listas_C2[i], i, 0, 8)
        print(listas_C2[i], i, 0, 8)
    else:
        omega_2.set_program(listas_C2[i], i, 0, i+1) 
        print(listas_C2[i], i, 0, i+1)

omega_2.stop()
omega_2.run_current_program()     ## Inicia el programa de control de temperatura. Se ejecuta el programa 
                                 # actualmente configurado (program0).
