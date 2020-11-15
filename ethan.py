from helpers import *

def rouletteColorWheel(pktNum):

    pktNumOdd = int(pktNum % 2)
    if(pktNum == 0):
        print('Pocket is green')
    elif(((pktNumOdd == 1 and ((1 <= pktNum <= 10) or (19 <= pktNum <= 28)))) or ((pktNumOdd == 0 and ((11 <= pktNum <= 18) or (29 <= pktNum <= 36))))):
        print('Pocket is red')
    elif(((pktNumOdd == 0 and ((1 <= pktNum <= 10) or (19 <= pktNum <= 28)))) or ((pktNumOdd == 1 and ((11 <= pktNum <= 18) or (29 <= pktNum <= 36))))):
        print('Pocket is black')
    else:
        print('Invalid Number')

userNum = getNum('Pick a roulette number', 0, 36, float('inf'), True)
rouletteColorWheel(userNum)
