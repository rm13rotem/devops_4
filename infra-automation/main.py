import sys
import os
import logging


# Make sure Python can find the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.JsonSerializer import JsonSerializer
from src.Machine import Machine


def print_menu():
    print("\n=== Machine Manager ===")
    print("1. List machines")
    print("2. Add a new machine")
    print("3. Save machines")
    print("4. Exit")


def list_machines(machines):
    if not machines:
        print("\nNo machines found.")
        return

    print("\nCurrent machines:")
    for m in machines:
        print("-------------------")
        print(m) 
        #use __str__ method


def add_machine(machines):
    try:
        print("\nEnter details for the new machine:")
        id_value = int(input("ID: "))
        name_value = input("Name: ")
        status_value = input("Status (online/offline): ")

        # Optional fields can be filled automatically by Pydantic
        ip_value = input("IP (optional, press Enter to skip): ").strip()
        ip_value = ip_value if ip_value else None

        os_value = input("Operating system (default Linux): ").strip()
        os_value = os_value if os_value else "Linux"

        cpu_value_input = input("CPU cores (default 4): ").strip()
        cpu_value = int(cpu_value_input) if cpu_value_input else 4

        ram_value_input = input("RAM in GB (default 16): ").strip()
        ram_value = int(ram_value_input) if ram_value_input else 16

        machine = Machine(
            id=id_value,
            name=name_value,
            status=status_value,
            ip=ip_value,
            operating_system=os_value,
            cpu_cores=cpu_value,
            ram_gb=ram_value
        )

        machines.append(machine)
        print("\nMachine added successfully!")

    except Exception as e:
        print(f"\nError: {e}")


def main():
    serializer = JsonSerializer()
    machines = serializer.Load()  # Load existing ones
    logger = logging.getLogger(__name__)
    
    logger.info("Loaded %d machines from instances.json.", len(machines))
    print("Loaded", len(machines), "machines from instances.json.")

    isRunning = True
    while isRunning:
        print_menu()
        choice = input("\nChoose an option: ")

        if choice == "1":
            list_machines(machines)
        elif choice == "2":
            add_machine(machines)
        elif choice == "3":
            serializer.Save(machines)
            print("\nMachines saved successfully.")
        elif choice == "4":
            print("Exiting...")
            logger.info("Exiting the Machine Manager.")
            isRunning = False
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
