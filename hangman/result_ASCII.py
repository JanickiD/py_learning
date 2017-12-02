# -*- coding:UTF-8 -*-
class result:
    __result = 6
    
    def __init__(self):
        pass
        
    def setResult(self):
        self.__result -= 1
        
    def getResult(self):
        return self.__result    
    
    def showResult(self):
        if self.__result == 6:
            print("=======")
            print("||    | ")
            print("||")
            print("||")
            print("||")
            print("||")
            print("||__________")
        if self.__result == 5:
            print("=======")
            print("||    | ")
            print("||    O")
            print("||")
            print("||")
            print("||")
            print("||__________")
        if self.__result == 4:
            print("=======")
            print("||    | ")
            print("||    O")
            print("||   /")
            print("||")
            print("||")
            print("||__________")
        if self.__result == 3:
            print("=======")
            print("||    | ")
            print("||    O")
            print("||   / \ ")
            print("||")
            print("||")
            print("||__________")
        if self.__result== 2:
            print("=======")
            print("||    | ")
            print("||    O")
            print("||   /X\ ")
            print("||")
            print("||")
            print("||__________")
        if self.__result == 1:
            print("=======")
            print("||    | ")
            print("||    O")
            print("||   /X\ ")
            print("||   /")
            print("||")
            print("||__________")                        
        if self.__result == 0:
            print("=======")
            print("||    | ")
            print("||    O")
            print("||   /X\ ")
            print("||   / \\")
            print("||")
            print("||__________")  
            print("Przegrałes!")