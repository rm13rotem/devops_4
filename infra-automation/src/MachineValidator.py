#from Machine import Machine

class MachineValidator:
     
    @staticmethod
    def IsValidId(input: str) -> bool:
      try:
        val = int(input)
        return val > 0
      except Exception:
        return False
      
    @staticmethod
    def IsValidName(input: str) -> bool:
      return len(input) > 0 and len(input) <= 50
    
    @staticmethod
    def IsValidStatus(input: str) -> bool:
      valid_statuses = ["online", "offline", "maintenance"]
      return input in valid_statuses  
    
    @staticmethod
    def IsValidIp(txt: str) -> bool: 
      parts = txt.split(".")
      if len(parts) != 4:
        return False
      for part in parts:
        try:
          val = int(part)
          if val < 0 or val > 255:
            return False
        except Exception:
          return False
      return True
    
    @staticmethod
    def Validate(self) -> bool:
      return (self.IsValidId(str(self.machine.id)) and
          self.IsValidName(self.machine.name) and
          self.IsValidStatus(self.machine.status) and
          self.IsValidIp(self.machine.ip))
  
     
    
  