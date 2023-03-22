'''
 * Docente:          Leopoldo André Dutra Lusquino Filho
 * Discente:         Cesar Augusto Mendes Cordeiro da Silva
 * GitHub:           https://github.com/Cesarquatro
 * Simulador online: https://wokwi.com/projects/359862803758179329
 * Aula 1 - LCD I2C
 * 21/03/2023
 * Codigo comentado pelo ChatGPT
'''
from time import sleep_ms, ticks_ms  # Importa as funções sleep_ms e ticks_ms da biblioteca time
from machine import I2C, Pin  # Importa as classes I2C e Pin da biblioteca machine
from i2c_lcd import I2cLcd  # Importa a classe I2cLcd da biblioteca i2c_lcd

AddressOfLcd = 0x27  # Define o endereço do display LCD

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)  # Instancia um objeto I2C com os pinos GPIO 22 e GPIO 21 como SCL e SDA, respectivamente
lcd = I2cLcd(i2c, AddressOfLcd, 2, 16)  # Instancia um objeto I2cLcd com o objeto I2C, endereço e tamanho do display

def testLcd(num):
    lcd.move_to(3,0)  # Move o cursor para a posição (3,0)
    lcd.putstr('Cesarquatro')  # Escreve 'Cesarquatro' na tela
    lcd.move_to(0,1)  # Move o cursor para a posição (0,1)
    lcd.putstr("Hello World: " + str(num))  # Escreve 'Hello World: num' na tela, onde num é um número inteiro

if __name__ == '__main__':
    for i in range(100):
        testLcd(i)  # Chama a função testLcd com o parâmetro i
        sleep_ms(200)  # Espera 200ms
