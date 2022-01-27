from datetime import *
import time as ti


def data_work():
    exc = input("Enter Exchange: ")
    exclist = ["gdax","polo","btm"]
    while(exc not in exclist):
        print("Retry, bad input")
        exc = input("Enter Exchange: ")
    cur = []
    cont = 'y'
    trade = ["btc","xbt","bch","ltc","eth","ALL"]
    while(cont == 'y'):
        usein = input("Please enter a pair: ")
        che = usein[:3]
        while(che not in trade):
            print("Retry, bad input")
            usein = input("Please enter a pair: ")
            che = usein[:3]
        cur.append(usein)
        if che == "ALL":
            break
        cont = input("Press y to add more pairs ")
    tist = input("Enter custom startdate or press enter for data since today: ")
    try:
        endz = int(input("Number of days back: "))
    except:
        print("not a number!!!")
        endz = int(input("Number of days back: "))
    if (exc == "gdax"):
        tail = "T00:00Z"
    elif(exc == "btm") or (exc == "polo"):
        tail = "T00:00"
    if (tist == ""):
        start = str(datetime.now().strftime("%Y-%m-%d")) + tail
    else:
        start = tist + tail
    return({"cur":cur,"exc":exc,"starttime":start,"days":endz})

def tm_mg(lst):
    if(lst["exc"] == "gdax"):
        buck = 86400 * lst["days"]
        intBuc = int(buck/(300*60))
        remBuc = (buck - (intBuc * 300 *60))/60
    elif(lst["exc"] == "btm" or lst["exc"] == "polo"):
        buck = 86400 * lst["days"]
        intBuc = int(buck/(500*60))
        remBuc = (buck - (intBuc * 500 *60))/60
    return({"full":intBuc,"rem":remBuc})

def cur_con(lst):
    gche = ["bchbtc","bchusd","ethbtc","ethusd","ltcbtc","ltcusd","btcusd"]
    bche = ["xbtusd"]
    pche = ["adaxbt","bchxbt","ethxbt","ltcxbt","xmrxbt"]
    b = lst["cur"]
    if (lst["exc"] == "gdax"):
        for i in range(len(b)):
            print(b[i])
            if (b[i] != "ALL"):
                if (b[i] not in gche):
                    raise ValueError('ASSET NOT IN EXCHANGE')
            if b[0] == "ALL":
                b = []
                for i in range(len(gche)):
                    b.append((gche[i][:3] + '-' + gche[i][3:]).upper())
                return b
            b[i] =(b[i][:3] + '-' + b[i][3:]).upper()
        return b
    elif(lst["exc"] == "polo"):
        for i in range(len(b)):
            if (b[i] != "ALL"):
                if (b[i] not in pche):
                    raise ValueError('ASSET NOT IN EXCHANGE')
            if b[0] == "ALL":
                b = []
                for i in range(len(pche)):
                  b.append(("." + pche[i]).upper())
                return b
            b[i] = ("." + b[i]).upper()
        return b
    elif(lst["exc"]== "btm"):
        for i in range(len(b)):
            if (b[i] != "ALL"):
                if (b[i] not in bche):
                    raise ValueError('ASSET NOT IN EXCHANGE')
            if b[0] == "ALL":
                b = []
                for i in range(len(bche)):
                    b.append(bche[i].upper())
                return b
            b[i] = b[i].upper()
        return b



        
    
        


