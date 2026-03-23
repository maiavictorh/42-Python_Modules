if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    file1 = "lost_archive.txt"
    file2 = "classified_vault.txt"
    file3 = "standard_archive.txt"
    try:
        with open(file1) as file1:
            print(file1.name)
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to {file1}...\n"
              "RESPONSE: Archive not found in storage matrix\n"
              "STATUS: Crisis handled, system stable\n")
    try:
        with open(file2, "w") as file2:
            file2.write("WHATEVER")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to {file2}...\n"
              "RESPONSE: Security protocols deny access\n"
              "STATUS: Crisis handled, security maintained\n")
    try:
        with open("standard_archive.txt") as file3:
            print(f"ROUTINE ACCESS: Attempting access to {file3.name}...\n"
                  f"SUCCESS: Archive recovered - '{file3.read()}'\n"
                  "STATUS: Normal operations resumed\n")
    except Exception as err:
        print(f"ERROR: {err}")
    finally:
        print("All crisis scenarions handled successfully. Archives secure.")
