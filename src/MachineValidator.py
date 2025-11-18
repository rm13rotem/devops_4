import Machine  

class MachineValidator:
    
  Machine machine
  
  def __init__(self, machine):
    self.machine = machine
      
    
  def IsValidId(input : str) -> bool:
    try:
      val = int(input)
      if (val > 0):
        return True
      else:
        return False  
    except ValueError:
      return False
    except Exception:
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
      except Exception:
        return False
    return True
  
  def Validate(self) -> bool:
    return (self.IsValidId(str(self.machine.id)) and
            self.IsValidName(self.machine.name) and
            self.IsValidStatus(self.machine.status) and
            self.IsValidIp(self.machine.ip))