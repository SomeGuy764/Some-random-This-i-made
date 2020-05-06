import time
finnished = False
setTimerA = 61
setTimerB = 61
setTimerC = 61
setTimerD = 61
setTimerE = 61
setTimerF = 61
setTimerG = 61
aTok = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "'", "#", "¤", "%", "&", "/", "(", ")", "=", "?", "+", "@", "£", "$", "€", "{", "[", "]", "}", ",", ".", "-", "_", ":", ";"]

while finnished == False:
    time.sleep(0)
    print(aTok[setTimerG] + aTok[setTimerF] + aTok[setTimerE] + aTok[setTimerD] + aTok[setTimerC] + aTok[setTimerB] + aTok[setTimerA])
    setTimerA -= 1
    if setTimerA == 0:
        if setTimerB >= 1:
            setTimerA += 61
            setTimerB -= 1
    if setTimerB == 0:
        if setTimerC >= 1:
            setTimerB += 61
            setTimerC -= 1
    if setTimerC == 0:
        if setTimerD >= 1:
            setTimerC += 61
            setTimerD -= 1
    if setTimerD == 0:
        if setTimerE >= 1:
            setTimerD += 61
            setTimerE -= 1
    if setTimerE == 0:
        if setTimerF >= 1:
            setTimerE += 61
            setTimerF -= 1
    if setTimerF == 0:
        if setTimerG >= 1:
            setTimerF += 61
            setTimerG -= 1
    if setTimerA == 0:
        if setTimerB == 0:
            if setTimerC == 0:
                if setTimerD == 0:
                    if setTimerE == 0:
                        if setTimerF == 0:
                            if setTimerG == 0:
                                finnished = True