from dataclasses import dataclass

class Arduino_Uno:
    procesamiento_datos: input()
    Programa: input()
    def Encender_Apagar(Contraseña:str) -> bool:
      n = input()
      if n == "1234":
        return True
      else:
        return False
class Laser:
    Estado: bool
    info_Arduino: Arduino_Uno
    def Encender_Apagar(): 
      if self.info_Arduino.Encender_Apagar == True:
        self.Estado = True
      elif self.info_Arduino.Encender_Apagar == False:
        self.Estado = False
      return self.Estado
class Fotocelda:
    Estado: bool
    info_laser: Laser
    info_Arduino: Arduino_Uno
    def luz_Laser():
      if self.info_laser.Encender_Apagar == True and self.info_Arduino.Encender_Apagar == True:
        if self.Estado == True:
          return True
      elif self.info_laser.Encender_Apagar == False and self.info_Arduino.Encender_Apagar == True:
        if self.Estado == False:
          return False
class Buzzer:
    Estado: bool
    info_Fotocelda: Fotocelda
    info_Arduino: Arduino_Uno
    def Encender_Apagar():
      if self.info_Arduino.Encender_Apagar == True and self.info_Fotocelda.luz_Laser == False:
        self.Estado = True
      elif self.info_Arduino.Encender_Apagar == False and self.info_Fotocelda.luz_Laser == True:
        self.Estado = False
      return self.Estado
