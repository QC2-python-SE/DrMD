import numpy as np

class QubitState:
    """
    A class representing a two-qubit state.

    This class holds the information about a particular quantum state. Once
    a user has initialised a qubitstate object, it can be applied to 
    unitary operations or measurements.

    Attributes:
        __qb_matrix (numpy.ndarray): the matrix representation of the
        current two-qubit state. Private variable to make it immutable
        outside of the class.
        __qb_init (numpy.ndarray): the matrix representation of the
        original two-qubit state. Private variable to make it immutable
        outside of the class.
    """

    # Constructor for qubit state input matrices
    def __init__(self, matrix1, matrix2 = None):  
        """
        Initialises the QubitState object, ensuring all requirements
        of a valid quantum state are met. Constructs the two-qubit 
        state from two single-qubit states, if necessary.

        Args:
            matrix1 (list): Matrix representation for the qubit state, or
            only first qubit state.
            matrix2 (list): A 2x1 matrix representation for the
            second qubit state, if necessary.
        
        Raises:
            TypeError: Checks if 'matrix' parameters are a list, tuple or 
            numpy array.
            ValueError: Checks if 'matrix1' parameter is correct size.
            ValueError: Checks if 'matrix2' parameter is correct size.
        """
        # Checks if there was a single two-qubit state input or two
        # single-qubit inputs
        if matrix2 == None:
            matrix = matrix1

            # Type check for matrix
            if not isinstance(matrix, (tuple, list, np.ndarray)):  
                raise TypeError("The qubit state matrix must be a tuple, "\
                                "list or NumPy array.")
            
            # Convert list or tuple to np array
            if isinstance(matrix, (list, tuple)):
                matrix = np.array(matrix)
            
            # Check dimensions of matrix parameter
            if matrix.ndim != 1 or matrix.shape != (4,):
                raise ValueError("The qubit state matrix should be a 4x1 matrix.")
        
        else:
            # Type check for matrices
            if not isinstance(matrix1, (tuple, list, np.ndarray)):  
                raise TypeError("The first qubit state matrix must be a "\
                                "tuple, list or NumPy array.")

            if not isinstance(matrix2, (tuple, list, np.ndarray)):  
                raise TypeError("The second qubit state matrix must be a "\
                                "tuple, list or NumPy array.")
            
            # Convert list or tuple to np array
            if isinstance(matrix1, (list, tuple)):
                matrix1 = np.array(matrix1)

            if isinstance(matrix2, (list, tuple)):
                matrix2 = np.array(matrix2)
            
            # Check dimensions of matrix parameters
            if matrix1.ndim != 1 or matrix1.shape != (2,):
                raise ValueError("The first qubit state matrix should be "\
                                 "a 2x1 matrix.")
            
            if matrix2.ndim != 1 or matrix2.shape != (2,):
                raise ValueError("The second qubit state matrix should be "\
                                 "a 2x1 matrix.")
        
            # Combine the two single-qubit states
            matrix = np.kron(matrix1, matrix2)

        self.__qb_init = matrix  # storing initial state in private variable

        # Check normalisation
        total_sum = np.sum(matrix)
        if not np.isclose(total_sum, 1.0, atol=1e-7):  # tolerance for floating-point errors
            matrix = matrix/total_sum  # renormalise
        
        self.__qb_matrix = matrix

    def get_initial(self):
        """
        Function to give the qubit state used to initialise this
        QubitState object. Returns a copy of the array to ensure no
        unwanted mutability.
        
        Returns:
            numpy.ndarray: The initial qubit state.
        """
        return np.copy(self.__qb_init)
    
    def peek(self):
        """
        Function to show the current qubit state probabilities in the
        computational basis. Returns a copy of the array to ensure no
        unwanted mutability.

        Returns:
            numpy.ndarray: 4x1 matrix of current qubit state.
        """
        return np.copy(self.__qb_matrix)

    def copy(self):
        """
        Creates and returns a copy of the current qubit
        state as a QubitState object.

        Returns:
            QubitState: copy of current state object.
        """
        temp_qs = QubitState(np.copy(self.__qb_matrix))
        return temp_qs

    def __repr__(self):
        """
        Function to override the default 'print()' behaviour in python.
        Calling 'print()' on a QubitState object, returns the current
        qubit state matrix.

        Returns:
            str: 4x1 matrix of current qubit state.
        """
        return str(self.peek())
    
    def measure(self, to_measure = 12):
        """
        A measurement of the qubit state in the computational basis.

        Args:
            to_measure (int): Which qubit to measure or whether to
            measure the two-qubit state.
        
        Returns:
            str: The z-basis state as a result of the measurement.
        """

        return_state = None
        match to_measure:
            case 1:
                return_state = str(np.random.choice(("|0>","|1>"),p=np.array([
                    self.__qb_matrix[0] + self.__qb_matrix[1], self.__qb_matrix[2]
                      + self.__qb_matrix[3]])))
            case 2:
                return_state = str(np.random.choice(("|0>","|1>"),p=np.array([
                    self.__qb_matrix[0] + self.__qb_matrix[2], self.__qb_matrix[1]
                      + self.__qb_matrix[3]])))
            case 12:
                return_state = str(np.random.choice(("|00>","|01>",
                                                     "|10>","|11>"),
                                                     p=self.__qb_matrix))
            case _:
                raise ValueError("The qubit to be measured must be"\
                                  "indicated as an integer. Either 1,2"\
                                    " or 12 (both)")
        
        return return_state

    

    


    

