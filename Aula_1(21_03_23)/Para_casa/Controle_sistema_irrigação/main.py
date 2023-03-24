'''
 * Docente:          Leopoldo André Dutra Lusquino Filho
 * Discente:         Cesar Augusto Mendes Cordeiro da Silva
 * GitHub:           https://github.com/Cesarquatro
 * Simulador online: https://wokwi.com/projects/360047030427532289
 * Aula 1 - Controle  sistema irrigação
 * 21/03/2023
 * OBS: Como estamos em um simulador e não temos nem um sensor de 
        umidade do solo, nem uma valvula solenoide para simular,
        temos que fazer analogias. O sensor de umidade agora é o
        potenciometro vertical e o led azul representa a válvula
        que será acionada por um relé, ou seja, sua alimentação de
        energia vem de uma fonte externa.
'''

#Importação de bibliotecas
from machine import Pin, ADC
import time

#criando um objeto 'potenciometro' que vai usar o conversor analógico digital
potenciometro = ADC(Pin(14))

#Define a porta e o modo do pino como saída
releValcula = Pin(12, Pin.OUT) 

#funcão map do arduino, funciona como uma regra de 3
def mapValores(x, entrada_min, entrada_max, saida_min, saida_max):
    return int((x - entrada_min) * (saida_max - saida_min) / (entrada_max - entrada_min) + saida_min)

#loop infinito || seria o void lool() no arduino
while True:
    #Os valores da umidade seram coletados pelo sensor(potenciometro)
    umidadeSolo = potenciometro.read() #armazena os valores da leitura no variável umidadeSolo
    umidadeSolo = mapValores(umidadeSolo, 0, 4095, 0, 100) #mapeia os valores da leitura para %

    print(f"Umidade do solo:\t{umidadeSolo}%") #Imprimi o valor da umidade

    #Se a umidade for menor que 40%
    if umidadeSolo < 40:
        releValcula.on()      #Ative a valvula solenoide
        print("Irrigando...") #Imprime que esta irrigando
        time.sleep(5)         #Espera 5s com a valvula aberta
    #Se não
    else:
        releValcula.off()     #Desliga a valvula

    time.sleep(0.1)           #Espera 0.s com a valvula aberta