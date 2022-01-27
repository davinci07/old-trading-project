import numpy as np
import pandas as pd
import os

def get_data():
    exc = input("Enter name of exchange the data was pulled from: ")
    asset = input("Enter name of the asset you wish to work with: ")
    return({"exc":exc,"asset":asset})

def gen():
    excas = get_data()
    total = [["STATS","Mean","Variance","Volatility"]]
    ohlc = ["open","high","low","close","volume"]
    try:
        exas = pd.read_csv(excas["exc"] + excas["asset"] + "1.csv") 
    except:
        print("File Not Found")
        get_data()
    for i in range(len(ohlc)):
        dub = []
        dub.append(excas["asset"]+ohlc[i])
        dub.append(exas[excas["asset"]+ohlc[i]].mean())
        dub.append(exas[excas["asset"]+ohlc[i]].var())
        dub.append(exas[excas["asset"]+ohlc[i]].std())
        total.append(dub)
    total = pd.DataFrame(total).transpose()
    file = (excas["exc"] + "stats.csv")
    path = os.getcwd() + "\\" + file
    if(os.path.isfile(path)):
        print("Existing file")
        with open(file, 'a') as f:
            full.to_csv(f,index=False,header=False)
    else:
        with open(file, 'a') as f:
            full.to_csv(f,index=False,header=ohlc)
    print("")
    print("Success!")
    print("")

def corr():
    exc = input("Enter Exchange to work with: ")
    asA = input("Enter First Asset/Pair:  ")
    asB = input("Enter Second Asset/Pair:  ")
    full = []
    ohlc = ["","open","high","low","close","volume"]
    try:
        csvA = pd.read_csv(exc + asA + "1.csv")
        csvB = pd.read_csv(exc + asB + "1.csv")
    except:
        print("File Not Found")
        exc = input("Enter Exchange to work with: ")
        asA = input("Enter First Asset/Pair:  ")
        asB = input("Enter Second Asset/Pair:  ")
    full.append(asA + "/" + asB)
    for i in range(len(ohlc)):
        try:
            full.append(csvA[asA + ohlc[i]].corr(csvB[asB+ohlc[i]]))
        except:
            print(ohlc[i])
    full = pd.DataFrame(full).transpose()
    file = (exc + "corr.csv") 
    path = os.getcwd() + "\\" + file
    if(os.path.isfile(path)):
        print("Existing file")
        with open(file, 'a') as f:
            full.to_csv(f,index=False,header=False)
    else:
        with open(file, 'a') as f:
            full.to_csv(f,index=False,header=ohlc)
    print("")
    print("Success!")
    print("")

def rollvol():
    asA = get_data()
    full = []
    ohlc = ["","open","high","low","close","volume"]
    try:
        csvA = pd.read_csv(asA["exc"] + asA["asset"] + "1.csv")
    except:
        print("File Not Found")
        get_data()
    print(" N / A temporary")
    '''for i in range(len(ohlc)):
        dub = []
        dub.append(pd.rolling_std('''
    
    
def rollhr():
    print("Coming Soon....")

def hrat():
    print("Coming Soon....")
