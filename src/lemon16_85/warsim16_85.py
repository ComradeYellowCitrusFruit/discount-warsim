from Lemon16_85 import *

class save():
    def indexCompile(self, attributes: list) -> bytes:
        ### Atrributes contains in the following order:
        ### Country count
        ### Difficulty
        ### Rebel status
        ind = '-Index\n'
        ind += str(attributes[0]) + '\n'
        ind += str(attributes[1]) + '\n'
        ind += str(attributes[2]) + '\n'
        self.index = Encode(ind.encode('unicode-escape'))
        return Encode(ind.encode('unicode-escape'))
    def playerCompile(self, attributes: list) -> bytes:
        ### Atrributes contains in the following order:
        ### Name
        ### Gold
        ### Land
        ### Elites
        ### Soldiers
        ### Peasants
        ### Tech
        ply = '-Player\n'
        ply += attributes[0] + '\n'
        ply += str(attributes[1]) + '\n'
        ply += str(attributes[2]) + '\n'
        ply += str(attributes[3]) + '\n'
        ply += str(attributes[4]) + '\n'
        ply += str(attributes[5]) + '\n'
        ply += str(attributes[6]) + '\n'
        self.ply = Encode(ply.encode('unicode-escape'))
        return Encode(ply.encode('unicode-escape'))
    def foreignCompile(self, attributes: list) -> bytes:
        ### Atrributes contains in the following order:
        ### ID
        ### Name
        ### Gold
        ### Land
        ### Elites
        ### Soldiers
        ### Peasants
        ### Tech
        fgn = '-Foreign\n'
        fgn += str(attributes[0]) + '\n'
        fgn += attributes[1] + '\n'
        fgn += str(attributes[2]) + '\n'
        fgn += str(attributes[3]) + '\n'
        fgn += str(attributes[4]) + '\n'
        fgn += str(attributes[5]) + '\n'
        fgn += str(attributes[6]) + '\n'
        fgn += str(attributes[7]) + '\n'
        if self.fgn:
            self.fgn += Encode(fgn.encode('unicode-escape'))
        else:
            self.fgn = Encode(fgn.encode('unicode-escape'))
        return Encode(fgn.encode('unicode-escape'))
    def finalCompile(self):
        final = self.index + self.ply + self.fgn
        self.final = final
        return final
class load():
    def __init__(self, file: bytes):
        self.file = file
    def decompile(self):
        self.decodedFile = Decode(self.file)
        File = self.decodedFile.split('-')
        for i in File:
            if i.partition('\n')[0] == 'Index':
                self.Index = i 
            elif i.partition('\n')[0] == 'Player':
                self.ply = i
            elif i.partition('\n')[0] == 'Foreign':
                if self.fgn:
                    self.fgn += i
                else:
                    self.fgn = i
