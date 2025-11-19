# Example machine configurations Testing
# Arrange
machine_configs = [
  {"name": "web-server", "cpu": 4, "ram": 16},
  {"name": "db-server", "cpu": 8, "ram": 32},
  {"name": "cache-server", "cpu": 2, "ram": 8},
]

creator = NewMachineCreator()
machines = []

# Act
for config in machine_configs:
  machine = creator.create_machine(
    name=config["name"],
    cpu=config["cpu"],
    ram=config["ram"]
  )
  print(machine.schema())
  
  machines.append(machine)
    
# Assert
  assert len(machines) == 3
  assert machines[0].name == "web-server"
  assert machines[0].cpu == 4
  assert machines[0].ram == 16
  assert machines[1].name == "db-server"
  assert machines[1].cpu == 8
  assert machines[1].ram == 32
  assert machines[2].name == "cache-server"
  assert machines[2].cpu == 2
  assert machines[2].ram == 8