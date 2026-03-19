if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    f1 = None
    try:
        with open("ancient_fragment.txt") as f1:
            print(f"Accessing Storage Vault: {f1.name}")
            print("\033[32mConnection established...\033[0m"
                  "\n\nRECOVERED DATA:")
            print(f1.read())
    except FileNotFoundError:
        print("\033[31mERROR: Storage vault not found\033[0m")
    finally:
        if f1:
            f1.close()
        print("\n\033[32mData recovery complete."
              " Storage unit disconnected.\033[0m")
