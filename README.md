# PyVestSolver

## Disclaimers (PLEASE READ!)

**IMPORTANT NOTE:** The scripts and tools within this repository are provided for educational and informational purposes only and do not constitute investment advice. I assume no responsibility for any losses or damages resulting from the use of these tools. Users should conduct their own research and consult with a qualified financial advisor before making any investment decisions.

**ARCHITECTURE NOTE:** This repository utilizes purely mathematical implementations with no external package dependencies. This design choice, while increasing complexity in certain procedures, is necessary to ensure compatibility with MicroPython, making it more versatile.

## Introduction

Welcome to `PyVestSolver`, a personal project of mine, Royden Daniels. This collection of interactive solver scripts is designed to dynamically address various investment-related questions and scenarios through user input. My aim in creating these tools is to deepen both my understanding and that of others in financial theories and applications, serving educational and practical purposes in the field of investment analysis.

## Features

- **Dependency-Free**: Built solely on Python's standard library and mathematical computations for broad compatibility, including with MicroPython environments.
- **Interactive Analysis**: Designed to allow users to input specific parameters and receive tailored outputs, enhancing the learning experience.
- **Educational Tool**: A practical resource for anyone looking to explore investment strategies, market dynamics, and financial modeling.

## Scripts Overview

### M1_ForwardLoanBondHedge.py
Methods for hedging bond investments using forward contracts, with a focus on bond pricing and forward loan agreements.

### M2_ZeroBondPort.py
Functionality for valuing zero-coupon bond portfolios and optimizing allocations to meet future obligations.

### M3_MarketCalc.py
Calculations of expected returns and portfolio statistics using the Capital Asset Pricing Model (CAPM) and fundamental financial theories.

### M4_FamaFrench.py
An interactive tool for applying the Fama-French three-factor model to predict stock returns based on market, size, and value factors.

## Getting Started

1. **Clone the repository** to your local machine.
2. **Navigate** to the repository directory in your terminal.
3. **Disable TestMode** if you wish to provide user input.
4. **Run** the desired script using Python:

bash
python <script_name>.py


## Note on Python Installation and the `math` Module

Before using the scripts in `PyVestSolver`, ensure that Python is installed on your system. Python can be downloaded and installed from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

The scripts within this repository make use of the `math` module, which is part of Python's Standard Library. Therefore, no additional installation is required for the `math` module once Python is installed on your system.

## Contributions

`PyVestSolver` is an open-source project under the MIT License, I warmly welcome contributions, suggestions for improvements, and discussions. Feel free to fork the repository, make your changes, and submit a pull request.

## Acknowledgments

Repository created and maintained by **Royden Daniels **  with the hope of contributing to the financial education and practical tool development community.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

