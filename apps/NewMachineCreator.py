import logging
from MachineValidator import MachineValidator
from Machine import Machine

class NewMachineCreator:
  @staticmethod
  def getNewMachine() -> Machine:
    
    print("let's create a new machine")
    isValid = False
    while not isValid:
      try:            
          id = input("Enter machine Id:")
          name = input("Enter machine Name:")
          status = input("Enter machine status (online/offline/maintenance):") 
          machine = Machine(id, name, status)
          
          isValid = MachineValidator.isValidMachine(machine)
          if not isValid:
            print("The machine you entered is not valid, please try again.")
            continue
          ip = input("Enter machine IP (xx.xx.xx.xx):")
          if (MachineValidator.IsValidIp(ip)):
            machine.ip = ip 
          else: 
            print("The IP you entered is not valid, setting to default")
            machine.ip = "192.168.1.1"
          
          newOs = input("Enter operating system (default Linux):")
          if (newOs.strip() != ""):
            machine.operating_system = newOs  
          
          newCpu = input("Enter number of CPU cores (default 4):")
          if (newCpu.strip() != ""):
            machine.cpu_cores = int(newCpu)
          
          newRam = input("Enter amount of RAM in GB (default 16):")
      except Exception as e:
        print("An error occurred while creating the machine:", e)
        logger.error("Error in NewMachineCreator.getNewMachine: %s", e)
        isValid = False 
        print("An error occurred while creating the machine:", e)
        logger.error("Error in NewMachineCreator.getNewMachine: %s", e)
        isValid = False 
        
    return machine  

