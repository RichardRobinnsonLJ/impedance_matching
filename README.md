# Matching Network Design

This repository contains Python scripts for designing impedance matching networks, including **L-matching**, **T-matching**, and **Π-matching** networks. The tool supports both Low Pass Filter (LPF) and High Pass Filter (HPF) configurations for each topology.

## Files in the Repository

1. **`matching.py`**
   - Main module to execute the program.
   - Provides an interface to choose between LPF and HPF configurations.
   - Supports three topologies: L-matching, T-matching, and Π-matching.

2. **`l_match.py`**
   - Contains functions for designing L-matching networks for LPF (`lml`) and HPF (`lmh`).

3. **`t_match.py`**
   - Contains functions for designing T-matching networks for LPF (`tml`) and HPF (`tmh`).

4. **`pi_match.py`**
   - Contains functions for designing Π-matching networks for LPF (`pml`) and HPF (`pmh`).

## How to Use

1. Clone the repository and navigate to the directory.
   ```bash
   git clone https://github.com/RichardRobinnsonLJ/impedance_matching.git
   cd <repository-directory>
   ```

2. Run the main module:
   ```bash
   python matching.py
   ```

3. Follow the prompts to select the desired configuration:
   - **Choose Filter Type:**
     - `1` for Low Pass Filter (LPF).
     - `2` for High Pass Filter (HPF).
   - **Choose Topology:**
     - `1` for L-Matching Network.
     - `2` for Π-Matching Network.
     - `3` for T-Matching Network.

4. Enter the required parameters when prompted:
   - **Source Resistance (Rs):** Resistance at the source side.
   - **Load Resistance (Rl):** Resistance at the load side.
   - **Frequency (Hz):** Operating frequency of the matching network.

5. The program calculates and displays the component values (inductors and capacitors) and provides guidance on how to connect them.

## Example Output

### Input:
```
Choose any one of the Following filter type
1.LPF
2.HPF
Enter Your option: 1
Choose one of the topology
1.L_Matching Network
2.Pi_Matching Network
3.T_Matching Network
Enter Your option: 2
Enter the Source Resistance: 50
Enter the Load Resistance: 200
Enter the Frequency: 1000000
```

### Output:
```
Connect Capacitor 1.5915494309189535e-10 F in parallel with source.
Connect Inductor 2.5464790894703256e-05 H in series between source and load.
Connect Capacitor 7.957747154594767e-11 F in parallel with load.
```

## Dependencies
- Python 3.x
- No additional libraries are required (uses only the standard math library).

## Features
- Supports L, T, and Π matching networks.
- Handles both Low Pass and High Pass filter designs.
- Dynamically calculates required inductance and capacitance values.

## Notes
- Ensure that the input values are realistic for your circuit application (e.g., resistance and frequency).
- The program assumes ideal components; parasitic effects are not considered.

## License
This project is licensed under the MIT License.

---

Developed for designing advanced impedance matching networks for RF and other electronic circuit applications.
