'''
 * Docente:          Leopoldo André Dutra Lusquino Filho
 * Discente:         Cesar Augusto Mendes Cordeiro da Silva
 * GitHub:           https://github.com/Cesarquatro
 * Simulador online: https://wokwi.com/projects/359907054174260225
 * Aula 1 - Controle de um sensor de movimento
 * 21/03/2023
'''
#Importação de bibliotecas
from machine import Pin
import time

# Define o pinos conectado aos LEDs como uma saída
vermelho_pin = Pin(4, Pin.OUT)
verde_pin = Pin(2, Pin.OUT)

# Define o pino conectado ao sensor como uma entrada
sensor_pin = Pin(13, Pin.IN)

# Loop principal do programa:
while True:

    #como o valor da leitura do sensor é 1 ou 0, o if interpreta o 1 como true
    # Caso o movimento seja detectado
    if sensor_pin.value():
        # Se o sensor detectar algo, acende o LED verde e apaga o LED vermelho
        verde_pin.on()                # verde ligado
        vermelho_pin.off()            # vermelho desliago
        print("Eu me remecho muito")  # Imprime mensagem indicando que algo foi detectado
    
    else:
        # Se o sensor não detectar nada, apaga o LED verde e acende o LED vermelho
        verde_pin.off()             # verde desliago
        vermelho_pin.on()           # vermelho ligado
        print("Eu não me remecho")  # Imprime mensagem indicando que nada foi detectado

    time.sleep(0.5)                 # espere 0,5s