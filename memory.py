import pandas as pd

class Memory:

    memory = None
    fileName = None
    
    def __init__(self, fileName):
        self.fileName = fileName
        #self.memory = pd.read_csv('./data/memory-' + self.fileName, header=None)
        self.memory = pd.read_csv(self.fileName, header=None)
    
    def replaceMemory(self, stockName, dataArray):
        for i in range(len(self.memory)):
            stock = self.memory.at[i, 0]
            if stockName == stock:
                isMatching = True;
                for k in range(len(dataArray)):
                    if dataArray[k] != self.memory.at[i, k+1]:
                        isMatching = False
                        break
                if isMatching == False:
                    self.memory.drop(axis=0, index=i, inplace=True)
                    data = [stockName]
                    for j in range(len(dataArray)):
                        data.append(dataArray[j])
                    self.memory.loc[len(self.memory)] = data
                    return True 
        return False

    def isPresentInMemory(self, stockName, dataArray = None):
        for i in range(len(self.memory)):
            stock = self.memory.at[i, 0]
            if stockName == stock:
                return True
        return False
        
    def addToMemory(self, stockName, dataArray = []):
        data = [stockName]
        for j in range(len(dataArray)):
            data.append(dataArray[j])
        self.memory.loc[len(self.memory)] = data

    def saveMemory(self):
        #self.memory.to_csv('./data/memory-' + self.fileName, header=False, index=False)
        self.memory.to_csv(self.fileName, header=False, index=False)