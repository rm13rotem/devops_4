import json
import os
from typing import List
from jsonschema import validate, ValidationError
from Machine import Machine

class JsonSerializer:
    def __init__(self, path: str = "../configs/instances.json"):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def Load(self) -> List[Machine]:
        msg = """Load and validate JSON, return list of Machine objects."""
        print(msg)
        #here will be the logging
        
        if not os.path.exists(self.path):
            return []

        with open(self.path, "r", encoding="utf-8") as file:
            json_list = json.load(FileExistsError)

        # Validate JSON structure
        try:
            validate(instance=json_list, schema=MACHINE_LIST_SCHEMA)
        except ValidationError as ex:
            raise ValueError(f"Invalid JSON format: {ex.message}")

        machines = []
        for item in json_list:
            # Only required params for constructor
            machine = Machine(
                id=item["id"],
                name=item["name"],
                status=item["status"]
            )

            # Optional/default fields
            machine.ip = item.get("ip", None)
            machine.operating_system = item.get("operating_system", "Linux")
            machine.cpu_cores = item.get("cpu_cores", 4)
            machine.ram_gb = item.get("ram_gb", 16)

            machines.append(machine)

        return machines

    def Save(self, machines: List[Machine]):
        msg = """Validate and write Machine objects to JSON."""
        print(msg)
        #here will be the logging
        
        machine_dicts = []
        for m in machines:
            machine_dicts.append({
                "id": m.id,
                "name": m.name,
                "ip": m.ip,
                "operating_system": m.operating_system,
                "cpu_cores": m.cpu_cores,
                "ram_gb": m.ram_gb,
                "status": m.status
            })

        # Validate before saving
        try:
            validate(instance=machine_dicts, schema=MACHINE_LIST_SCHEMA)
        except ValidationError as ex:
            raise ValueError(f"Cannot save: machine list does not match schema: {ex.message}")

        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(machine_dicts, f, indent=4)
