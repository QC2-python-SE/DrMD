from unitary_gate import UnitaryGate
from qubit_state import QubitState
from typing import TypeVar
import numpy as np

circ_in = TypeVar("circ", list[UnitaryGate], UnitaryGate)

class Circuit:
    """
    Class for storing circuits acting on 2 qubits.

    The circuit is stored as a list of unitary gates,
    Indexing starts from 0 for the gate that is first applied.

    The list of gates is inteded to be a protected attribute, 
    to be accessed through the class methods to avoid midhandling.
    
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
        
        if self.isEmpty():
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
        
    def isEmpty(self):
        """Return True if the circuit is empty, False otherwise."""
        return self._gates == []
    
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

        Return:
            UnitaryGate: the unitary that was removed from the circuit.
        """
        return self._gates.pop(index)
    
    def get_element(self, index: int) -> UnitaryGate:
        """
        Returns copy of unitary at position index in circuit.

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

    def size(self):
        """Returns number of gates in (depth of) circuit"""
        return len(self._gates)

    def copy(self):
        """
        Creates and returns deep copy of circuit.

        Returns:
            Circuit: deep copy of self
        """
        gates = self.__deepcopy(self._gates)

        copied = Circuit(gates)
        return copied

    def merge(self, circuit: 'Circuit'):
        """
        Modify current circuit by appending deep copy 
        of another circuit to the end.

        Args:
            circuit: object of type Circuit, which
                     will be appended to current object

        Raise:
            TypeError: if input not of type Circuit

        Return:
            Circuit: reference to self
        """

        if type(circuit) != Circuit:
            raise TypeError("Merged element must be of type ", type(self))
        
        for unitary in circuit._gates:
            self.append(unitary)    # to perform deep copy

        return self
    
    def apply(self, in_state):
        """
        Apply circuit to a state and return output state.
        Input state is not modified.

        Args:
            in_state (QubitState or np.array): state to which self is applied

        Return:
            QubitState or np.array: state after applying the circuit, same
            return type as input
        
        Raises:
            ValueError: if np.array state not of correct size
            TypeError: if input not QubitState or np.array
        """
        #TODO: correct (clean) code after Mai solves the unitary_gate 

        if not isinstance(in_state, (QubitState, np.ndarray)):
            raise(TypeError, "Input must be a QubitState or numpy.ndarray")
        
        if type(in_state) == np.ndarray:
            if in_state.shape != (4,) or in_state.ndim != 1:
                raise(ValueError, "wrong size of state")

        out_state = in_state.copy()  # don't modify input

        for unitary in self._gates:
            out_state = unitary.apply(out_state)
            
        return out_state
    
    def print(self):
        """
        Alternative method for printing gates of circuit.
        """
        
        if self.isEmpty():
            print("Empty circuit")
            return
        
        print("The gates applied are: ")

        for unitary in self._gates:
            unitary.print()
    

        
    






