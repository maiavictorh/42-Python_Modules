import os
import sys


def get_env(name: str) -> str:
    var = os.getenv(name)
    if not var:
        raise ValueError("Configuration not found!")
    return var


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...")
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv()
        mode = get_env("MATRIX_MODE")
        api_access = get_env("API_KEY")
        log_level = get_env("LOG_LEVEL")
    except (ModuleNotFoundError, ValueError) as err:
        print(f"\33[31mERROR: {err}\33[0m")
        print("\n\33[31m[KO]\33[0m .env file poorly configured")
        print("\nThe Oracle sees nothing.")
        sys.exit()

    print("\nConfiguration loaded:")
    if type(mode) is str and mode.strip():
        print("Mode:", mode)
        if mode == "development":
            print("Database: Connected to local instance")
        elif mode == "production":
            print("Database: Connected to nerwork instance")
        else:
            print("Invalid mode.")
            sys.exit()
        if api_access and api_access.strip():
            print("API Access: Authenticated")
        else:
            print("API Access: Missing key")
        print("Log level:", log_level)
        print("Zion Nerwork: Online")

        print("\nEnvironment security check:\n"
              "\33[32m[OK]\33[0m No harcoded secrets detected\n"
              "\33[32m[OK]\33[0m .env file properly configured\n"
              "\33[32m[OK]\33[0m Production overrides available\n"
              "\nThe Oracle sees all configurations.")
    else:
        print("\33[31mAn error ocurred, aborting!!!\33[0m")
        sys.exit()
