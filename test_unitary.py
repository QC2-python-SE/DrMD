import numpy as np
import gate_list as gl
import unitary_gate as ug

x = np.array([0, 1])
y = np.array([1, 0])

xmat = ug.UnitaryGate(gl.X_mat)

def test_unitary_apply():
    # Test unitary_gate.apply function
    l = x == xmat.apply(y)
    assert l.all()



test_unitary_apply()
