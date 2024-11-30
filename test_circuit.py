import pytest
from circuit import Circuit
import gate_list as gl
from unitary_gate import UnitaryGate
from qubit_state import QubitState
import random as rand
from scipy.stats import unitary_group as ug
import numpy as np

def random_unitary() -> UnitaryGate:
    """Return random unitary"""
    uni = ug.rvs(4)
    return UnitaryGate(uni)

# Tests for constructor 

def test_empty_init():
    """Test empty circuit generation"""
    empty_circ = Circuit()
    assert empty_circ.is_empty()

def test_singleton_init():
    """Test circuit generation from singleton"""

    uni = random_unitary()
    circ1 = Circuit(uni)
    
    assert circ1.is_empty() == False
    assert circ1.size() == 1
    assert circ1.get_element(0).compare(uni)
    gate = circ1.pop()

    assert gate != uni  # Check they are distinct objects

    assert circ1.is_empty()

def test_list_init():
    """Test circuit generation from list"""
    #Create random circuit
    gates = []
    for i in range(5):
        gates.append(random_unitary())

    circ = Circuit(gates)

    # Test size stored correct
    assert circ.is_empty() == False
    assert circ.size() == len(gates)

    # Test unitaries properly stored in new objects
    while circ.is_empty() == False:
        last = circ.pop()
        gate = gates.pop()
        assert last.compare(gate) # This indirectly tests __deepcopy
        assert last != gate  # Check they are at distinct addresses
        
def test_wrong_init():
    """Test errors properly raised by constructor on invalid inputs"""

    matrix = gl.CNOT_mat  # Not UnitaryGate object

    # Test only list[UnitaryGate] or UnitaryGate inputs are accepted
    with pytest.raises(TypeError) as notList:
        Circuit(matrix)
        assert str(notList.value) == \
            "Input needs to be a list of elements UnitaryGate"

    gates = [gl.CNOT_mat, None]  # List of matrix objects
    with pytest.raises(TypeError) as notUni:
        Circuit(gates)
        assert str(notUni.value) == \
            "All elements of input list need to be UnitaryGate"
        
    gates = (gl.cnot, gl.x1)  # Tuple of UnitaryGate (not list)
    with pytest.raises(TypeError) as tupleIn:
        Circuit(gates)
        assert str(tupleIn.value) == \
            "Input needs to be a list of elements UnitaryGate"
        
# Test for getters and functionalities
# ( Note: __str__ tested by printing in the notebooks,
#   __deepcopy tested within other functionalities)

def test_empty():
    """Test that is_empty returns True iff circuit is truly empty"""
    circ = Circuit()
    assert circ.is_empty()

    circ = Circuit(gl.cnot)
    assert not circ.is_empty()

def test_size():
    """Test that size is correct"""
    circ = Circuit()
    assert circ.size() == 0

    gates = [gl.x1, gl.cnot, gl.hadamard1]
    circ = Circuit(gates)
    assert circ.size() == len(gates)

def test_append():
    """
    Function to test that unitaries properly appended to circuit,
    and that on invalid input the corresponding error is raised.
    """
    
    circ = Circuit()
    gates = [gl.x1, gl.cnot, gl.hadamard1]

    curr_len = circ.size()  # Current depth of circ

    for u in gates:
        circ.append(u)

        # Check depth increased
        curr_len += 1 
        assert circ.size() == curr_len

        # Check last stored object
        assert circ.get_element(-1).compare(u)  # Check equal
        assert circ.get_element(-1) != u  # Check different address

    # Check circuits are equal at the end
    target_circuit = Circuit(gates)
    assert target_circuit.compare(circ)

    # Test error-raising
    with pytest.raises(TypeError) as invalid_append:
        circ.append(gl.CNOT_mat)  # Try append a matrix
        assert str(invalid_append.value) == \
            "Input must be a UnitaryGate"

def test_pop():
    """
    Function to test that UnitaryGate.pop() mimics 
    behavior of list.pop().
    """
    gates = [gl.x1, gl.cnot, gl.hadamard1, gl.hadamard2]
    circ = Circuit(gates)

    # Empty argument
    last_circ = circ.pop()
    last_gates = gates.pop()
    assert last_circ.compare(last_gates)

    # Numberical argument
    last_circ = circ.pop(-1)
    last_gates = gates.pop(-1)
    assert last_circ.compare(last_gates)

    first_c = circ.pop(0)
    first_g = gates.pop(0)
    assert first_c.compare(first_g)

    # Check remainder of circuit is as expected
    assert circ.size() == len(gates)
    new_circ = Circuit(gates)
    assert circ.compare(new_circ)

def test_get_element():
    """Test UnitaryGate.get_element() behavior."""

def test_insert():
    """TODO"""

def test_merge():
    """TODO"""

def test_copy():
    """TODO"""

def test_compare():
    """TODO"""

def test_apply(): 
    """TODO"""


test_list_init()
print("List init successful")

test_empty_init()
print("Empty list successful")

test_singleton_init()
print("Singleton successful")

test_wrong_init()
print("Wrong init successful")

test_empty()
print("is_empty works well")

test_size()
print(".size() works well")

test_append()
print(".append() works as expected")

test_pop()
print(".pop() works as expected")

test_get_element()
print("Get element works")

test_insert()
print("Insert works")

test_merge()
print("Merge works")

test_copy()
print("Copy works")

test_compare()
print("Compare works")

test_apply()
print("Apply works")
