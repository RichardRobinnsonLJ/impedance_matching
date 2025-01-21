import math

def pml():
    rs = int(input("Enter the Source Resistance: "))
    rl = int(input("Enter the Load Resistance: "))
    freq = int(input("Enter the Frequency: "))

    if rl > rs:
        xs1 = math.sqrt((rl * rs) - (rs * rs))
        xs2 = math.sqrt((rl * rs) - (rs * rs))
        c1 = 1 / (2 * math.pi * freq * xs1)
        l = xs2 / (2 * math.pi * freq)
        c2 = 1 / (2 * math.pi * freq * xs2)
        print("Connect Capacitor", c1, "F in parallel with source.")
        print("Connect Inductor", l, "H in series between source and load.")
        print("Connect Capacitor", c2, "F in parallel with load.")
    else:
        xs1 = math.sqrt((rl * rs) - (rl * rl))
        xs2 = math.sqrt((rl * rs) - (rl * rl))
        c1 = 1 / (2 * math.pi * freq * xs1)
        l = xs2 / (2 * math.pi * freq)
        c2 = 1 / (2 * math.pi * freq * xs2)
        print("Connect Capacitor", c1, "F in parallel with source.")
        print("Connect Inductor", l, "H in series between source and load.")
        print("Connect Capacitor", c2, "F in parallel with load.")

def pmh():
    rs = int(input("Enter the Source Resistance: "))
    rl = int(input("Enter the Load Resistance: "))
    freq = int(input("Enter the Frequency: "))

    if rl > rs:
        xs1 = math.sqrt((rl * rs) - (rs * rs))
        xs2 = math.sqrt((rl * rs) - (rs * rs))
        l1 = xs1 / (2 * math.pi * freq)
        c = 1 / (2 * math.pi * freq * xs2)
        l2 = xs2 / (2 * math.pi * freq)
        print("Connect Inductor", l1, "H in parallel with source.")
        print("Connect Capacitor", c, "F in series between source and load.")
        print("Connect Inductor", l2, "H in parallel with load.")
    else:
        xs1 = math.sqrt((rl * rs) - (rl * rl))
        xs2 = math.sqrt((rl * rs) - (rl * rl))
        l1 = xs1 / (2 * math.pi * freq)
        c = 1 / (2 * math.pi * freq * xs2)
        l2 = xs2 / (2 * math.pi * freq)
        print("Connect Inductor", l1, "H in parallel with source.")
        print("Connect Capacitor", c, "F in series between source and load.")
        print("Connect Inductor", l2, "H in parallel with load.")
