GREEN = "\33[92m"
YELLOW = "\33[93m"
RED = "\33[31m"
NC = "\33[0m"

if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    dependency_check = True

    try:
        import pandas # type: ignore
        print(f"{GREEN}[OK]{NC} pandas ({pandas.__version__})"
              "- Data manipulation ready")
    except ImportError:
        dependency_check = False
        print(f"{RED}[ERROR]{NC}: pandas not found")
        print("Try pip install -r requirements.txt or poetry install\n")
    try:
        import numpy # type: ignore
        print(f"{GREEN}[OK]{NC} numpy ({numpy.__version__})"
              "- Data manipulation ready")
    except ImportError:
        dependency_check = False
        print(f"{RED}[ERROR]{NC}: numpy not found")
        print("Try pip install -r requirements.txt or poetry install\n")
    try:
        import requests # type: ignore
        print(f"{GREEN}[OK]{NC} requests ({requests.__version__})"
              "- Data manipulation ready")
    except ImportError:
        dependency_check = False
        print(f"{RED}[ERROR]{NC}: requests not found")
        print("Try pip install -r requirements.txt or poetry install\n")
    try:
        import matplotlib # type: ignore
        print(f"{GREEN}[OK]{NC} matplotlib ({matplotlib.__version__})"
              "- Data manipulation ready")
    except ImportError:
        dependency_check = False
        print(f"{RED}[ERROR]{NC}: matplotlib not found")
        print("Try pip install -r requirements.txt or poetry install\n")

    if not dependency_check:
        print(YELLOW, "Couldn't complete analysis", NC)
    else:
        print("\nAnalyzing Matrix Data...")
