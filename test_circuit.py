import pytest
from circuit import Circuit, random_circuit
import gate_list as gl
from unitary_gate import random_unitary
from qubit_state import QubitState
import random as rand
import numpy as np


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
    """Test errors are properly raised by constructor on invalid inputs"""

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

    for i in range(10): # Test for multiple random data
        depth = rand.randint(1,20)
        circ = random_circuit(depth)
        assert circ.size() == depth

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

    # Numerical argument
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

    for i in range(10): # Test with multiple random data

        # Create random circuit
        depth = rand.randint(1, 20)
        circ = random_circuit(depth)

        # Create random valid index
        index = rand.randint(1, depth)

        # Insert valid unitary at index
        uni = random_unitary()
        original = circ.copy()
        circ.insert(index, uni)

        # Test correct size and element
        assert circ.size() == depth + 1
        assert circ.get_element(index).compare(uni)

        # Test appended object is at distinct address 
        uni_in_circ = circ.pop(index)
        assert uni != uni_in_circ

        # Test rest of circuit unmodified
        assert circ.compare(original)


def test_merge():
    """TODO"""
    
    # Test TypeError is properly raised
    circ1 = Circuit()
    with pytest.raises(TypeError) as invalid_in:
        circ1.merge(gl.CNOT_mat)  # Try append a matrix
        assert str(invalid_in.value) == \
            "Merged element must be of type Circuit"
    
    # Test merge functionality on multiple random data
    for i in range(10):
        depth1 = rand.randint(1, 5)
        circ1 = random_circuit(depth1)
    
        depth2 = rand.randint(1, 5)
        circ2 = random_circuit(depth2)

        og = circ1.copy()

        # Test two random circuits are properly merged
        circ1.merge(circ2)

        # Check correct size
        assert circ1.size() == depth1 + depth2

        # Check elements are correct
        for i in range(depth1):
            # Check first part is the original circ1
            u_circ1 = circ1.get_element(i)
            assert og.get_element(i).compare(u_circ1)
    
        for i in range(depth1, circ1.size()):
            # Check second part is circ2
            u_circ2 = circ2.get_element(i - depth1)
            assert circ1.get_element(i).compare(u_circ2)

        # Check elements merged are stored at new addresses
        last_1 = circ1.pop()
        last_2 = circ2.pop()
        assert last_1.compare(last_2)
        assert last_1 != last_2

def test_copy():
    """TODO"""

    for i in range(10):
        depth1 = rand.randint(0, 10)
        circ1 = random_circuit(depth1)

        circ2 = circ1.copy()

        # Test size
        assert circ1.size() == circ2.size()

        # Test elements
        while not circ1.is_empty():
            u1 = circ1.pop()
            u2 = circ2.pop()
            assert u1.compare(u2)  # Check elements are identical
            assert u1 != u2  # Check different addresses


def test_compare():
    """TODO"""
    gates = [gl.x1, gl.cnot, gl.hadamard1, gl.hadamard2]
    circ = Circuit(gates)

    # Test error is raised on list input
    with pytest.raises(TypeError) as invalid_in:
        circ.compare(gates)  
        assert str(invalid_in.value) == \
            "Input must be a Circuit"
        
    # Test comparisons work
    circ2 = Circuit()
    assert circ.compare(circ2) == False

    circ2.merge(circ)
    assert circ.compare(circ2)

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
