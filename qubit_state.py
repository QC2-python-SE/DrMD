import numpy as np

class QubitState:
    """
    A class representing a two-qubit state.

    This class holds the information about a particular quantum state. Once
    a user has initialised a qubitstate object, it can be applied to 
    unitary operations or measurements.

    Attributes:
        qb_matrix (numpy.ndarray): the matrix representation of the
        current two-qubit state
        qb_init (numpy.ndarray): the matrix representation of the
        original two-qubit state
    """
    # Constructor for one two-qubit input matrix
    def __init__(self, matrix):
        """
        Initialises the QubitState object, ensuring all requirements
        of a valid quantum state are met.

        Args:
            matrix (list): A 4x1 matrix representation of a 
            two-qubit state.
        
        Raises:
            TypeError: Checks if 'matrix' parameter is a list, tuple or 
            numpy array.
            ValueError: Checks if 'matrix' parameter is a 4x1 matrix.
        """
        # Type check for matrix
        if not isinstance(matrix, (tuple, list, np.ndarray)):  
            raise TypeError("The qubit state matrix must be a tuple, list or NumPy array.")
        
        # Convert list or tuple to np array
        if isinstance(matrix, (list, tuple)):
            matrix = np.array(matrix)
        
        # Check dimensions of matrix parameter
        if matrix.ndim != 1 or matrix.shape != (4,):
            raise ValueError("The qubit state matrix should be a 4x1 matrix.")
        
        # Check normalisation
        total_sum = np.sum(matrix)
        if not np.isclose(total_sum, 1.0, atol=1e-7):  # tolerance for floating-point errors
            matrix = matrix/total_sum  # renormalise
        
        self.qb_matrix = matrix

    # Constructor for two one-qubit input matrices
    def __init__(self, matrix1, matrix2):  
        """
        Initialises the QubitState object, ensuring all requirements
        of a valid quantum state are met. Constructs the two-qubit 
        state from two single-qubit states.

        Args:
            matrix1 (list): A 2x1 matrix representation for the
            first qubit state.
            matrix2 (list): A 2x1 matrix representation for the
            second qubit state.
        
        Raises:
            TypeError: Checks if 'matrix' parameters are a list, tuple or 
            numpy array.
            ValueError: Checks if 'matrix1' parameter is a  2x1 matrix.
            ValueError: Checks if 'matrix2' parameter is a  2x1 matrix.
        """
        
        # Type check for matrices
        if not isinstance((matrix1, matrix2), (tuple, list, np.ndarray)):  
            raise TypeError("The qubit state matrices must be tuples, lists or NumPy arrays.")
        
        # Convert list or tuple to np array
        if isinstance(matrix1, (list, tuple)):
            matrix1 = np.array(matrix1)

        if isinstance(matrix2, (list, tuple)):
            matrix2 = np.array(matrix2)
        
        # Check dimensions of matrix parameters
        if matrix1.ndim != 1 or matrix1.shape != (2,):
            raise ValueError("The first qubit state matrix should be a 2x1 matrix.")
        
        if matrix2.ndim != 1 or matrix2.shape != (2,):
            raise ValueError("The second qubit state matrix should be a 2x1 matrix.")
        
        # Combine the two single-qubit states
        complete_state = np.kron(matrix1, matrix2)

        # Check normalisation
        total_sum = np.sum(complete_state)
        if not np.isclose(total_sum, 1.0, atol=1e-7):  # tolerance for floating-point errors
            complete_state= complete_state/total_sum  # renormalise
        
        self.qb_matrix = complete_state

