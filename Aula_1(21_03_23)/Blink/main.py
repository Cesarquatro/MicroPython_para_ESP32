'''
 * Docente:          Leopoldo André Dutra Lusquino Filho
 * Discente:         Cesar Augusto Mendes Cordeiro da Silva
 * GitHub:           https://github.com/Cesarquatro
 * Simulador online: https://wokwi.com/projects/359809378942785537
 * Aula 1 - Blink
 * 21/03/2023
'''
#Importação de bibliotecas
import machine as mc  #microcontroladores
import time           #manipulação de tempo (delay)

#Define a porta e o modo do pino como saída
'''
No arduino:
#define led_pin 25;
pinMode(led_pin, OUTPUT);

'''
led_pin = mc.Pin(13, mc.Pin.OUT) 

#Loop infinito | Seria o 'void loop()' no arduino
while True:
    led_pin.on()     #led ligado
    time.sleep(0.5)  #espere 0.5[s]
    led_pin.off()    #led ligado
    time.sleep(0.5)  #espere 0.5[s]