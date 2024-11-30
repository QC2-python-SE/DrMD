import sys
import os

# Add the package's source directory to sys.path
sys.path.insert(0, os.path.abspath('../drmd'))

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
    assert np.allclose(q_state.peek(), np.sqrt(np.array([0.5,0.5,0,0])))

    qubit_init = (0.5,0.5,0,0)  # tuple
    q_state = qs.QubitState(qubit_init)
    assert np.allclose(q_state.peek(), np.sqrt(np.array([0.5,0.5,0,0])))

    # Test normalisation
    qubit_init = [1,1,0,0]
    q_state = qs.QubitState(qubit_init)
    assert np.allclose(q_state.peek(), np.sqrt(np.array([0.5,0.5,0,0])))

    # Test initial state save
    assert np.allclose(q_state.get_initial(), np.array([1,1,0,0]))

    # Test wrong input type
    with pytest.raises(TypeError, match = ("The qubit state matrix must be " +
                       "a tuple, list or NumPy array.")):
        qs.QubitState("error-worthy.")
    
    # Test wrong input element type
    with pytest.raises(TypeError, match = ("All elements of the input " +
                       "state must be either int or float.")):
        qs.QubitState(['a','b','c',0])

    # Test wrong two-qubit matrix input size
    with pytest.raises(ValueError, match = ("The qubit state matrix should " +
                       "be a 4x1 matrix.")):
        qs.QubitState([0,0,0])

    # Test an empty qubit state input
    with pytest.raises(ValueError, match = ("The qubit state must have " +
                                            "some non-zero entries.")):
        qs.QubitState([0,0,0,0])


def test_twoqubit():
    """
    Function to test the construction of QubitState object for the input
    of a two single-qubit initial qubit states.
    """
    # Test conversion to numpy array for tuple and list and normalisation
    qubit_init_1 = [1,1]  # list
    qubit_init_2 = [1,0]
    q_state = qs.QubitState(qubit_init_1, qubit_init_2)
    assert np.allclose(q_state.peek(), np.sqrt(np.array([0.5,0,0.5,0])))

    qubit_init_1 = (1,1)  # tuple
    qubit_init_2 = (1,0)
    q_state = qs.QubitState(qubit_init_1, qubit_init_2)
    assert np.allclose(q_state.peek(), np.sqrt(np.array([0.5,0,0.5,0])))

    # Test initial state save
    assert np.allclose(q_state.get_initial(), np.array([1,0,1,0]))

    # Test wrong input type for both inputs
    with pytest.raises(TypeError, match = ("The first qubit state matrix " +
                       "must be a tuple, list or NumPy array.")):
        qs.QubitState("error.",(1,0))

    with pytest.raises(TypeError, match = ("The second qubit state matrix " +
                       "must be a tuple, list or NumPy array.")):
        qs.QubitState((1,0),"worthy.")
    
    # Test wrong input element type
    with pytest.raises(TypeError, match = ("All elements of the input " +
                       "state must be either int or float.")):
        qs.QubitState(['a','b'],[1,0])

    with pytest.raises(TypeError, match = ("All elements of the input " +
                       "state must be either int or float.")):
        qs.QubitState([1,0],['c','d'])

    # Test wrong first qubit matrix input size
    with pytest.raises(ValueError, match = ("The first qubit state matrix should be " +
                       "a 2x1 matrix.")):
        qs.QubitState([0,0,0], (1,0))
    
    # Test wrong second qubit matrix input size
    with pytest.raises(ValueError, match = ("The second qubit state matrix should be " +
                       "a 2x1 matrix.")):
        qs.QubitState((1,0), [0,0,0])
    
    # Test an empty qubit state input
    with pytest.raises(ValueError, match = ("The qubit state must have" +
                       " some non-zero entries.")):
        qs.QubitState([0,0],[0,0])


def test_copy():
    """
    Function to test the copy function, making sure that a new object
    is created and not comparing reference pointers.
    """
    q_state = qs.QubitState([1,0,1,0])
    q_state_copy = q_state.copy()

    assert not q_state_copy is q_state


def test_measurements():
    """
    Function to test measurement of qubit states. Ensuring that both
    the two-qubit measurements and single-qubit measurements return
    expected outcomes.
    """
    q_state = qs.QubitState([1,1,0,0])

    # Test measurement on both qubits
    states, probs = zip(*q_state.measure_stats(12))
    assert np.allclose(states[0].peek(), np.array([1,0,0,0]))
    assert np.allclose(states[1].peek(), np.array([0,1,0,0]))
    assert np.isclose(probs[0], 0.5)
    assert np.isclose(probs[1], 0.5)

    # Test measurement on qubit 1
    states, probs = zip(*q_state.measure_stats(1))
    assert np.allclose(states[0].peek(), np.array([0.7071,0.7071,0,0]))
    assert np.isclose(probs[0], 1.0)

    # Test measurement on qubit 2
    states, probs = zip(*q_state.measure_stats(2))
    assert np.allclose(states[0].peek(), np.array([1,0,0,0]))
    assert np.allclose(states[1].peek(), np.array([0,1,0,0]))
    assert np.isclose(probs[0], 0.5)
    assert np.isclose(probs[1], 0.5)


def test_set():
    """
    Function to test the modification of a qubit state after initialisation.
    """
    q_state = qs.QubitState([1,1,0,0])

    assert np.allclose(q_state.set_state([0,0,0,1]), np.array([0,0,0,1]))


def test_compare():
    """
    Function to test the qubit state comparisons, ensuring that the object
    contents are equal, not the reference pointers.
    """
    q_state = qs.QubitState([1,1,0,0])

    # Test comparison
    assert q_state.compare((1,1,0,0))

    # Test error handling for invalid comparison state
    with pytest.raises(ValueError, match = ("Comparison state needs " +
                        "to be a valid numerical qubit input state as a " +
                        "QubitState, NumPy array, list or tuple.")):
        q_state.compare("error")
    