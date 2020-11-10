# Original author: MWS
# Creation date: 2020-10-26
# Version 2: creates 20 inverters, each with a string of 940 panels, and 4 extra strings of 940 panels,
#            then prints out every panel unique id.
# Purpose: flesh out some ideas for the objects required by SCADA
import math
import pyrometer
import inverter
import pvmodule

# Power Plant Specification
# Number of modules: 22560  
# Number of modules per MW: 4512  (NB: 22560 modules ÷ 4512 modules/MW = 5MW, and 22560 modules x 220W per module = 5MW)
# Detail of series/parallel combination: 24 strings in series; 940 panels (in parallel) in each string.

''' def make_string( string_id : int ) -> range:
    # Make a string of pv_arrays...
    # Should this be a function in pvmodule? It doesn't belong here, but I don't think it's a method of the class either!
    pv_string : list = []
    numbers : range = range(940)
    # print( f"{type(numbers)=}" )
    for number in numbers:
        pv_string.append( pvmodule.PvModule( id = (string_id * 940) + number ) )
    return pv_string
 '''

# Make a test inverter to experiment
i0 = inverter.Inverter( id = 0 )
#p0 = pvmodule.PvModule( id = 0 )
print( type( i0 ))
i0.pv_string.append( pvmodule.PvModule().make_string( 0 ) ) # One pv_string.
i0.pv_string.append( pvmodule.PvModule().make_string( 1 ) ) # A second pv_string.
print( i0.pv_string[1][1] )
print( f"{i0.pv_string[1][1].temp=}" )
i0.pv_string[1][1].temp = 20
print( f"{i0.pv_string[1][1].temp=}")

# No of inverters: 20.
pv_inverter : list = []
#inverters : range = 
for inverter1 in range(20):
    pv_inverter.append( inverter.Inverter( id = inverter1 ) ) # Each inverter has a unique id number 0-19.
    print( "Inverter "+str(pv_inverter[inverter1].inverter_id), " - make_string( "+str(inverter1)+" )" )
    pv_inverter[inverter1].pv_string.append( pvmodule.PvModule().make_string( inverter1 ) ) # One pv_string.
    k = input( 'Hit [enter]' )

# Note: most inverters have one PV String attached, but not all because there are 24 PV Strings.
for inverter2 in range(16, 20):
    print( "Inverter " + str(pv_inverter[inverter2].inverter_id), " - make_string( "+str(inverter2 + 4 ) + " )" )
    pv_inverter[inverter2].pv_string.append( pvmodule.PvModule().make_string( inverter2 + 4 ) ) # A second pv_string.
    k = input( 'Hit [enter]' )

# ===== TEST: every pv_array should have a unique id
'''for inverter1 in range(20):
    print( f"{pv_inverter[inverter1].inverter_id=}" )
    for module1_count in pv_inverter[inverter1].pv_string[0]:
        print( module1_count.panel_id )
    k = input( str(inverter1) )
for inverter2 in range(16, 20):
    print( f"{pv_inverter[inverter1].inverter_id=}" )
    for module2_count in pv_inverter[inverter2].pv_string[1]:
        print( module2_count.panel_id )
    k = input( str(inverter2) ) '''
# END TEST =====

pyrometer = pyrometer.pyrometer()
print( pyrometer )

# OK, lets do some sums
#area = [sigma inverters] string area * strings
pv_area = 0
for i in pv_inverter:
    for s in i.pv_string:
        for m in s:
            pv_area += m.area
pv_area /= 1000000
print( f"{pv_area=} meter² ")
#wattage = area * Gcs * efficiency


# pv_string = make_string(0)
# m = PvModule(1)
# print(f"{m.panel_id=} {m.mppV=} {m.pmax=}")
# print(f"{pv_string[100].pmax=}")