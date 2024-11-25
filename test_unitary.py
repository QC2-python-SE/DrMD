import numpy as np
import gate_list as gl
import unitary_gate as ug

x = np.array([0, 1])
y = np.array([1, 0])

print(gl.H_mat)

xmat = ug.UnitaryGate(gl.X_mat)
print(xmat.apply(y))
