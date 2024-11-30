from unitary_gate import UnitaryGate, random_unitary
from qubit_state import QubitState
from typing import TypeVar
import numpy as np

circ_in = TypeVar("circ", list[UnitaryGate], UnitaryGate)
state_type = TypeVar("state", np.ndarray, QubitState)

class Circuit:
    """
    Class for storing circuits acting on 2 qubits.

    The circuit is stored as a list of unitary gates,
    Indexing starts from 0 for the gate that is first applied.

    The list of gates is inteded to be a protected attribute, 
    to be accessed through the class methods to avoid mishandling.

    Gates stored within circuit objects are copies of the gates
    given as parameters, to preserve the integrity of the data 
    from unwanted external modifications. 
    
    Attributes:
        _gates (list[UnitaryGate]): a list of unitaries describing the circuit.
    """

    def __init__(self, gates: circ_in = []):
        """
        Constructor of a a 2-qubit circuit.

        Args: 
            gates (list[UnitaryGate] or UnitaryGate): a list of unitary gates,
            or a single unitary. Implicitly, it is an empty list.

        Raises:
            TypeError: if input type is wrong.
        """
        if type(gates) is UnitaryGate:
            gates = [gates]

        # Check correct type of input:
        if type(gates) is not list:
            raise TypeError("Input needs to be a list of elements UnitaryGate")
        elif not all(type(x) is UnitaryGate for x in gates):
            raise TypeError("Elements of input list need to be UnitaryGate")
        
        # store deep copy so that gate list cannot be modified via reference:
        self._gates= self.__deepcopy(gates)
    
    def __str__(self):
        """
        Override behavior of str so that matrices of the circuit are printed.
        """
        
        if self.is_empty():
            return "Empty circuit"
        
        mess = "The gates applied are: \n"

        for unitary in self._gates[:-1]:
            mess = mess + str(unitary)
            mess = mess + ", \n"
        
        mess = mess + str(self._gates[-1]) 
        mess = mess + ".\n"
        
        return mess
    
    
    def __deepcopy(self, gates):
        # Private method to create a deep copy of gates list
        returned = []
        for unitary in gates:
            returned.append(unitary.copy())
        return returned
        
    def is_empty(self):
        """Return True if the circuit is empty, False otherwise."""
        return self._gates == []
    
    def size(self):
        """Returns number of gates in (depth of) circuit"""
        return len(self._gates)
    
    def append(self, unitary: UnitaryGate):
        """
        Appends unitary to the end of the circuit.
        A deep copy of the unitary is appended instead of a reference
        for encapsulation.
        
        Args:
            unitary (UnitaryGate): unitary to be appended to circuit

        Raises:
            TypeError: if input is not a UnitaryGate
        """

        if type(unitary) is not UnitaryGate:
            raise TypeError("Input must be a UnitaryGate")
        
        self._gates.append(unitary.copy())

    def pop(self, index = -1) -> UnitaryGate:
        """
        Removes gate at position index from circuit 
        and returns the removed unitary.
        See also: behavior of list.pop() in Python3.

        Raise:
            IndexError: if index out of bounds or if circuit is empty.

        Returns:
            UnitaryGate: the unitary that was removed from the circuit.
        """
        return self._gates.pop(index)
    
    def get_element(self, index: int) -> UnitaryGate:
        """
        Returns a copy of the unitary at position index in self.

        Args:
            index (int): position of the unitary to be returned
        
        Returns:
            UnitaryGate: copy of gate in circuit at position index.

        Raises:
            IndexError: if index out of bounds.
        
        """
        return self._gates[index].copy()
    
    def insert(self, index: int, unitary: UnitaryGate):
        """
        Insert at position index a unitary in the circuit.
        If index exceeds the depth of the circuit, the method
        will append the unitary at the end.
        See also the behavior of list.insert() in Python3.

        Args:
            index (int): position at which unitary is inserted
            unitary (UnitaryGate): unitary whose deep copy is 
                    inserted in the circuit
        """
        self._gates.insert(index,unitary.copy())

    def merge(self, circuit: 'Circuit'):
        """
        Modify current circuit by appending deep copy 
        of the gates in another circuit to the end.

        Args:
            circuit: object of type Circuit, whose gates
                     will be appended to current object

        Raise:
            TypeError: if input not of type Circuit

        Returns:
            Circuit: reference to self
        """

        if type(circuit) != Circuit:
            raise TypeError("Merged element must be of type Circuit")
        
        for unitary in circuit._gates:
            self.append(unitary)    # to perform deep copy

        return self
    
    def copy(self):
        """
        Creates and returns deep copy of circuit.

        Returns:
            Circuit: deep copy of self
        """
        gates = self.__deepcopy(self._gates)

        copied = Circuit(gates)
        return copied
    
    def apply(self, in_state: state_type) -> state_type:
        """
        Apply circuit to a state and return output state.
        Input state is not modified.

        Args:
            in_state (QubitState or np.array): state to which self is applied

        Returns:
            QubitState or np.array: state after applying the circuit, 
            of same type as the input
        
        Raises:
            ValueError: if np.array state not of correct size
            TypeError: if input not QubitState or np.array
        """

        out_state = in_state.copy()  # don't modify input

        for unitary in self._gates:
            out_state = unitary.apply(out_state)  # errors handled here 
            
        return out_state
    
    def compare(self, circ: 'Circuit') -> bool:
        """
        Function for comparing self to another circuit.
        Returns True iff. the two circuits apply same gates in same order.

        Args:
            circ (Circuit): a circuit to be compared with self

        Returns:
            bool: True iff. the two circuits have same circuit diagram.
        """
        if type(circ) is not Circuit:
            raise TypeError("Input must be a Circuit")

        if circ.size() != self.size():
            return False

        for i in range(circ.size()):
            if not self._gates[i].compare(circ._gates[i]):
                return False 
            
        return True
    
    def print(self):
        """
        Alternative method for printing gates of circuit.
        """
        
        if self.is_empty():
            print("Empty circuit")
            return
        
        print("The gates applied are: ")

        for unitary in self._gates[:-1]:
            print(unitary, ", \n")
        
        print(self._gates[-1], ".\n")
    
def random_circuit(depth: int = 1) -> Circuit:
    """
    Function that returns a random circuit of unitaries,
    of given depth.

    Args:
        depth (int): depth of the circuit to be returned.
                    Implicitly, it is 1.

    Returns:
        Circuit : circuit with 'depth' random unitaries
    """
    gates = []

    for i in range(depth):
        gates.append(random_unitary())
    
    return Circuit(gates)
        
    






