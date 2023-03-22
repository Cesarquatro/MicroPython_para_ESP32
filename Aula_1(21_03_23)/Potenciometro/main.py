'''
 * Docente:          Leopoldo André Dutra Lusquino Filho
 * Discente:         Cesar Augusto Mendes Cordeiro da Silva
 * GitHub:           https://github.com/Cesarquatro
 * Simulador online: https://wokwi.com/projects/359810557911367681
 * Aula 1 - Potenciometro
 * 21/03/2023
'''
#Importação de bibliotecas
from machine import ADC, Pin #Da lib machine importe esses métodos, conversor AD e Pinos
import time                  #manipulação de tempo (delay)

#criando um objeto que vai usar o conversor analógico digital no pino
adc = ADC(Pin(36))

while True:
    value = adc.read() #Faz a leitura da porta
    print(f"Value do ADC: {str(value)} bits") #imprime o valor em bits
    print(f"Value do ADC: {str(value * 3.3/4096)} V") ##imprimi o valor em [V]
    time.sleep(0.2) #Espera 0.2[s]
