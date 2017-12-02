# -*- coding: UTF-8 -*-
import random
import os
import result_ASCII

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
    __result = 6
    
    def __init__(self, wylosowane_slowo = wyraz()):
        self.wylosowane_slowo = wylosowane_slowo
        self.uzyte_litery=wylosowane_slowo.uzyte_litery
        
   
    def getChar(self):      #pobiera i zwraca znak od gracza
        self.char =  input("Wpisz litere: ")
    #    self.char = "'" + self.char + "'"
        return self.char
    
    def setStatement(self, statementValue):
        if not statementValue:
            self.__statement = "Podana litera nie znajduje się w wyrazie"
        if statementValue:
            self.__statement = "Brawo! Trafiłeś"
    
    def getStatement(self):
        print(self.__statement)
    

 
        
    
    def checkChar(self, wylosowane_slowo_tablica, playground, show_ascii):  #sprawdza czy znak występuję w słowie(jeżeli tak -wypisuje)
        char = self.getChar()
        result_indicator = 0
        for i in range(len(wylosowane_slowo_tablica)):
            self.uzyte_litery.add(str(char)) 
            if wylosowane_slowo_tablica[i] == str(char):
                self.setStatement(True)
                playground[i*2] = char
                result_indicator = 1
                continue
        if result_indicator != 1:
            show_ascii.setResult()
        
    def display(self, playground,): 
        os.system("cls")
        print("*****************W I S I E L E C*************************")
        print("".join(playground).center(40), "\n")
        self.getStatement()
        print("Użyłeś już następujących liter: ", list(self.uzyte_litery))
        self.setStatement(False)
        
    def showASCII(self, show_ascii): 
        show_ascii.showResult()

########################
#print("*****************W I S I E L E C*************************")
res =result_ASCII.result()
wylosowane_slowo = wyraz()
gra = game()
gra.display(wylosowane_slowo.plgrnd,)
while res.getResult() != 0 and wylosowane_slowo.plgrnd.count('_') > 0:
    gra.checkChar(wylosowane_slowo.slowo_tablica, wylosowane_slowo.plgrnd, res )
    gra.display(wylosowane_slowo.plgrnd,)
    res.showResult()

exit=input("Press enter to exit")
   
