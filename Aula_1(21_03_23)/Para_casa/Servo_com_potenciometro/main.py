'''
 * Docente:          Leopoldo André Dutra Lusquino Filho
 * Discente:         Cesar Augusto Mendes Cordeiro da Silva
 * GitHub:           https://github.com/Cesarquatro
 * Simulador online: https://wokwi.com/projects/359817107629915137
 * Aula 1 - Potenciometro controlado por servo
 * 21/03/2023
'''

#Importação de bibliotecas
from machine import ADC, Pin, PWM
import time

#funcão map do arduino, funciona como uma regra de 3
def mapValores(x, entrada_min, entrada_max, saida_min, saida_max):
    return int((x - entrada_min) * (saida_max - saida_min) / (entrada_max - entrada_min) + saida_min)


#criando um objeto 'potenciometro' que vai usar o conversor analógico digital
pot = ADC(Pin(36))

#criando um objeto 'servo' que vai usar o conversor analógico digital
servo = PWM(Pin(22, mode=Pin.OUT))
servo.freq(50)

# 0.5ms/20ms = 0.025 = 2.5% duty cycle
# 2.4ms/20ms = 0.12 = 12% duty cycle

# 0.025*1024=25.6
# 0.12*1024=122.88

#tempo de delay
tempoEspera = 1 #[s]

#loop infinito || seria o void lool() no arduino
while True:
    valor = pot.read() #leitura do potenciometro

    '''Mapeamento de Valores:
       -O servo calibrado nesse simulador aceita valores entre 26 e 123
       -A GPIO36 (Sensor VP) usada pelo potenciometro possui o padrão
        de 12bits, logo, lê valores entre 0 e 4095
    '''
    valor = mapValores(valor, 0, 4095, 26, 123) #atualiza a var. com valores mapeados
    time.sleep(tempoEspera) #espera
    
    #imprimi com valores mapeados novamente para graus entre 0 e 180, porém não atualiza a variavel valor
    print(f"Angulo do Servo:\t{mapValores(valor, 26, 123, 0, 180)}º")

    servo.duty(valor) #passa o valor que o servo deve virar  
    
'''
 *O duty cycle do PWM se refere à proporção entre o tempo em que o sinal 
 está em nível lógico alto (ou "1") e o tempo em que está em nível lógico
 baixo (ou "0"). Em outras palavras, é a fração do tempo em que o sinal
 está em estado ativo em relação ao período total do sinal.
 O método PWM da biblioteca "machine" do micropython permite configurar a
 frequência e a largura do pulso de saída para gerar um sinal PWM em um
 pino específico do microcontrolador. Para usar o método PWM, é necessário
 primeiro importar a biblioteca "machine" e instanciar um objeto PWM com os
 parâmetros necessários.
 Por exemplo, para criar um sinal PWM em um pino específico com frequência
 de 1000 Hz e largura de pulso de 50%
'''
