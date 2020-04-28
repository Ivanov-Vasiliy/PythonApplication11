import numpy as np
from myxml import downloadSquareFromXML, saveSquareInXml

class Square:

    def __init__(self, N = 4): 
        self.N = 4
        self.square = np.zeros((N,N), dtype=int)

    def download(self):
        self.N, self.square = downloadSquareFromXML()

    def save(self):
        saveSquareInXml(self.N, self.square)

    def isright(self):
        sq = np.copy(self.square)
        for i in range(0,self.N):
            for j in  range(0,self.N):
                if (sq[i][j] < 1) or (sq[i][j] > 4):
                    return False
        for i in range(0,self.N):
            for j in  range(0,self.N-1):
                if sq[i][j] == sq[i][j+1]:
                    return False
        for j in range(0,self.N):
            for i in  range(0,self.N-1):
                if sq[i][j] == sq[i+1][j]:
                     return False
        if (sq[0][0] == sq[0][1]) or (sq[0][0] == sq[1][0]) or (sq[0][0] == sq[1][1]) or (sq[0][1] == sq[1][0]) or (sq[0][1] == sq[1][1]) or (sq[1][0] == sq[1][1]):
            return False
        if (sq[0][2] == sq[0][3]) or (sq[0][2] == sq[1][2]) or (sq[0][2] == sq[1][3]) or (sq[0][3] == sq[1][2]) or (sq[0][3] == sq[1][3]) or (sq[1][2] == sq[1][3]):
            return False
        if (sq[2][0] == sq[2][1]) or (sq[2][0] == sq[3][0]) or (sq[2][0] == sq[3][1]) or (sq[2][1] == sq[3][0]) or (sq[2][1] == sq[3][1]) or (sq[3][0] == sq[3][1]):
            return False
        if (sq[2][2] == sq[2][3]) or (sq[2][2] == sq[3][2]) or (sq[2][2] == sq[3][3]) or (sq[2][3] == sq[3][2]) or (sq[2][3] == sq[3][3]) or (sq[3][2] == sq[3][3]):
            return False
        return True
        
