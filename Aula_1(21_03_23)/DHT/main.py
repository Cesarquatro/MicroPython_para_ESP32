'''
 * Docente:          Leopoldo André Dutra Lusquino Filho
 * Discente:         Cesar Augusto Mendes Cordeiro da Silva
  * GitHub:          https://github.com/Cesarquatro
 * Simulador online: https://wokwi.com/projects/359809346682295297
 * Aula 1 - DHT
 * 21/03/2023
'''
#Importação de bibliotecas
import dht            #sensor de umidade e temperatura
import machine as mc  #microcontroladores
import time           #manipulação de tempo (delay)

#Define a porta e o modo do pino como saída
'''
No arduino:
#define led_pin 25;
pinMode(led_pin, OUTPUT);

'''
dht_pin = mc.Pin(4, mc.Pin.IN)
dht_sensor = dht.DHT11(dht_pin)

while True:
    dht_sensor.measure() #Realiza a medida
    temperature = dht_sensor.temperature() #Armazena a medida da temperatura na variavel
    humidity = dht_sensor.humidity()       #Armazena a medida da umidade na variavel
    print(f"Temp: {temperature}ºC\tHum: {humidity}%") #print os valores
    time.sleep(2) #espera 2[s]
    
    '''
    Teste de Pull request do Deus Caio Maciel
    '''
