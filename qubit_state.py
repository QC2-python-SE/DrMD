import numpy as np
np.set_printoptions(legacy='1.25')  # For more intuitive float print messages

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
            
            # Type check for each element in the input states
            if not all(isinstance(item, (int, float)) for row in matrix for item in row):
                raise TypeError("All elements of the input state must be either int or float.")

            
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
            
            # Type check for each element in the input states
            if not all(isinstance(item, (int, float)) for row in matrix1 for item in row):
                raise TypeError("All elements of the input state must be either int or float.")
            
            if not all(isinstance(item, (int, float)) for row in matrix2 for item in row):
                raise TypeError("All elements of the input state must be either int or float.")
            
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
        total_sum = np.sum(np.conjugate(matrix)*matrix)

        # Check for null state
        if total_sum == 0:
            raise ValueError("The qubit state must have some non-zero entries.")
        
        if not np.isclose(total_sum, 1.0, atol=1e-7):  # tolerance for floating-point errors
            matrix = matrix/np.sqrt(total_sum)  # renormalise
        
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
        return str(np.round(self.peek(),4))  # Rounded for clarity
    
    def measureStats(self, to_measure = 12):
        """
        A description of the statistics for a  measurement of the qubit
        state in the computational basis.

        Args:
            to_measure (int): Which qubit to measure or whether to
            measure the two-qubit state.
        
        Returns:
            list: The qubit states as a result of the measurement along
            with the associated probabilities.
        """
        # List to hold states and probabilities
        stats = []

        # Pre-compute the probabilties for each possible basis state.
        prob = np.round(np.conjugate(self.__qb_matrix)*self.__qb_matrix,4)

        # Check which qubit states to 'measure'
        match to_measure:
            # Measure state 1
            case 1:
                prob_0 = prob[0] + prob[1]
                prob_1 = prob[2] + prob[3]

                # Only add non-zero states
                if not prob_0 == 0:
                    stats.append((QubitState(np.array([self.__qb_matrix[0],
                                                        self.__qb_matrix[1], 0, 0])), prob_0))
                
                if not prob_1 == 0:
                    stats.append((QubitState(np.array([0, 0, self.__qb_matrix[2],
                                                        self.__qb_matrix[3]])), prob_1))

            # Measure state 2
            case 2:
                prob_0 = prob[0] + prob[2]
                prob_1 = prob[1] + prob[3]

                # Only add non-zero states
                if not prob_0 == 0:
                    stats.append((QubitState(np.array([self.__qb_matrix[0], 0,
                                                        self.__qb_matrix[2], 0])), prob_0))
                
                if not prob_1 == 0:
                    stats.append((QubitState(np.array([0, self.__qb_matrix[1], 0,
                                                        self.__qb_matrix[3]])), prob_1))
                

            # Measure both states
            case 12:
                # Only add non-zero states
                if not prob[0] == 0:
                    stats.append((QubitState(np.array([1,0,0,0])), prob[0]))
                
                if not prob[1] == 0:
                    stats.append((QubitState(np.array([0,1,0,0])), prob[1]))
                
                if not prob[2] == 0:
                    stats.append((QubitState(np.array([0,0,1,0])), prob[2]))
                
                if not prob[3] == 0:
                    stats.append((QubitState(np.array([0,0,0,1])), prob[3]))

            # Handle any other user input    
            case _:
                raise ValueError("The qubit to be measured must be"\
                                  "indicated as an integer. Either 1,2"\
                                    " or 12 (both)")
        
        return stats
    
    def measureCollapse(self, to_measure = 12):
        """
        A measurement of the qubit state in the computational basis.
        Collapses the current qubit state to one of the z-basis states.

        Args:
            to_measure (int): Which qubit to measure or whether to
            measure the two-qubit state.
        
        Returns:
            QubitState: The qubit state as a result of the measurement.
        """
        stats = self.measureStats(to_measure)

        # Extract QubitStates and probabilties from stats list
        states, probs = zip(*stats)

        # Randomly choose measurement state based on z-basis probabilities
        self.__qb_matrix = np.random.choice(states, p=probs).peek()

        # Return a QubitState object
        return self.copy()
    

    


    

