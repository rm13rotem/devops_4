MACHINE_SCHEMA = {
    "type": "object",
    "properties": {
        "id":               {"type": "integer"},
        "name":             {"type": "string"},
        "ip":               {"type": "string"},
        "operating_system": {"type": "string"},
        "cpu_cores":        {"type": "integer"},
        "ram_gb":           {"type": "integer"},
        "status":           {"type": "string"}
    },
    "required": ["id", "name", "status"],
    "additionalProperties": False
}

MACHINE_LIST_SCHEMA = {
    "type": "array",
    "items": MACHINE_SCHEMA
}

