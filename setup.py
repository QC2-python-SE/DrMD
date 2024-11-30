from setuptools import setup, find_packages

setup(
   name='drmd',
   version='1.0',
   description='A python package for performing gate operations on two qubits.',
   long_description=open("README.md").read(),          
   long_description_content_type="text/markdown",   
   author='DrMD',
   url='https://github.com/QC2-python-SE/DrMD',
   license='MIT',
   packages=find_packages(),
   install_requires=[                       # Dependencies
        "numpy>=2.1.1",
        "scipy>=1.14.1",
        "pytest>=8.3.3",
        "sphinx-build>=8.1.3"
    ],
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
   python_requires=">=3.6",                 # Minimum Python version
)