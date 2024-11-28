import gate_list as gl
from unitary_gate import UnitaryGate as ug

'''
A testing python file that has been designed to ensure that apply function
correctly applies unitary gates on states.
'''

def test_apply():
    '''
    Function to test the operation of the unitary gates on example states.
    The apply function takes a 1 or 2 qubit gate as an input, 
    as well as an two qubit state, and outputs a vector with four inputs.

    We use several gates and states as an example to ensure the apply function
    is performing matrix multiplication correctly and outputting the correct
    states.
    '''
    #Perform a CNOT on |10> to get |11> 
    assert (ug.apply(gl.cnot, [0,0,1,0]) == [0,0,0,1]).all()
    #Perform X1 on |00> to get |10>
    assert (ug.apply(gl.x1, [1,0,0,0]) == [0,0,1,0]).all()
    #Perform X2 on |10> to get |11>
    assert (ug.apply(gl.x2, [0,0,1,0]) == [0,0,0,1]).all()
    #Perform Y1 on |10> to get -i|00>
    assert (ug.apply(gl.y1, [0,0,1,0]) == [-1.j,0,0,0]).all()
    #Perform Y2 on |10> to get i|11>
    assert (ug.apply(gl.y2, [0,0,1,0]) == [0,0,0,1.j]).all()
    #Perform Z1 on |10> to get -|10>
    assert (ug.apply(gl.z1, [0,0,1,0]) == [0,0,-1,0]).all()
    #Perform Z2 on |10> to get |10> 
    assert (ug.apply(gl.z2, [0,0,1,0]) == [0,0,1,0]).all() 

test_apply()