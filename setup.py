from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
   name='drmd',
   version='1.0',
   description='A python package for performing quantum gate operations on two qubits.',
   long_description=open("README.md", encoding="utf-8").read(),          
   long_description_content_type="text/markdown",   
   author='DrMD',
   author_email=('dillon.lewis.24@ucl.ac.uk', 'nguyet.pham.24@ucl.ac.uk', 'ralph.costales.24@ucl.ac.uk', 'delia.citea.20@ucl.ac.uk'),
   url='https://github.com/QC2-python-SE/DrMD',
   license='MIT',
   packages=find_packages(),
   install_requires=[                       # Dependencies
        "numpy<2",
        "scipy>=1.14.1",
        "pytest>=8.3.3",
        "wheel",
        "bar",
        "greek",
        "docutils<0.18"],
   python_requires=">=3.6",                 # Minimum Python version
)