import time
kaas = int(input('welk cijfer wilt u de tafel van zien?'))

def Tafels(keer:int):
    for i in range(1,11):
        print(str(keer) + ' x ' + str(i) + " = " + str(keer*i))
        time.sleep(0.5)

Tafels(kaas)

