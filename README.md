# 📦 DR MD: Qubits and Unitary Gates

## 🌟 Highlights

To come back later (summarise main points of Overview + main sale points)
- Some functionality made easy!
- This problem handled
- etc.

## Who is this package for? 🧑‍🎓

Are you an Undergrad or Master's student learning Quantum? Are you a PhD student in the physical sciences who needs to quickly check circuit calculations?

This package is **for you**.

The *DR. MD quantum circuits and unitaries* package allows you to create, view, and apply unitary operations on 2-qubit states!

And if you are not too sure about what you are doing? 

**Worry not!** 

We created the package with this kind of situations in mind: \
we've put checks :guard: in place to ensure that no accidental mishandling of the data takes place!\
We also check for your that your operations are unitary, and renormalise your quantum states to save you some time. 😉

That way you can focus :mag_right: on what matters most!

## 🚀 Usage

Want to create a unitary gate?\
Just write your unitaries in a `numpy.array`, a `tuple` or a `list`, and feed them into the constructor of the `UnitaryGate` class. \
The class will ensure you are only dealing with unitaries, and that you don't accidentally change the gate in your code!

Want to use a quantum circuit?\
Just feed a list of `UnitaryGate` objects into the constructor of the `Circuit` class. 

(*Psst!* Not sure what to include in your circuit? Toy with random circuits using `random_circuit`, or create an empty one and then `append` unitaries as you go!)

Once you have your unitaries and your circuit, you can just `apply` them onto your states created with the `QubitState` class!\
You can then explore the resulting state using `peek`, and measure in the computational basis (one or both qubits) using `measure_stats` (for statistics) and `measure_collapse` (to randomly collapse the state according to the distribution).

**Feeling lazy 😴?** \
You can also apply unitaries and circuits directly onto `numpy.ndarray` objects - but make sure you know what you are doing! \
The resulting state might not be normalised. Using the `QubitState` class will ensure normalisation for you instead.

We also predefined a range of unitaries for you in the `gate_list` file.

**You can find a tutorial notebook plenty of examples in the folder `docs\source\notebooks`.** 

## ⬇️ Installation

FOR DILLON:
Simple, understandable installation instructions!

```bash
pip install my-package
```

And be sure to specify any other minimum requirements like Python versions or operating systems.

*You may be inclined to add development instructions here, don't.*


## ℹ️ Structure of the package and development info

This project is designed to introduce students to performing quantum circuits on Python. This package allows users to play around with applying different quantum operators onto two-qubit states and perform a measurement in the Z-basis at the end of a circuit.

Users may utilize the ```UnitaryGate``` class found in unitary_gate.py to construct gates in their quantum circuit and perform a variety of operations associated to unitary operators. Users can either select from pre-existing gates listed in gate_list.py, which covers essential gates like the Pauli matrices, as well as the Hadamard and CNOT gates. Of course, users are also permitted to and encouraged to experiment with their own unitary gates they construct using the ```UnitaryGate``` class. Gates may be only be constructed from 4x4 unitary matrices, or from two 2x2 matrices, whatever may suit their fancy. The class is constructed such that an informative error will be printed should they try to construct a gate from a non-unitary operator, or perhaps a frog. The class also contains the ```apply``` function that takes a gate and applies it to either a four element ```ndarray``` or an object from the ```QubitState``` class. *(idk what the ```repr``` or ```copy``` function really does sorry)*. The ``dagger`` function returns the Hermitian conjugate of a unitary operator, a crucial feature as the Hermitian conjugate of unitaries are their own inverse. The ```compare``` function allows users to compare if two gates are equal, allowing users to becoming familiar with important relationships in quantum circuits, such as the relationships between Pauli matrices or how the X gate is equivalent to applying a Hadamard, Z, then Hadamard gates on a qubit. The ```random_unitary``` function also allows users to toy with random circuits.

The aforementioned ```QubitState``` class in qubit_state.py allows users to define qubit states as objects, as opposed to ndarrays. Users are, as before, given errors before constructing qubit states of the incorrect shape or type (our package only permits two qubit circuits, so either a single 4x1 array or two 2x1 arrays corresponding to each qubit!). The ```peek``` function allows users to get an informative understanding of the qubit state in the computational basis at any point of the circuit to ensure the circuit works as expected at every point. Two avenues of measurement are also offered by this package. The ```measure_stats``` function gives an in-depth review of the qubits post-measurement, detailing all the possible states the measurement projects to and their associated probabilities. The ```measure_collapse``` function merely outputs one such state with a given probability, so toy around and run your circuit over and over and witness the probabilistic nature of quantum circuits for yourself!

*(I don't understand half of the functions in QubitState to be honest)*

## ✍️ Authors

Dillon Lewis dillon.lewis.24@ucl.ac.uk

Ralph Jason Costales, ralph.costales.24@ucl.ac.uk

Mai Pham, nguyet.pham.24@ucl.ac.uk

Delia Melinte Citea, delia.citea.20@ucl.ac.uk

## 💭 Feedback and Contributing

Student 👨‍🎓👩‍🎓? Researcher 👨‍🔬👩‍🔬 ? Wandering Critic?\
Tell us :e-mail: what you would like to see from our package! \
We are always interested in improving the users experience so that exploring quantum circuits is accessible to all that find themselves interested.
