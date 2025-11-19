from pydantic import BaseModel, Field
from typing import Optional

class Machine(BaseModel):
  id: int
  name: str
  status: str = "offline" # can be offline/online/maintenance
  
  ip : Optional[str]
  
  operating_system: str = "Linux"
  cpu_cores: int = 4
  ram_gb: int = 16 
  
  # dunder (double under) functions region
  def __init__(self, id: int, name: str, status: str):
      self.id = id
      self.name = name
      self.status = status  
  
  def __str__(self):
      description = f"Machine ID: {self.id}"
      description += f"\nName: {self.name}"
      description += f"\nIP Address: {self.ip}" 
      description += f"\nOperating System: {self.operating_system}"
      description += f"\nCPU Cores: {self.cpu_cores}"
      description += f"\nRAM (GB): {self.ram_gb}"
      description += f"\nStatus: {self.status}"
      return description
          
  # endregion
  