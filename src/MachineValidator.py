class MachineValidator:
  def __init__(self, Machine machine):
    self.machine = machine
      
    
  def IsValidId(input : str) -> bool:
    try:
      val = int(input)
      return val > 0
    except ValueError:
      return False
    
    
  def IsValidName(input : str) -> bool:
    return len(input) > 0 and len(input) <= 50
  
  def IsValidStatus(input : str) -> bool:
    valid_statuses = ["online", "offline", "maintenance"]
    return input in valid_statuses  
  def IsValidIp(input : str) -> bool: 
    parts = input.split(".")
    if len(parts) != 4:
      return False
    for part in parts:
      try:
        val = int(part)
        if val < 0 or val > 255:
          return False
      except ValueError:
        return False
    return True
  def Validate(self) -> bool:
    return (self.IsValidId(str(self.machine.id)) and
            self.IsValidName(self.machine.name) and
            self.IsValidStatus(self.machine.status) and
            self.IsValidIp(self.machine.ip))