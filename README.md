# L-Matching Network Impedance Matching Calculator

This Python script calculates the component values for an L-matching network to match a given load impedance to a source impedance. The L-matching network consists of either a series and parallel inductor or capacitor, designed to maximize power transfer between the source and load.

## Features
- Calculates series and shunt component values (inductor or capacitor) for impedance matching.
- Supports both high-to-low and low-to-high impedance matching scenarios.
- Customizable input parameters for load and source impedance and frequency.

## Formula Used
The script uses standard L-network matching equations:
- Quality factor (Q):
  - If \( R_{load} > R_{source} \): \( Q = \sqrt{\frac{R_{load}}{R_{source}} - 1} \)
  - If \( R_{load} < R_{source} \): \( Q = \sqrt{\frac{R_{source}}{R_{load}} - 1} \)
- Series Reactance: \( X_{series} = R \times Q \)
- Shunt Reactance: \( X_{shunt} = \frac{R}{Q} \)
- Inductor: \( L = \frac{X}{2\pi f} \)
- Capacitor: \( C = \frac{1}{2\pi f X} \)

## Usage
1. Install Python (version 3.x recommended).
2. Run the script using any Python IDE or from the command line:
   ```bash
   python l_match_network.py
   ```
3. Customize the input parameters in the script:
   ```python
   R_load = 100  # Load resistance in ohms
   X_load = 0    # Load reactance in ohms
   R_source = 50 # Source resistance in ohms
   freq = 1e6    # Frequency in Hz (1 MHz)
   ```
4. The script will output the calculated component values:
   ```
   Series Inductor (H): 7.071068e-06
   Shunt Capacitor (F): 2.253934e-09
   ```

## Example Output
For matching a 100 Ω load to a 50 Ω source at 1 MHz:
```
Series Inductor (H): 7.071068e-06
Shunt Capacitor (F): 2.253934e-09
```

## License
This project is open-source and free to use under the MIT License.

## Contributions
Contributions, issues, and feature requests are welcome!

## Author
Developed by Richard Robinnson L J

