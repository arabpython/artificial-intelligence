"""يفحص أن بيئة Python الخاصة بالذكاء الاصطناعي جاهزة."""

import sys

import matplotlib
import numpy as np
import pandas as pd
import sklearn


def main() -> None:
    numbers = np.array([10, 20, 30])

    print("Python executable:")
    print(sys.executable)
    print()

    print(f"Python version: {sys.version.split()[0]}")
    print(f"NumPy version: {np.__version__}")
    print(f"Pandas version: {pd.__version__}")
    print(f"Matplotlib version: {matplotlib.__version__}")
    print(f"scikit-learn version: {sklearn.__version__}")
    print(f"NumPy mean test: {np.mean(numbers):.2f}")
    print()
    print("بيئة الذكاء الاصطناعي جاهزة للعمل.")


if __name__ == "__main__":
    main()
