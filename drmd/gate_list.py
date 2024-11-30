'''
A file consisting of commonly found qubit gates.

The gates are initialised objects of the 'UnitaryGate' class from the
'unitary_gate.py' file, which the user can easily call upon.

One qubit gates that define the identity matrix and Pauli matrices are
defined using numpy arrays.

One qubit gates that define the identity matrix, Pauli and Hadamard 
matrices are defined using numpy arrays. The CNOT gate is also
explicitly defined, where cnot1 describes a control on qubit 1 and a NOT gate
qubit on 2 and cnot2 describes a control on qubit 2 and a NOT gate on qubit 1.

'''

import numpy as np
import drmd.unitary_gate as unitary_gate

# Common gate matrices

# Pauli matrices
I_mat = np.array([[1, 0], [0, 1]])
X_mat = np.array([[0, 1], [1, 0]])
Y_mat = np.array([[0, -1j], [1j, 0]])
Z_mat = np.array([[1, 0], [0, -1]])

# Hadamard gate
H_mat = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])

# Define gates
X1 = unitary_gate.UnitaryGate(np.kron(X_mat,I_mat))
X2 = unitary_gate.UnitaryGate(np.kron(I_mat,X_mat))
Y1 = unitary_gate.UnitaryGate(np.kron(Y_mat,I_mat))
Y2 = unitary_gate.UnitaryGate(np.kron(I_mat,Y_mat))
Z1 = unitary_gate.UnitaryGate(np.kron(Z_mat,I_mat))
Z2 = unitary_gate.UnitaryGate(np.kron(I_mat,Z_mat))

HADAMARD1 = unitary_gate.UnitaryGate(np.kron(H_mat,I_mat))
HADAMARD2 = unitary_gate.UnitaryGate(np.kron(I_mat,H_mat))

# CNOT gate
C1NOT2 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
C2NOT1 = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])

CNOT1 = unitary_gate.UnitaryGate(C1NOT2)
CNOT2 = unitary_gate.UnitaryGate(C2NOT1)


# Function to list all UnitaryGate objects
def list_unitary_gates():
    # Use globals() to get all global variables
    all_vars = globals()
    # Filter for instances of UnitaryGate
    unitary_gate_names = [name for name, var in all_vars.items() if isinstance(var, unitary_gate.UnitaryGate)]

    return unitary_gate_names
