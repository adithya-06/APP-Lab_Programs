#6
class Banks_SRMIST:
    def getBalance():
        return 0

class CUB(Banks_SRMIST):
    def getBalance(balance):
        return balance

class HDFC(Banks_SRMIST):
    def getBalance(balance):
        return balance

class Indian_Bank(Banks_SRMIST):
    def getBalance(balance):
        return balance


Banks_SRMIST()
print(CUB.getBalance(100))
print(HDFC.getBalance(200))
print(Indian_Bank.getBalance(300))