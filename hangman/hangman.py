# -*- coding: UTF-8 -*-
import random
import os

class wyraz:
    lista_slow={1:"stokrotka", 2:"komputera", 3:"rabarbar", 4:"kraj", 5:"prostopadłościan"}
    def __init__(self):
        self.uzyte_litery = set([])
        self.slowo = str(self.losujSlowo())
        self.litery = set(self.slowo)
        self.plgrnd = self.createPlayground()
        self.slowo_tablica = list(self.slowo)
                                                        
    
    def losujSlowo(self):
        return self.lista_slow[random.randint(1, len(self.lista_slow))]
    
    def createPlayground(self):
        self.plgrnd = list(len(self.slowo)*"_ ")
        return self.plgrnd



class game:
    __statement = ""
    
    def __init__(self, wylosowane_slowo = wyraz()):
        self.wylosowane_slowo = wylosowane_slowo
        self.uzyte_litery=wylosowane_slowo.uzyte_litery
        
   
    def getChar(self):      #pobiera i zwraca znak od gracza
        self.char =  input("wpisz litere: ")
    #    self.char = "'" + self.char + "'"
        return self.char
    
    def setStatement(self, statementValue):
        if not statementValue:
            self.__statement = "Podana litera nie znajduje się w wyrazie"
        if statementValue:
            self.__statement = "Brawo! Trafiłeś"
    
    def getStatement(self):
        print(self.__statement)
        self.state="asdf"
 
        
    
    def checkChar(self, wylosowane_slowo_tablica, playground,):  #sprawdza czy znak występuję w słowie(jeżeli tak -wypisuje)
        char = self.getChar()
        for i in range(len(wylosowane_slowo_tablica)):
            self.uzyte_litery.add(str(char)) 
            if wylosowane_slowo_tablica[i] == str(char):
                self.setStatement(True)
                playground[i*2] = char
            #if wylosowane_slowo_tablica[i] != str(char):
                #self.setStatement(False)  
                continue
        os.system("cls")
        print("".join(playground).center(40))
        self.getStatement()
        print(list(self.uzyte_litery))
        self.setStatement(False)

########################
print("*****************W I S I E L E C*************************")
wylosowane_slowo = wyraz()
gra = game()
while wylosowane_slowo.plgrnd.count('_') > 0:
    gra.checkChar(wylosowane_slowo.slowo_tablica, wylosowane_slowo.plgrnd)

