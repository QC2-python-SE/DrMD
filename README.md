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

Installing the DrMD package is a very simple process!

First, you will need to clone the git repository:

```bash
git clone https://github.com/QC2-python-SE/DrMD.git
```
Then, you'll need to install the necessary packages:

```bash
pip install -r requirements.txt
```
You can then build the package:
```bash
pip python setup.py sdist bdist_wheel
```
And validate the build by checking that the following check passes:
```bash
twine check dist/*
```
Finally, can then install the package by running the following command in the base directory:
```bash
pip install .
```

You can verify the installation by running:

```bash
pip show drmd
```

That's it! You're now all set to start using the package.

_Note: The drmd package requires a minimum python version of 3.6. This will automatically be checked in the package installation._

## 📚 Generating Documentation for the Package

Follow these steps to generate the documentation for this package:

---

#### 1. Install Required Packages
Ensure the necessary dependencies are installed (this should already be done from `requirements.txt`):

```bash
pip install nbsphinx nbconvert pandoc
```

#### 2. Clean the Documentation Directory
While in the base directory of the project, navigate to the `docs` directory and clean previous builds:

```bash
cd docs
make clean
```

#### 3. Install Pandoc
##### Using Conda (Recommended):
If you're using `conda`, install `pandoc` by running:

```bash
conda install pandoc
```

##### Without Conda:
Download and install Pandoc based on your operating system:

- **Windows**:  
  Visit the [Pandoc Downloads Page](https://pandoc.org/installing.html), download the installer, and follow the installation steps.

- **Mac/Linux**:  
  Use a package manager:
  - **Mac***:  
    ```bash
    brew install pandoc
    ```
  - **Linux**:  
    ```bash
    sudo apt-get install pandoc
    ```
    *(For Debian-based distributions; use your distro's package manager if different.)*


#### 4. Build the HTML Documentation
Once the dependencies are installed and the directory is clean, build the HTML documentation:

```bash
make html
```

#### 5. View the Documentation
Navigate to the generated `index.html` to browse the documentation for the package:

```plaintext
./docs/build/html/index.html
```
_Note: If you have the latest version of sphinx, you may run into version issues with jinja2. Generating these docs requires jinja2 version 3.0.3. (You may have to uninstall and reinstall jinja2 to satisfy this.)_

## ℹ️ Structure of the package and development info

This project is designed to introduce students to performing quantum circuits in Python. \
The package allows users to play around with applying different quantum operators onto two-qubit states and perform a measurement in the Z-basis at the end of a circuit.

We are designing our package in an iterative and model-driven manner, striving to make our code maintainable, secure, and reusable. Hence we used the object-oriented paradigm, which fits well with these requirements, through abstraction and encapsulation.\
Our humble start (MVP) involved using `UnitaryGate` objects to apply unitaries to vectors given as lists. \
We successively added functionalities, and we plan to iteratively add classes, such as measurement operators! 

Rigorous testing is performed through pytest (due to its ease of use).

Want to be part of the developement team? Give us a ☎️. 

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

## 🧪 Running Tests

To run the tests for this project, follow these steps:

1. Navigate to the `/docs` folder:
```bash
cd docs
```

2. Run the tests using pytest:
```bash
python -m pytest
```

That's it! 🎉 You should now see the results of the tests in the terminal.


## ✍️ Authors

Dillon Lewis dillon.lewis.24@ucl.ac.uk : QubitState (class and tests, with docstrings). Documentation and package generation. README. 

Ralph Jason Costales, ralph.costales.24@ucl.ac.uk : Defined gate_list and developed MVP. Tests for UnitaryGate (with docstrings). README.

Mai Pham, nguyet.pham.24@ucl.ac.uk : Defined gate_list and developed MVP. UnitaryGate class (with docstrings). Tutorial notebook.

Delia Melinte Citea, delia.citea.20@ucl.ac.uk : Circuit (class and tests, with docstrings). README. 

The design of the package (first MVP and successive models) was decided collectively through periodic (documented) design meetings.

## 💭 Feedback and Contributing

Student 👨‍🎓👩‍🎓? Researcher 👨‍🔬👩‍🔬 ? Wandering Critic?\
Tell us :e-mail: what you would like to see from our package! \
We are always interested in improving the users experience so that exploring quantum circuits is accessible to all that find themselves interested.
