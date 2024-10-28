class UnitaryGate:
    """
    A class representing a unitary quantum gate.

    This class holds to basic attributes for a gate to be implemented in 
    quantum computing protocols. This includes methods to find the affect
    of applying these unitaries to arbitrary quantum states.

    Attributes:
        matrix_rep (numpy.ndarray): the matrix representation of the unitary gate.
        n_qubits (int): the number of qubits involved in the gate operation.
    """

    def __init__(self, matrix):  # constructor
        """
        Initialises the UnitaryGate object, taking in the matrix representation.

        TODO: fill out rest ..
        """
        self.matrix = matrix
        #TODO: FILL IN


    def apply(self, state):
        #TODO: fill in
        return self.matrix @ state
    # could add other functions here that output the representation? idk

