#
#
#
#
#

from genericpath import isfile
from os import path
from os import mkdir

class raw_data:
    def __init__(self):
        pass

    def fileCheck(self):
        if path.isdir("data-archvie"):
            pass
        else:
            mkdir("data-archive")
        
        if isfile("data-archive/stocklist.txt"):
            pass
        else:
            APIRequest(self, 0)

        pass

    def fileCreate(self):
        pass

    def APICreate(self):
        pass

    def APIRequest(self):
        pass
    
    def setDataUse(self):
        pass

    def exportDatabase(self):
        pass