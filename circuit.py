from unitary_gate import UnitaryGate

class Circuit:
    """
    Class for storing circuits acting on 2 qubits.

    The circuit is stored as a list of unitary gates,
    Indexing starts from 0 for the gate that is first applied.

    The list of gates is inteded to be a protected attribute, 
    to be accessed through the class methods to avoid midhandling.
    
    Attributes:
        _gates (list[UnitaryGate]): a list of unitaries 
        describing the circuit.
    """

    def __init__(self, gates: list[UnitaryGate] = []):
        """
        Constructor of a a 2-qubit circuit.

        Args: 
            gates: a list of unitary gates. Implicitly, it is an empty list.

        Raises:
            TypeError: if input type is wrong.
        """

        # Check correct type of input:
        if type(gates) is not list:
            raise TypeError("Input needs to be a list of elements UnitaryGate")
        elif not all(type(x) is UnitaryGate for x in gates):
            raise TypeError("Elements of the input list need to be UnitaryGate")
        
        # store deep copy so that gate list cannot be modified via reference:
        self._gates= self.__deepcopy(gates)

    def __deepcopy(self, gates):
        # Private method to create a deep copy of gates list
        returned = []
        for unitary in gates:
            returned.append(unitary.copy())
        return returned
        
    def isEmpty(self):
        return self._gates == []
    
    def print(self):
        """
        TODO: perhaps change with __str__. Add separator (eventually)
        """

        if self.isEmpty():
            print("Empty circuit")
            return
        
        print("The gates applied are: ")

        for unitary in self._gates:
            unitary.print()


    def append(self, unitary: UnitaryGate):
        """
        Appends copy of unitary to the end of the circuit.
        (Copy of unitary: because we don't want it to be 
        modified via reference after appending to the circuit)
        TODO: modify docstring.
        
        Args:
            unitary: a unitary stored in UnitaryGate object

        Raises:
            TypeError: if input is not a UnitaryGate
        """

        if type(unitary) is not UnitaryGate:
            raise TypeError("Input must be a UnitaryGate")
        
        self._gates.append(unitary.copy())

    def pop(self, index = -1) -> UnitaryGate:
        """
        Removes gate at position index from circuit and returns the removed unitary.
        See also behavior of list.pop() in the Python3 documentation.

        Raise:
            IndexError: if index out of bounds or if circuit is empty.

        Return:
            UnitaryGate: the unitary that was removed from the circuit.
        """
        return self._gates.pop(index)
    
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

    def copy(self):
        """
        Creates and returns deep copy of circuit.

        Returns:
            circuit: deep copy of current object
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
            self: reference to current object
        """

        if type(circuit) != Circuit:
            raise TypeError("Merged element must be of type ", type(self))
        
        for unitary in circuit._gates:
            self.append(unitary)    # to perform deep copy

        return self
    
    def apply(self, in_state):
        """
        TODO: update with Dillon's class when he is done? For tests
        Apply circuit to a state and return output state.
        Input state is not modified.

        Args:
            in_state (QubitState): state to which circuit is applied

        Return:
            out_state (QubitState): state after applying the circuit
        """

        out_state = in_state.copy()

        for unitary in self._gates:
            out_state = unitary.apply(out_state)
            
        return out_state
    

        
    






