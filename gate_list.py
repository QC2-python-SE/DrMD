"""
A file consisting of commonly found qubit gates.

The gates are initialised objects of the 'UnitaryGate' class from the
'unitary_gate.py' file, which the user can easily call upon.
"""

# imports
import numpy as np
import unitary_gate


# common gate matrices

# e.g.   X_matrix = np.array(blah)

# Pauli matrices
I_mat = np.array([[1, 0], [0, 1]])
X_mat = np.array([[0, 1], [1, 0]])
Y_mat = np.array([[0, -1j], [1j, 0]])
Z_mat = np.array([[1, 0], [0, -1]])

# Hadamard gate
H_mat = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])

# CNOT gate
CNOT_mat = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

# define gates
x1 = unitary_gate.UnitaryGate(np.kron(X_mat,I_mat))
x2 = unitary_gate.UnitaryGate(np.kron(I_mat,X_mat))
y1 = unitary_gate.UnitaryGate(np.kron(Y_mat,I_mat))
y2 = unitary_gate.UnitaryGate(np.kron(I_mat,Y_mat))
z1 = unitary_gate.UnitaryGate(np.kron(Z_mat,I_mat))
z2 = unitary_gate.UnitaryGate(np.kron(I_mat,Z_mat))

hadamard1 = unitary_gate.UnitaryGate(np.kron(H_mat,I_mat))
hadamard2 = unitary_gate.UnitaryGate(np.kron(I_mat,H_mat))

cnot = unitary_gate.UnitaryGate(CNOT_mat)

# e.g. X = UnitaryGate(X_matrix)
