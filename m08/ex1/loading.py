GREEN = "\33[92m"
YELLOW = "\33[93m"
RED = "\33[31m"
NC = "\33[0m"

if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    dependency_check = True

    try:
        import pandas  # type: ignore
        print(f"{GREEN}[OK]{NC} pandas ({pandas.__version__})"
              "- Data manipulation ready")
    except ImportError:
        dependency_check = False
        print(f"{RED}[ERROR]{NC}: pandas not found")
    try:
        import numpy  # type: ignore
        print(f"{GREEN}[OK]{NC} numpy ({numpy.__version__})"
              "- Data manipulation ready")
    except ImportError:
        dependency_check = False
        print(f"{RED}[ERROR]{NC}: numpy not found")
    try:
        import requests  # type: ignore
        print(f"{GREEN}[OK]{NC} requests ({requests.__version__})"
              "- Data manipulation ready")
    except ImportError:
        dependency_check = False
        print(f"{RED}[ERROR]{NC}: requests not found")
    try:
        import matplotlib  # type: ignore
        from matplotlib import pyplot  # type: ignore
        print(f"{GREEN}[OK]{NC} matplotlib ({matplotlib.__version__})"
              "- Data manipulation ready")
    except ImportError:
        dependency_check = False
        print(f"{RED}[ERROR]{NC}: matplotlib not found")

    if not dependency_check:
        print(YELLOW, "\nCouldn't complete analysis", NC)
        print("Try pip install -r requirements.txt or poetry install\n")

    else:
        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        time = numpy.linspace(0, 10, 1000)
        sign = numpy.sin(time) + numpy.random.normal(0, 0.3, 1000)
        df = pandas.DataFrame({
            "time": time,
            "signal": sign})

        print("Generating visualization...")
        pyplot.figure()
        pyplot.plot(df["time"], df["signal"])
        pyplot.title("Matrix Signal Activity")
        pyplot.xlabel("Time")
        pyplot.ylabel("Signal Strenght")
        pyplot.savefig("matrix_analysis.png")

        print("\nAnalysis complete!")
        print("Result saved to: matrix_analysis.png")
