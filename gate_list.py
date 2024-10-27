"""
A file consisting of commonly found qubit gates.

The gates are initialised objects of the 'UnitaryGate' class from the
'unitary_gate.py' file, which the user can easily call upon.
"""

# imports
import numpy as np


# common gate matrices

# e.g.   X_matrix = np.array(blah)

# Pauli matrices
I_mat = np.array([[1, 0], [0, 1]])
X_mat = np.array([[0, 1], [1, 0]])
Y_mat = np.array([[0, -1j], [1j, 0]])
Z_mat = np.array([[1, 0], [0, -1]])

# Hadamard gate
H_mat = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])

# define gates

# e.g. X = UnitaryGate(X_matrix)
