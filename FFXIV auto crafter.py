import pyautogui
import time

def sleep_inicial():
    for x in range(5, 0, -1):
        print("O script vai comecar em " + str(x) + "!")
        time.sleep(1)
    print("Vai comecar!")
    time.sleep(1)

# O "tempo_entre_crafts" deve ser o tempo que a craft demorou 
# arredondado ao inteiro superior mais proximo mais 3.
# Ex 1 : se uma craft demorou 31,73 seg , então tempo_entre_crafts = 32,00 (31,73 arredondado ao inteiro superior mais proximo) + 3 = 35  
# Ex 2 : se uma craft demorou 10,30 seg , então tempo_entre_crafts = 11,00 (10,30 arredondado ao inteiro superior mais proximo) + 3 = 14  
def craftar(numero_crafts: int, tempo_entre_crafts): 
    for x in range(numero_crafts):
        print("A comecar a craft.")
        pyautogui.click(clicks=2, interval=2)
        time.sleep(3)
        print("Craft numero " + str(x+1) + " num total de " + str(numero_crafts) + ".")
        pyautogui.click(clicks=2, interval=2)
        time.sleep(tempo_entre_crafts)
        print("Craft terminada!")
        time.sleep(2)
    print("Terminou o processo!")
        
sleep_inicial()
craftar(numero_crafts=36, tempo_entre_crafts=43)