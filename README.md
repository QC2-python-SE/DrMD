# 📦 DR MD: Qubits and Unitary Gates

## 🌟 Highlights

- Package for students studying Quantum Computing
- Use the package to apply `UnitaryGates` and `Circuits` of unitaries on two-qubit `QubitStates`
- Measure your `QubitState` in the computational basis at the end of your circuit
- Checks are in place to ensure unitarity of gates
- States defined with `QubitState` are automatically renormalised
- Data integrity and validity is ensured by forcing the user to interact with it through class methods.

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

## 🚀 Usage 101

Want to create a unitary gate?\
Just write your unitaries in a `numpy.array`, a `tuple` or a `list`, and feed them into the constructor of the `UnitaryGate` class. \
The class will ensure you are only dealing with unitaries, and that you don't accidentally change the gate in your code!

Want to use a quantum circuit?\
Just feed a list of `UnitaryGate` objects into the constructor of the `Circuit` class. 

(*Psst!* Not sure what to include in your circuit? Toy with random circuits using `random_circuit`, or create an empty one and then `append` unitaries as you go!)

Once you have your unitaries and your circuit, you can just `apply` them onto your states created with the `QubitState` class!\
You can then explore the resulting state using `peek`, and measure in the computational basis (one or both qubits) using `measure_stats` (for statistics) and `measure_collapse` (to collapse the state).

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

This project is designed to introduce students to performing quantum circuits in Python. \
The package allows users to play around with applying different quantum operators onto two-qubit states and perform a measurement in the Z-basis at the end of a circuit.

We are designing our package in an iterative and model-driven manner, striving to make our code maintainable, secure, and reusable.\
Our humble start involved using `UnitaryGate` objects to apply unitaries to vectors given as lists. \
We successively added functionalities, and we plan to iteratively add classes, such as measurement operators! 

Want to make part of the developemnt team? Give us a ☎️. 

### Current state of the package 📦

The functionalities of the package arise at the interplay of three key classes: 
* `QubitState`
* `UnitaryGate`
* `Circuit`

The relationship between classes is the following (in a simplified diagram):
![UML simplified](https://github.com/user-attachments/assets/71916319-1a67-4d13-9fd0-ef604987ee62)

Users may utilize the ```UnitaryGate``` class to perform a variety of operations associated to unitary operators. They can either select from pre-existing gates listed in `gate_list.py`, or are encouraged to experiment with their own unitary gates, which they construct. Gates may be only be built from 4x4 unitary matrices, or from two 2x2 matrices, whatever may suit their fancy. An informative error will be printed should they try to construct a gate from a non-unitary operator, or perhaps a frog :frog:. The class also contains the ```apply``` function that applies the gate to either a four element ```ndarray```, or an object of the ```QubitState``` class. Use ``dagger`` to obtain the Hermitian conjugate of a unitary operator, and ```compare``` to check if two gates are equal. 

`UnitaryGate` objects can be assembled together to form a `Circuit` object. These work in a list-like manner, allowing to `merge` circuits, `append`, `pop`, and retrieve gates from the circuit. Circuits may also be applied to states, just as `UnitaryGate` objects. 

The aforementioned ```QubitState``` class allows users to define qubit states as objects, which are automatically renormalised, as opposed to ndarrays. Errors are issued if the user attempts to construct qubit states of the incorrect shape or type. Through ```peek```, users can get the representation of the qubit state in the computational basis. Two avenues of measurement are offered. The ```measure_stats``` function gives an in-depth review of the qubits post-measurement, detailing all the possible states the measurement projects to and their associated probabilities. The ```measure_collapse``` function merely outputs one such state with a given probability, so toy around and run your circuit over and over and witness the probabilistic nature of quantum circuits for yourself! Partial measurements are also supported.

The integrity of the data is ensured by forcing the user to interact with the representations of unitaries, circuits, and states through the class methods (encapsulation). Thus, unsafe modification of the attributes is prevented.

## ✍️ Authors

Dillon Lewis dillon.lewis.24@ucl.ac.uk

Ralph Jason Costales, ralph.costales.24@ucl.ac.uk

Mai Pham, nguyet.pham.24@ucl.ac.uk

Delia Melinte Citea, delia.citea.20@ucl.ac.uk

## 💭 Feedback and Contributing

Student 👨‍🎓👩‍🎓? Researcher 👨‍🔬👩‍🔬 ? Wandering Critic?\
Tell us :e-mail: what you would like to see from our package! \
We are always interested in improving the users experience so that exploring quantum circuits is accessible to all that find themselves interested.
