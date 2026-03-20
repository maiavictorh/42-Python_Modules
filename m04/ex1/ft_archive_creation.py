if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    data_tab = ["New quantum algorithm discovered",
                "Efficiency increased by 347%",
                "Archived by Data Archivist trainee"]
    try:
        with open("new_discovery.txt", "w") as file:
            print(f"Initializing new storage unit: {file.name}")
            print("\33[32mStorage unit created successfully...\33[0m"
                  "\n\nInscribing preservation data...")
            i = 1
            for data in data_tab:
                file.write(f"[ENTRY 00{i}] {data}\n")
                print(f"[ENTRY 00{i}] {data}")
                i += 1
    except Exception as err:
        print(f"\33[31mError: {err}\33[0m")
    finally:
        if file:
            print("\n\33[32mData incription complete."
                  " Storage unit sealed.\33[0m\n"
                  f"Archive {file.name} ready for long-term preservation")
            file.close()
