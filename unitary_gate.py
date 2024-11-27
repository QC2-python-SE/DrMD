import numpy as np

class UnitaryGate:
    """
    A class representing a unitary quantum gate.

    This class holds to basic attributes for a gate to be implemented in 
    quantum computing protocols. This includes methods to find the affect
    of applying these unitaries to arbitrary quantum states.

    Attributes:
        matrix_rep (numpy.ndarray): the matrix representation of the unitary gate.
        
    """

    def __init__(self, matrix1, matrix2 = None):  
        """
        Initialises the UnitaryGate object, taking in the matrix representation.
        Ensures all requirements of a valid unitary gate are met. Constructs the
        two-qubit unitary gate from two single-qubit unitary gates, if necessary.

        Args:
            matrix1 (list): Matrix representation for the unitary gate, or
            only first unitary gate.
            matrix2 (list): A 2x2 matrix representation for the second
            unitary gate, if necessary.
        
        Raises:
            TypeError: Checks if 'matrix' parameters are a list, tuple or 
            numpy array.
            ValueError: Checks if 'matrix1' parameter is correct size.
            ValueError: Checks if 'matrix2' parameter is correct size.
        """
        # Checks if there was a single two-qubit unitary gate input or two
        # single-qubit inputs
        if matrix2 == None:
            matrix = matrix1

            # Type check for matrix
            if not isinstance(matrix, (tuple, list, np.ndarray)):  
                raise TypeError("The unitary gate matrix must be a tuple, "\
                                "list or NumPy array.")
            
            # Convert list or tuple to np matrix
            if isinstance(matrix, (list, tuple)):
                matrix = np.matrix(matrix)
            
            # Check dimensions of matrix parameter
            if matrix.shape != (4,4):
                raise ValueError("The unitary gate matrix should be a 4x4 matrix.")
        
        else:
            # Type check for matrices
            if not isinstance(matrix1, (tuple, list, np.ndarray)):  
                raise TypeError("The first unitary gate matrix must be a "\
                                "tuple, list or NumPy array.")

            if not isinstance(matrix2, (tuple, list, np.ndarray)):  
                raise TypeError("The second unitary gate matrix must be a "\
                                "tuple, list or NumPy array.")
            
            # Convert list or tuple to np matrix
            if isinstance(matrix1, (list, tuple)):
                matrix1 = np.matrix(matrix1)

            if isinstance(matrix2, (list, tuple)):
                matrix2 = np.matrix(matrix2)
            
            # Check dimensions of matrix parameters
            if  matrix1.shape != (2, 2):
                raise ValueError("The first unitary gate matrix should be "\
                                 "a 2x2 matrix.")
            
            if  matrix2.shape != (2, 2):
                raise ValueError("The second unitary gate matrix should be "\
                                 "a 2x2 matrix.")
        
            # Combine the two single-qubit unitary gates
            matrix = np.kron(matrix1, matrix2)


        # Check if the input is unitary
        I_mat = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        l = matrix@matrix.getH() == I_mat
        if not l.all():
            raise ValueError("The unitary gate matrix should be unitary.")
        
        # CHECKKKKKK!!!!
        self.matrix = np.matrix.copy(matrix) 
        


    def apply(self, state):
        """
        Applies a unitary gate to a state. 

        Args:
            state (list): Matrix representation for a 2-qubit state.

        Returns:
            numpy.ndarray: The final state.
        
        Raises:
            TODO: insert error handling
        """

        return self.matrix @ state
    # could add other functions here that output the representation? idk


# print(isinstance("Hello", (float, int, str, list, dict, tuple)))
# m = np.matrix([[0,1], [1j, 0]])
# print(m.getH())
# I_mat = np.array([[1, 0], [0,1]])
# print(m@m.getH())
# l = m@m.getH() == I_mat
# print(l.all())

u = UnitaryGate([[0,1], [-1j, 0]], [[1,0], [0,1]])

