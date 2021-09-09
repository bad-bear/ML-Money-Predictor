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
        #Check for data folder that holds values
        if (path.isdir("data-archvie")):
            pass
        else:
            mkdir("data-archive")
        
        #Check if list of stocks to be analyzed is in folder
        if (isfile("data-archive/stocklist.txt")):
            pass
        else:
            self.APIRequest(0)

        #Check if API request are in database
        pass

    def fileCreate(self):
        pass

    def APICreate(self):
        pass

    def APIRequest(self, request):
        #Pulls list of stocks and sends the json back to check function
        if (request == 0):
            reqStr = self.APICreate(0)
            
        pass
    
    def setDataUse(self):
        pass

    def exportDatabase(self):
        pass