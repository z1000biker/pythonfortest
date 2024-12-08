#Python Performance Comparison: Simple Loop vs. Numba vs. Multithreading

This project compares the performance of three different approaches for calculating the sum of squares of the first `n` integers in Python:

1. A simple Python for loop.
2. A JIT-compiled function using Numba, which can leverage SIMD instructions like AVX.
3. A multithreaded approach using Python's `threading` module.

Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Performance Comparison](#performance-comparison)
- [Requirements](#requirements)
- [License](#license)

#Installation

To run this project, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

#Required Libraries

You will need to install the following libraries:

- NumPy
- Numba

You can install these libraries using pip:


pip install numpy numba

#Usage

    Clone this repository or download the script.
    Open a terminal or command prompt.
    Navigate to the directory where the script is located.
    Run the script using Python:
         python performance_comparison.py
#Performance Comparison

The script measures the execution time of each approach over 10 runs and prints the average time taken for each method. The results will be displayed in the terminal.
#Requirements

    Python 3.x
    A CPU that supports AVX instructions for optimal performance with Numba.

#License

This project is licensed under the MIT License.

