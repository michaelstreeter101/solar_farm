# Original author: MWS
# Creation date: 2020-11-09
# Version 1: creates the object with some pre-defined charateristics
class PvModule:
    def __init__(self, id : int):
        self.panel_id = id

        # PV panel specification attributes
        # MPP description: https://en.wikipedia.org/wiki/Maximum_power_point_tracking
        # Note: the MPP amps, volts, and watts do not all happen under the same conditions.
        # All modules are rated by manufacturers in terms of their peak power (Wp) under standard test conditions: 
        # ie. 1000W/m² of sunlight (‘peak sun’); 25 ºC; and air mass of 1.5, so P ≠ IV here!
        self.mppV = 360 # Volts
        self.mppI = 9.95 # Amps
        self.pmax = 220 # Watts. 
        self.type = 'Monocrystalline'
        self.efficiency = 14.3 # % 

        # Normal operating temperature: Min 15 ºC and Max 40 ºC 
        self.temp = 15 # ºC

        # Dimensions of single module(mm) 
        self.length = 1655 # mm
        self.width = 995 # mm
        self.thickness = 50 # mm
        self.area = self.length * self.width
        # NB: Area of single panel = 1646725 (mm²) = 1.64 meter² 

        self.angle = 35 # (slope) of PV Module: 35 degrees
        # NB: In the UK the optimum slope for solar panels is 30 to 40 degrees. 
        # This is due to the fact that the angle of the sun is 50 to 60 degrees, 
        # which when combined with a 30 to 40 degree slope creates a 90 degree angle; 
        # providing the highest level of solar radiation.

        self.wind_speed_rating = 150 # Km/h 
        self.mounting = 'Fixed'

    def __str__(self):
        return f"{self.panel_id=}"
