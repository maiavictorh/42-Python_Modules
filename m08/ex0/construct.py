import sys

if __name__ == "__main__":

    path = sys.prefix
    default_path = sys.base_prefix
    print("\nMATRIX STATUS: ", end="")

    if path == default_path:
        print("You're still plugged in")
        print("\nCurrent Python:", path)
        print("Virtual Environment: None detected")

        print("\n\33[93mWARNING: You're in the global environment!\33[0m")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")

        print("\nThen run this program again.")

    elif path != default_path:
        print("Welcome to the construct")

        split_path = path.split("/")
        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment:", split_path[-1])
        print("Environment Path:", path)

        print("\n\33[92mSUCCESS: You're in an isolated environment!\33[0m")
        print("Safe to install packages without affecting the global system.")

        print("\nPackage installation path:")
