from random import choice
import os
import time

## Оснавная функция генерация
class generPas():
    ## Иницилизация
    def __init__(self, kolPass, razSinvol, kolSekciy, dlinaSekcii):
        self.kolPass = kolPass
        self.razSinvol = razSinvol
        self.kolSekciy = kolSekciy
        self.dlinaSekcii = dlinaSekcii
        self.passwords = []
        self.BazaSimvol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', \
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', \
        'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', \
        'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', \
        'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    ## Создаю заданое количество паролей
    def createPass(self):
        skleu = ""
        genPass = ""
        for i in range(0, self.kolPass):
            for j in range(0, self.kolSekciy):
                for q in range(0, self.dlinaSekcii):
                    if q < self.dlinaSekcii:
                        genPass += choice(self.BazaSimvol)
                if j + 1 < self.kolSekciy:
                    skleu += genPass + self.razSinvol
                else:
                    skleu += genPass
                genPass = ""
            self.passwords.insert(i, skleu)
            skleu = ""

        ##rez = self.kolPass
        ##return rez
    ## Показ пароля из созданых
    def ridPass(self, nom):
        return self.passwords[nom]

    ## вывести все созданые пароли
    def FulCreatePass(self):
        for i in range(0, self.kolPass):
            print("Pass №", i+1 ," : " , self.passwords[i] )

    ## Сохранить в фаил созданые пароли (*.txt)
    def SaveToFile(self):
        Namefile = time.strftime("%Y_%m_%d_%H.%M.%S", time.localtime())
        PTF = open( Namefile + "_pass.txt","w")
        for i in range(0, self.kolPass):
            PTF.write("Pass №" + str(i+1) + " : " + self.passwords[i] + '\n')
        PTF.close()

## Запрос даннных для генерации
print("## Пароля формата  @@@@&@@@@  ##")
kolPass = int(input("Ветите количество поролей:"))
razSinvol = str(input("Ведите разделяющий синвол:"))
kolSekciy = int(input("Ветите количество секций:"))
dlinaSekcii = int(input("Ветите длину секции:"))
print("### Готово !!! #################")

## Формирования с паролем
pas = generPas(kolPass, razSinvol, kolSekciy, dlinaSekcii)
pas.createPass()
#pas.FulCreatePass()
pas.SaveToFile()
##print(pas.ridPass(1))
##print(pas.ridPass(2))
