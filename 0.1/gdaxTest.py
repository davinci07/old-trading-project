import json,requests,ast,sys,pytz,os 
import time as ti
from datetime import *
import pandas as pd


def gdax_data(req,strT,tmg):
    cou = 0
    ftn = 0
    pricer = []
    sub  = [[],[],[],[],[],[]]
    ohlc = ["time","open","high","low","close","volume"]
    a = int(ti.mktime(ti.strptime(strT, '%Y-%m-%dT%H:%MZ')))
    d = tmg["rem"] * 60
    #a - ((300*60*tmg["full"])+d)
    for g in range(tmg["full"]):
        bti = str(datetime.fromtimestamp(a).isoformat())+"Z"
        k = a - (300 * 60)
        kti = str(datetime.fromtimestamp(k).isoformat())+"Z"
        print(bti,kti)
        thing =("https://api.gdax.com/products/"+ req + "/candles")
        que = {"start": kti, "end": bti,"gran":60}
        try:
            rep = requests.get(thing, params = que)
            rep.raise_for_status()
            print(rep)
        except:
            if rep.status_code == 429:
                print("Please Wait...")
                ti.sleep(3.0)
                rep = requests.get(thing, params = que)
                rep.raise_for_status()
            else:
                print("Contact the dev with your issue with the code: " + str(rep.status_code))
                os.system("pause")
        rep = json.loads(rep.content)
        for i in range(len(rep)):
            for est in range(len(ohlc)):
                sub[est].append(rep[i][est])
        a -= 300*60
        ti.sleep(3.0)
    bti = str(datetime.fromtimestamp(a).isoformat())+"Z"
    k = a - d
    kti = str(datetime.fromtimestamp(k).isoformat())+"Z"
    print(bti,kti)
    thing =("https://api.gdax.com/products/"+ req + "/candles")
    que = {"start": kti, "end": bti,"gran":60}
    try:
        rep = requests.get(thing, params = que)
        rep.raise_for_status()
        print(rep)
    except:
        if rep.status_code == 429:
            print("Please Wait...")
            ti.sleep(5.0)
            rep = requests.get(thing, params = que)
            rep.raise_for_status()
        else:
            print("Contact the dev with your issue with the number: " + str(rep.status_code))
            os.system("pause")
    rep = json.loads(rep.content)
    for i in range(len(rep)):
        for est in range(len(ohlc)):
            sub[est].append(rep[i][est])
    for n in range(len(sub[0])): 
        sub[0][n] = ti.strftime('%Y-%m-%dT%H:%M:%SZ', ti.gmtime(sub[0][n]))
    supe = pd.DataFrame(sub).transpose()
    cols = [0,3,2,1,4,5]
    supe = supe[cols]
    head = [req + ohlc[i] for i in range(len(ohlc))]
    file = str("gdax"+req+"1.csv")
    with open(file, 'a') as f:
        supe.to_csv(f,index=False,header=head)
    print("Success " + str(req))
            
        
def test():
    tim = str(datetime.now().strftime("%Y-%m-%d")) + "T00:00Z"
    a = gdax_data("BTC-USD",tim,{'full': 4, 'rem': 240.0})
    return(a)






       
            
            
            
            
            
            
            
        
