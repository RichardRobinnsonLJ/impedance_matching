import math
def lml():
    rs=int(input("Enter the Source Resistance:"))
    rl=int(input("Enter the Load Resistance:"))
    freq=int(input("Enter the Frequency:"))
    if(rl>rs):
        xs= math.sqrt(((rl*rs)-(rs*rs)))
        l=(xs)/(2*math.pi*freq)
        xp=(rs*rl)/(xs)
        c=1/(2*math.pi*freq*xp)
        print("Connect",l,"H in Series to source resistor & Capacitor",c,"F in parallel to the load for LPF")
    else:
        xs= math.sqrt(((rl*rs)-(rl*rl)))
        l=(xs)/(2*math.pi*freq)
        xp=(rs*rl)/(xs)
        c=1/(2*math.pi*freq*xp)
        print("Connect",c,"F in Parallel to source resistor & Inductor",L,"H in parallel to the load LPF")

def lmh():
    rs=int(input("Enter the Source Resistance:"))
    rl=int(input("Enter the Load Resistance:"))
    freq=int(input("Enter the Frequency:"))
    if(rl>rs):
        xs= math.sqrt(((rl*rs)-(rs*rs)))
        c=1/(2*math.pi*freq*xs)
        xp=(rs*rl)/(xs)
        l=(xp)/(2*math.pi*freq)
        print(xs,xp)
        print("Connect",c,"F in Series to source resistor & Indcutor",l,"H in parallel to the load for HPF")
    else:
        xs= math.sqrt(((rl*rs)-(rl*rl)))
        c=1/(2*math.pi*freq*xs)
        xp=(rs*rl)/(xs)
        l=(xp)/(2*math.pi*freq)
        print("Connect",c,"F in Series to Load resistor & Inductor",L,"H in parallel to the Source HPF")
