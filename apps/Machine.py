import logging
from pydantic import BaseModel
from typing import Optional

logger = logging.getLogger(__name__)


class Machine(BaseModel):

    id: int
    name: str
    status: str = "offline"

    ip: Optional[str] = None

    operating_system: str = "Linux"
    cpu_cores: int = 4
    ram_gb: int = 16


    def __str__(self):

        description = f"Machine ID: {self.id}"
        description += f"\nName: {self.name}"
        description += f"\nIP Address: {self.ip}"
        description += f"\nOperating System: {self.operating_system}"
        description += f"\nCPU Cores: {self.cpu_cores}"
        description += f"\nRAM (GB): {self.ram_gb}"
        description += f"\nStatus: {self.status}"

        return description
