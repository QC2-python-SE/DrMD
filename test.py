import gate_list
import unitary_gate

def test_apply():
    '''
    Tests if the functions are all working as expected
    '''
    assert (unitary_gate.UnitaryGate.apply(gate_list.cnot, [0,0,1,0]) == [0,0,0,1]).all()
    assert (unitary_gate.UnitaryGate.apply(gate_list.x1, [1,0,0,0]) == [0,0,1,0]).all()
    assert (unitary_gate.UnitaryGate.apply(gate_list.x2, [0,0,1,0]) == [0,0,0,1]).all()
    assert (unitary_gate.UnitaryGate.apply(gate_list.y1, [0,0,1,0]) == [-1.j,0,0,0]).all()
    assert (unitary_gate.UnitaryGate.apply(gate_list.y2, [0,0,1,0]) == [0,0,0,1.j]).all()
    assert (unitary_gate.UnitaryGate.apply(gate_list.z1, [0,0,1,0]) == [0,0,-1,0]).all()
    assert (unitary_gate.UnitaryGate.apply(gate_list.z2, [0,0,1,0]) == [0,0,1,0]).all()

test_apply()
