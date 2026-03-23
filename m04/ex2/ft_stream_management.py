import sys


class EmptyImput(Exception):
    pass


if __name__ == "__main__":
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n\n")

    try:
        sys.stdout.write("Input Stream active. Enter archivist ID: ")
        arch_id = input()
        print("Input Stream active. Enter status report: ", end="")
        status = input()
        if not arch_id.strip() or not status.strip():
            raise EmptyImput("Imput cannot be empty!")

    except EmptyImput as err:
        sys.stderr.write(f"\n\33[31mERROR: {err}\n\33[0m\n")
        sys.exit()

    sys.stdout.write(f"\n[STANDARD] Archive status from {arch_id}: {status}\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communitcation channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.\n")
