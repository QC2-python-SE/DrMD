'''
A testing python file that has been designed to ensure that the constructor
as well as the functions apply and dag in the UnitaryGate class operate as 
expected.
'''

import gate_list as gl
from unitary_gate import UnitaryGate
from qubit_state import QubitState

def test_construction():
    '''
    Function to test the error raising in the constructor of the UnitaryGate
    class. Errors for constructing an operator that is not a tuple, list or
    NumPy array is flagged to ensure the appropriate error is encountered.
    This function also ensures the matrices are th approriate size for 
    generating an overall two qubit operation.

    This is done for both the two qubit gate input and the two separate one
    qubit gate inputs.
    '''
    with pytest.raises(TypeError, match = "The unitary gate matrix must be a"\
                       " tuple, list or NumPy array."):
        UnitaryGate("Error inducing input")
    
    with pytest.raises(ValueError, match = "The unitary gate matrix should "\
                       "be a 4x4 matrix."):
        UnitaryGate(np.array([[1, 0, 0, 0], [0, 1, 0, 0]]))

    with pytest.raises(TypeError, match = "The first unitary gate matrix "\
                       "must be a tuple, list or NumPy array."):
        UnitaryGate("Error inducing input", gl.H_mat)

    with pytest.raises(TypeError, match = "The second unitary gate matrix "\
                       "must be a tuple, list or NumPy array."):
        UnitaryGate(gl.H_mat, "Error inducing input")

    with pytest.raises(ValueError, match = "The first unitary gate matrix "\
                       "should be a 2x2 matrix."):
        UnitaryGate(gl.hadamard1, gl.H_mat)

    with pytest.raises(ValueError, match = "The second unitary gate matrix "\
                       "should be a 2x2 matrix."):
        UnitaryGate(gl.H_mat, gl.hadamard2)

test_construction

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

    assert (gl.y1.apply(example_qubitstate) = [0,0,1j,0]).all()

    with pytest.raises(ValueError, match = "Wrong size of state"):
        gl.z2.apply([0,0,1])

    with pytest.raises(TypeError, match = "Input must be numpy.ndarray or QubitState"):
        gl.y1.apply('Error inducing input')

test_apply()

def test_dag():
    '''
    Function that tests the dag function by taking an example operator
    and ensuring that it has output the Hermitian matrix.

    We use the simple example of a non-Hermitian unitary being the XZ gate
    acting on qubit 1. The dagger function should output the Hermitian
    conjugate of the matrix which has been calculated for comparison by hand.
    '''
    example = UnitaryGate(np.kron(X_mat @ Z_mat,I_mat))
    example_hermitianconjugate = UnitaryGate(np.array([[0, -1, 0, 0],
                        [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]]))

    assert (example.dagger() == example_hermitianconjugate).all()





