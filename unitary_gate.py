import numpy as np
from typing import TypeVar
from qubit_state import QubitState
from numpy import allclose

apply_type = TypeVar("state", np.ndarray, QubitState)

class UnitaryGate:
    """
    A class representing a unitary quantum gate.

    This class holds to basic attributes for a gate to be implemented in 
    quantum computing protocols. This includes methods to find the effect
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
        if type(matrix2) == type(None):
            uni_mat = matrix1

            # Type check for matrix
            if not isinstance(uni_mat, (tuple, list, np.ndarray)):  
                raise TypeError("The unitary gate matrix must be a tuple, "\
                                "list or NumPy array.")
            
            # Convert list or tuple to np matrix
            if isinstance(uni_mat, (list, tuple, np.ndarray)):
                uni_mat = np.matrix(uni_mat)
            
            # Check dimensions of matrix parameter
            if uni_mat.shape != (4,4):
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
            if isinstance(matrix1, (list, tuple, np.ndarray)):
                matrix1 = np.matrix(matrix1)

            if isinstance(matrix2, (list, tuple, np.ndarray)):
                matrix2 = np.matrix(matrix2)
            
            # Check dimensions of matrix parameters
            if  matrix1.shape != (2, 2):
                raise ValueError("The first unitary gate matrix should be "\
                                 "a 2x2 matrix.")
            
            if  matrix2.shape != (2, 2):
                raise ValueError("The second unitary gate matrix should be "\
                                 "a 2x2 matrix.")
        
            # Combine the two single-qubit unitary gates
            uni_mat = np.kron(matrix1, matrix2)


        # Check if the input is unitary
        I_mat = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        l =  uni_mat@uni_mat.getH()
        if not allclose(l, I_mat, atol = 1.e-5):
            raise ValueError("The unitary gate matrix should be unitary.")
        
        self._matrix = np.matrix.copy(uni_mat) 
        
    def apply(self, state: apply_type) -> apply_type:
        """
        Applies a unitary gate to a state. 

        Args:
            state (QubitState or numpy.ndarray): input state

        Returns:
            QubitState or numpy.ndarray: final state (same type as input)
        
        Raises:
            ValueError: if np.array state not of correct size
            TypeError: if input not QubitState or np.array
        """

        if type(state) == np.ndarray:
            if state.shape != (4,) or state.ndim != 1:
                raise ValueError("Wrong size of state. Input states need to be a 4x1 array.")
            
            return np.array(self._matrix @ state)[0]
        
        elif type(state) == QubitState:
            state_array = state.get_initial()
            state_array = np.array(self._matrix @ state_array)[0]
            return QubitState(state_array)
        
        else:
            raise TypeError("Input must be numpy.ndarray or QubitState.")


    def __repr__(self):
        """
        Overrides the default 'print()' behaviour in python.
        Returns the current unitary gate matrix.
        """
        return str(self._matrix)
    

    def dagger(self) -> 'UnitaryGate':
        """
        Returns the hermitian conjugate of the input matrix.

        Returns:
            UnitaryGate: the hermitian conjugate of the input.
        """
        return UnitaryGate(self._matrix.getH())
 

    def copy(self) -> 'UnitaryGate':
        """
        Returns pointer deep copy of self.
        """

        mat = self._matrix.copy()
        return UnitaryGate(mat)
    

    def compare(self, gate: 'UnitaryGate') -> bool:
        """
        Returns True if the two gates are the same.

        Args:
            gate (UnitaryGate): input unitary gate.

        Returns:
            Boolean: if the two gates are the same.
        """
        mat1 = gate._matrix
        mat2 = self._matrix
        return allclose(mat1, mat2, atol = 1.e-5)
        

  
