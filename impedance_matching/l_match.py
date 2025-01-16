import cmath
import math

def l_match_network(R_load, X_load, R_source, freq):
    omega = 2 * math.pi * freq
    
    if R_load > R_source:
        Q = math.sqrt((R_load / R_source) - 1)
        X_series = R_source * Q
        X_shunt = R_load / Q
    else:
        Q = math.sqrt((R_source / R_load) - 1)
        X_series = R_load * Q
        X_shunt = R_source / Q
    
    # Series reactance component
    if X_series > 0:
        L_series = X_series / omega
        C_series = None
    else:
        C_series = -1 / (omega * X_series)
        L_series = None
    
    # Shunt reactance component
    if X_shunt > 0:
        L_shunt = X_shunt / omega
        C_shunt = None
    else:
        C_shunt = -1 / (omega * X_shunt)
        L_shunt = None
    
    return {
        'Series Inductor (H)': L_series,
        'Series Capacitor (F)': C_series,
        'Shunt Inductor (H)': L_shunt,
        'Shunt Capacitor (F)': C_shunt
    }

# Example parameters
R_load = 100  # Load resistance in ohms
X_load = 0    # Load reactance in ohms
R_source = 50 # Source resistance in ohms
freq = 1e6    # Frequency in Hz (1 MHz)

components = l_match_network(R_load, X_load, R_source, freq)

for component, value in components.items():
    if value:
        print(f"{component}: {value:.6e}")
