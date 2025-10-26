from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import numpy as np
import math

# ==================================================
# --- CONFIGURAÇÃO DOS SIMULADORES ---
# ==================================================
S_simulator = AerSimulator(method='statevector')
M_simulator = AerSimulator()

# ==================================================
# --- FUNÇÃO: Wavefunction ---
# ==================================================
def Wavefunction(obj, precision=5, column=False, systems=None, show_systems=None):
    """
    Exibe o vetor de estado (função de onda) de um circuito quântico ou array numpy.

    Args:
        obj: QuantumCircuit ou np.ndarray representando o statevector.
        precision: número de casas decimais.
        column: se True, exibe cada estado em linha separada.
        systems: lista de inteiros separando grupos de qubits (opcional).
        show_systems: lista de bools indicando quais sistemas mostrar (opcional).
    """
    # --- Obtém o statevector ---
    if isinstance(obj, QuantumCircuit):
        statevec = Statevector.from_instruction(obj)
    elif isinstance(obj, np.ndarray):
        statevec = obj
    else:
        raise TypeError("Objeto deve ser QuantumCircuit ou np.ndarray.")

    wavefunction = ""
    dec = precision
    qubits = int(math.log2(len(statevec)))

    # --- Gera representação binária de cada estado ---
    for i, amp in enumerate(statevec):
        amp_real = round(amp.real, dec)
        amp_imag = round(amp.imag, dec)
        if amp_real != 0 or amp_imag != 0:
            bin_state = format(i, f"0{qubits}b")
            # Constrói a string da amplitude
            amp_str = ""
            if amp_real != 0:
                amp_str += f"{amp_real}"
            if amp_imag != 0:
                amp_str += f"{'+' if amp_imag > 0 and amp_real != 0 else ''}{amp_imag}j"
            # Monta linha da função de onda
            wavefunction += f"{amp_str} |{bin_state}⟩"
            wavefunction += "\n" if column else "  "

    print(wavefunction)