import xml.etree.ElementTree as ET

class xmlRefactor():
    def __init__(self, responseQWS):
        self.response = responseQWS

    def getNumChamado(self):
        dict = {}
        for x in ET.fromstring(self.response)[1][0]:
            dict.update({x.tag: x.text})
        return dict["cdchamado"]

    def getresponseChamado(self):
        dict = {}
        for x in ET.fromstring(self.response)[1][0]:
            dict.update({x.tag: x.text})
        return dict["nmresponsavel"]

    def getDictCalledFull(self):
        dict = {}
        for x in ET.fromstring(self.response)[1][0]:
            dict.update({x.tag: x.text})
        return dict

    def printFullItens(self):
        dictResponse = {}
        try:
            for i in ET.fromstring(self.response)[1][0]:
                dictResponse.update({i.tag: i.text})
            for i2 in dictResponse:
                print(i2, ':', dictResponse[i2])
        except IndexError or TypeError:
            for i in ET.fromstring(self.response)[0]:
                dictResponse.update({i.tag: i.text})
            for i2 in dictResponse:
                print(i2, ':', dictResponse[i2])