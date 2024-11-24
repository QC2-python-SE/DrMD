import pytest
import numpy as np

import qubit_state as qs
"""
A testing python file using the pytest framework for the QubitState class.

Tests the construction of a QubitState object for both a two-qubit state
matrix and two single-qubit state matrices.
Tests appropriate behaviour of all functions and functionality.
Tests the error handling within the constructor.
"""
def test_onequbit():
    """
    Function to test the construction of QubitState object for the input
    of a single two-qubit initial qubit state.
    """
    # Test conversion to numpy array for tuple and list
    qubit_init = [0.5,0.5,0,0]  # list
    q_state = qs.QubitState(qubit_init)
    assert np.allclose(q_state.peek(), np.array([0.5,0.5,0,0])) == True

    qubit_init = (0.5,0.5,0,0)  # tuple
    q_state = qs.QubitState(qubit_init)
    assert np.allclose(q_state.peek(), np.array([0.5,0.5,0,0])) == True

    # Test normalisation
    qubit_init = [1,1,0,0]
    q_state = qs.QubitState(qubit_init)
    assert np.allclose(q_state.peek(), np.array([0.5,0.5,0,0])) == True

    # Test initial state save
    assert np.allclose(q_state.get_initial(), np.array([1,1,0,0])) == True

    # Test wrong input type
    with pytest.raises(TypeError, match = "The qubit state matrix must be "\
                       "a tuple, list or NumPy array."):
        qs.QubitState("error-worthy.")

    # Test wrong two-qubit matrix input size
    with pytest.raises(ValueError, match = "The qubit state matrix should be "\
                       "a 4x1 matrix."):
        qs.QubitState([0,0,0])

def test_twoqubit():
    """
    Function to test the construction of QubitState object for the input
    of a two single-qubit initial qubit states.
    """
    # Test conversion to numpy array for tuple and list and normalisation
    qubit_init_1 = [1,1]  # list
    qubit_init_2 = [1,0]
    q_state = qs.QubitState(qubit_init_1, qubit_init_2)
    assert np.allclose(q_state.peek(), np.array([0.5,0,0.5,0])) == True

    qubit_init_1 = (1,1)  # tuple
    qubit_init_2 = (1,0)
    q_state = qs.QubitState(qubit_init_1, qubit_init_2)
    assert np.allclose(q_state.peek(), np.array([0.5,0,0.5,0])) == True

    # Test initial state save
    assert np.allclose(q_state.get_initial(), np.array([1,0,1,0])) == True

    # Test wrong input type for both inputs
    with pytest.raises(TypeError, match = "The first qubit state matrix "\
                       "must be a tuple, list or NumPy array."):
        qs.QubitState("error.",(1,0))

    with pytest.raises(TypeError, match = "The second qubit state matrix "\
                       "must be a tuple, list or NumPy array."):
        qs.QubitState((1,0),"worthy.")

    # Test wrong first qubit matrix input size
    with pytest.raises(ValueError, match = "The first qubit state matrix should be "\
                       "a 2x1 matrix."):
        qs.QubitState([0,0,0], (1,0))
    
    # Test wrong second qubit matrix input size
    with pytest.raises(ValueError, match = "The second qubit state matrix should be "\
                       "a 2x1 matrix."):
        qs.QubitState((1,0), [0,0,0])