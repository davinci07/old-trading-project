import json, requests,ast,os
import time as ti
from datetime import *
import pandas as pd
import itertools as itr


def bitmex_data(quer,endT,tmg):
    c = 500 * 60 * tmg["full"]
    d = int(tmg["rem"])
    cou = 0
    pricer = []
    sub  = [[],[],[],[],[],[]]
    ohlc = ["timestamp","open","high","low","close","volume"]
    try:
        a = int(ti.mktime(ti.strptime(endT, '%Y-%m-%d %H:%M')))
    except:
        a = int(ti.mktime(ti.strptime(endT, '%Y-%m-%dT%H:%M')))
    ######################  ###################################
    ###     (Semi)      REUSABLE ENGINE                   ###
    #########################################################        
    b = a - c #Edit the third number by (epoch(start) - epoch(end
    while(a != b): 
        endT = datetime.fromtimestamp(a).isoformat()
        try:
            qu = {"binSize":"1m","partial": False, "symbol":quer,"count":500,"reverse":False,"endTime":endT}
            thing=("https://www.bitmex.com/api/v1/trade/bucketed")
            rep = requests.get(thing, params = qu)
        except:
            print("Contact the dev with your issue with the code: " + str(rep.status_code))
            return(-1)
        cou += 1
        print("Batch: " + str(cou) + " Time: "+ str(endT) +"; ", end="\r")
        print(rep.headers["x-ratelimit-remaining"], end="\r")
        if (int(rep.headers["x-ratelimit-remaining"]) < 5):
            print("Please wait...")
            ti.sleep(310.0)
        rep = json.loads(rep.content) 
        for est in ohlc:
            for i in range(len(rep)):
                pricer.append(rep[i][est])
            for i in range(len(pricer)):
                sub[ohlc.index(est)].append(pricer[i])
            pricer = []
        a -= (500 * 60)
    #########################################################
    a = datetime.fromtimestamp(a).isoformat()
    qu = {"binSize":"1m","partial": False, "symbol":quer,"count": d,"reverse":False,"endTime":a}
    thing=("https://www.bitmex.com/api/v1/trade/bucketed")
    rep = requests.get(thing, params = qu)
    rep = json.loads(rep.content)
    #########################################################
    for est in ohlc:
        for i in range(len(rep)):
            pricer.append(rep[i][est])  
        sub[ohlc.index(est)].extend(pricer)
        pricer =[]
    print("Last Batch", end="\r")
    print(len(sub[0]))
    supe = pd.DataFrame(sub).transpose()
    head = [quer + ohlc[i] for i in range(len(ohlc))]
    file = str("bitmex"+ quer +"3.csv")
    with open(file, 'a') as f:
        supe.to_csv(f,index=False,header=head)

def test():
    bitmex_data("XBTUSD",str(datetime.now().strftime("%Y-%m-%d")) + "T00:00",{"full":2,"rem":440})
    #bitmex_data(".BCHXBT",str(datetime.now().strftime("%Y-%m-%d")) + "T00:00",[2,440])



