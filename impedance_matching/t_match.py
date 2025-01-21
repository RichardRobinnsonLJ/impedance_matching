import math
def tml():
    rs=int(input("Enter the Source Resistance:"))
    rl=int(input("Enter the Load Resistance:"))
    ro=rs+rl
    freq=int(input("Enter the Frequency:"))
    xs1= math.sqrt(((ro*rs)-(rs*rs)))
    xs2= math.sqrt(((ro*rl)-(rl*rl)))
    xp1=(rs*ro)/(xs1)
    xp2=(rl*ro)/(xs2)
    xp=(xp1*xp2)/(xp1+xp2)
    l1=(xs1)/(2*math.pi*freq)
    l2=(xs2)/(2*math.pi*freq)
    c=1/(2*math.pi*freq*xp)
    print("Connect",l1,"H in Series to source resistor &",l2," in series to Load and Capacitor",c,"F in parallel between them for LPF")

def tmh():
    rs=int(input("Enter the Source Resistance:"))
    rl=int(input("Enter the Load Resistance:"))
    ro=rs+rl
    freq=int(input("Enter the Frequency:"))
    xs1= math.sqrt(((ro*rs)-(rs*rs)))
    xs2= math.sqrt(((ro*rl)-(rl*rl)))
    xp1=(rs*ro)/(xs1)
    xp2=(rl*ro)/(xs2)
    xp=(xp1*xp2)/(xp1+xp2)
    c1=1/(2*math.pi*freq*xs1)
    c2=1/(2*math.pi*freq*xs2)
    l=(xp)/(2*math.pi*freq)
    print("Connect",c1,"F in Series to source resistor &",c2,"F in series to Load and Inductor",l,"H in parallel between them for LPF")


