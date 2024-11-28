import gate_list as gl
from unitary_gate import UnitaryGate
from qubit_state import QubitState

'''
A testing python file that has been designed to ensure that the constructor
as well as the functions apply and dag in the UnitaryGate class operate as 
expected.
'''

def test_construction():
    '''
    Function to test the error raising in the constructor of the UnitaryGate
    class. Errors for constructing an operator that is not a tuple, list or
    NumPy array is flagged to ensure the appropriate error is encountered.


    '''
    with pytest.raises(TypeError, match = "The unitary gate matrix must be a"\
                       " tuple, list or NumPy array."):
        UnitaryGate("Error inducing input")
    
    with pytest.raises(ValueError, match = "The unitary gate matrix should "\
                       "be a 4x4 matrix."):
        UnitaryGate(np.array([[1, 0, 0, 0], [0, 1, 0, 0]]))

def test_apply():
    '''
    Function to test the apply function in the UnitaryGate class. This
    function takes a one or two qubit unitary gate and applies it to a two
    qubit state, outputting another qubit state.

    We use the X1, X2 and Z1 gates acting on the |00> state as a vector as an 
    example to ensure the apply function is performing matrix multiplication
    correctly and outputting the correct states, being |01>, |00> and |00> 
    respectively.
    '''
    example_ndarray = [1,0,0,0]
    example_qubitstate = QubitState([1,0,0,0])

    assert (gl.x1.apply(example_ndarray) == [0,0,1,0]).all()
    assert (gl.x2.apply(example_ndarray) == [1,0,0,0]).all()
    assert (gl.z1.apply(example_ndarray) == [1,0,0,0]).all()

    assert (gl.y1.apply(example_qubitstate) = [0,0,1.j,0]).all()

    with pytest.raises(ValueError, match = "Wrong size of state"):
        gl.z2.apply([0,0,1])

    with pytest.raises(TypeError, match = "Input must be numpy.ndarray or QubitState"):
        gl.y1.apply('Error inducing input')

test_apply()