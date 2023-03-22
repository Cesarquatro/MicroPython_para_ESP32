'''
 * Docente:          Leopoldo André Dutra Lusquino Filho
 * Discente:         Cesar Augusto Mendes Cordeiro da Silva
 * GitHub:           https://github.com/Cesarquatro
 * Simulador online: https://wokwi.com/projects/359811062732576769
 * Aula 1 - PWM com led
 * 21/03/2023
'''
from machine import Pin, PWM
import time

'''
No arduino:
#define led_pin 25;
pinMode(led_pin, OUTPUT);

'''
pwm_pin = Pin(13, Pin.OUT)

#dutycicle = 512*
led = PWM(pwm_pin, freq = 5, duty = 512)
''' Sobre a linha acima:
    O argumento "freq" define a frequência do sinal PWM em Hertz, enquanto
    o argumento "duty" define a largura do pulso como uma porcentagem do
    ciclo total. O duty cycle pode variar de 0 a 100%.
'''

#Loop infinito | Seria o 'void loop()' no arduino
while True: 
    for i in range(0, 1023, 51): #for(i=0; i<1023, i+53)
        led.duty(i)              #muda o dutycicle para o valor do iterador 'i'
        time.sleep(0.5)          #espere 0.5[s]
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
