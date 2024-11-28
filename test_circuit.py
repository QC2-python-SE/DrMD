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

def test_empty_init():
    """Test empty circuit generation"""
    empty_circ = Circuit()
    assert empty_circ.isEmpty()


def test_singleton_init():
    """Test circuit generation from singleton"""
    #uni = random_unitary() TODO: add random when Mai corrects unitary
    uni = gl.x1
    circ1 = Circuit(uni)
    assert circ1.isEmpty() == False
    assert circ1.size() == 1
    assert circ1.get_element(0) == uni
    circ1.pop()
    assert circ1.isEmpty()

def test_list_init():
    """Test circuit generation from list"""
    #TODO: randomize when Mai corrects unitary
    uni = gl.x1
    gates = [uni, gl.cnot, gl.y2]
    circ1 = Circuit(gates)
    assert circ1.isEmpty() == False
    assert circ1.size() == len(gates)
    assert circ1.get_element(0) == uni
    last = circ1.pop()
    assert last == gates[-1]

def test_wrong_init():
    """Test errors raised for __init__()"""
    gates = gl.CNOT_mat
    with pytest.raises(TypeError) as notList:
        Circuit(gates)
        assert str(notList.value) == \
            "Input needs to be a list of elements UnitaryGate"

    gates = [gl.CNOT_mat, None]
    with pytest.raises(TypeError) as notUni:
        Circuit(gates)
        assert str(notUni.value) == \
            "Elements of input list need to be UnitaryGate"

