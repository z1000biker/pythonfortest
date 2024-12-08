# Python Performance Comparison: Simple Loop vs. Numba vs. Multithreading

This project compares the performance of three different approaches for calculating the sum of squares of the first `n` integers in Python:

1. A simple Python for loop.
2. A JIT-compiled function using Numba, which can leverage SIMD instructions like AVX.
3. A multithreaded approach using Python's `threading` module.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Performance Comparison](#performance-comparison)
- [Requirements](#requirements)


## Installation

To run this project, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Required Libraries

You will need to install the following libraries:

- **NumPy**
- **Numba**

You can install these libraries using pip:


pip install numpy numba


