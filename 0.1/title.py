import thung
import gdaxTest as g
import btmp
import pretty


def rocket(lt):
    cur = thung.cur_con(lt)
    for e in range(len(cur)):
        if(lt["exc"] == "gdax"):
            print("Loading GDAX data...")
            g.gdax_data(cur[e],lt["starttime"],thung.tm_mg(lt))
        elif(lt["exc"] == "btm"):
            print("Loading BitMex data...")
            btmp.bitmex_data(cur[e],lt["starttime"],thung.tm_mg(lt))
        elif(lt["exc"] == "polo"):
            print("Loading Poloniex data...")
            btmp.bitmex_data(cur[e],lt["starttime"],thung.tm_mg(lt))
        print("")
    
def collect_data():
    a = thung.data_work()
    rocket(a)
    print("Data Collected!")

def chart():
    print("chart")

def statscall():
    print("_" * 80)
    print("Input any of the following keywords for stats work")
    print("<gen>        General statistics include mean, variance, standard deviation of an asset")
    print("<corr>       Correlation between two assets")
    print("<rollvol>    Creates a csv with rolling correlation of two assets")
    print("<hrat>       Hedge Ratio between two assets")
    print("<rollhr>     Rolling Hedge Ratio between two assets")
    print("_" * 80)
    kas = input("Type of work: ")
    statDict = {"bye":inti,"gen":pretty.gen,"corr":pretty.corr,"rollvol":pretty.rollvol,"hrat":pretty.hrat,"rollhr":pretty.rollhr}
    while True:
        try:
            statDict[kas]()
            kas = input("Type of work: ")
        except:
            print("Not supported or bad input!")
            kas = input("Type of work: ")            
    
def title():
    print("="  * 80)
    print("Cetistat v.0.1")
    print("-"  * 80)
    inti()

def inti():
    print("Input any of the following keyword for data work")
    print("<data>: Collect Data from an exchange")
    print("<chart>: Create a chart based on given data")
    print("<stats>: Creates statistical outputs")
    print("<exit> : Exit Cetistat")
    print("="  * 80)
    funcDict = {"data": collect_data ,"chart": chart, "stats": statscall}
    ask = input("Enter Command: ")
    while True:
        if ask == "exit":
            quit()
        try:
            funcDict[ask]()
            ask = input("Enter Command: ")
        except:
            print("Command not available")
            ask = input("Enter Command: ")
            
        
title()
