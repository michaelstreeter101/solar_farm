# solar_farm
A simulator for a make-believe solar farm

**File manifest:**
* pvmodule.py - photovoltaic module class
* inverter.py - inverter class
* pyrometer.py - pyrometer class (tells us how much electricity we *expect* the panels to produce)
* Dailydata_lat_lon_month...json - 12 files containing average daily clear sky wattage/M²
* solar.py - puts it all together

**Description**

Based on this real solar farm: https://irjet.net/archives/V4/i8/IRJET-V4I8136.pdf

In industry they are called modules, arrays and strings but we can't call them that because they are programming terms!  Thinking about information needed to define/specify a PV Power Plant from the PDF:
From Figure 1...
* a PV Module is the same thing as a PV Panel.
* a PV String is a collection of PV Modules plus one "combiner"
* an Inverter may have 1 or more PV Strings (https://en.wikipedia.org/wiki/Power_inverter)
* The Inverters are what is controlled by the SCADA system (https://en.wikipedia.org/wiki/SCADA)
* a PV array is a collection of PV Strings (i.e. the array = all the modules, grouped into strings)
* a PV Power Plant is an aggregation including the PV Array, SCADA, LT Switchgear and MV switchgear, Power Transformer (LV to MV), HT Switchyard, Protection and Metering, Transmission lines.

Note we are not bothered about anything in a PV Power Plant above the SCADA system, so while it's nice to know there's a transformer etc. but we don't really care, because that's someone else's department.

**PV panel specification attributes**
* Watt: 220 Watt 
* Voltage: 360 Volts 
* Current: 7.6 A   Note: I can't make amps x volts = watts, even using efficiency. Maybe a physics teacher can explain why the numbers in this table don't add up.
* Type: Monocrystalline 
* Efficiency: 14.3% 
* Temperature: Min 15 ºC and Max 40 ºC 
* Dimensions of single module(mm): 1655(L) × 995(w) × 50(T) mm 
* Area of single panel = 1646725 (mm) 
* Area of single panel = 1.64 meter² 
* Tilt angle(slope) of PV Module: 40 degree 
* Wind speed rating: 150 Km/h 
* Mounting: Fixed Type 

PV Array specification attributes
* Output of the PV array to be connected to the PCU: Nominal 250 KW  (Note: Solar Power Conditioning unit (PCU) is an integrated system consisting of a solar charge controller, inverter and a Grid charger. It provides the facility to charge the battery bank through either a Solar or Grid/DG set. The PCU continuously monitors the state of battery voltage, solar power output and the load.)
* Protective device: 400 Volts under voltage relay

**Inverter Specifications**
* KVA rating: 250 KVA 
* Input DC voltage: 864 Volts DC 
* Input DC current: 500 A 
* Output AC voltage: 240 V ac (phase voltage) 240 V ac (line voltage) 
* No. of Phases: 3-φ 
* Type: GEC [grid export condition] 
* Efficiency: 90-93% 
* No of inverters: 20   Note: most inverters have one PV String attached, but not all because there are 24 PV Strings.

**Power Plant Specification**
* Number of modules: 22560  
* Number of modules per MW: 4512     NB: 22560 modules ÷ 4512 modules/MW = 5MW
* Detail of series/parallel combination: 24 strings in series, 940 panels (in parallel) in a string 

So, putting it all together a SCADA system would show Inverters, Combiners, PV Strings and PV Panels/Modules

Version 1 will define those data structures (static) and display the key attributes for each.

Version 2 would change some attributes and re-display!?

Stretch goal: https://nelhydrogen.com/water-electrolysers-hydrogen-generators/
When electricity is cheaper than H2, make H2
 
