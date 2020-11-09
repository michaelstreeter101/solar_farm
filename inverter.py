# Original author: MWS
# Creation date: 2020-11-09
# Version 1: creates the object with some pre-defined charateristics
class Inverter:
    def __init__(self, id : int):
        self.inverter_id = id

        # PV Inverter Specifications:
        self.rating_KVA : int = 250 # KVA 
        self.efficiency : int = 90 # % 
        self.input_dc_volts : int = 864 # Volts DC 
        self.input_dc_current : int = 500 # Amps 
        # Output AC voltage: 240 V ac (phase voltage) 240 V ac (line voltage) 
        # No. of Phases: 3-φ 
        # Type: GEC [grid export condition] 
        self.pv_string : list = [] # NB: most inverters have one PV String attached, but can have 2 strings

    def __str__(self):
        return f"{self.inverter_id=}"

