if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        print("Initiating secure vault access...\n"
              "Vault connection established with failsafe protocols\n")
        with open("classified_data.txt") as file1:
            print(f"SECURE EXTRATION:\n{file1.read()}")
        with open("preservation.txt", "w") as file2:
            print("\nSECURE PRESERVATION:")
            file2.write("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion\n")
    except FileNotFoundError:
        print("\n\33[31mCouldn't reach vault!\33[0m\n")
    finally:
        print("All vault operations completed with maximum security.")
    print(file1.name)
