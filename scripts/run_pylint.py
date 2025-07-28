# scripts/run_pylint.py

import subprocess
import os

def run_pylint():
    os.makedirs("reports", exist_ok=True)
    with open("reports/pylint_report.txt", "w") as file:
        subprocess.run(["pylint", "src/"], stdout=file)

if __name__ == "__main__":
    run_pylint()
