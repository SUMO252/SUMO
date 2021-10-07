# SUMO
Traffic Simulation

# SUMO_Assignment File

Osm.net.xml - Consist of information of all the lanes, junctions, and others in the map imported from Open Street Map.
<br /> Route1_rou.xml - The route of vehicles, trips, stops, etc.
<br /> Pedestrains.rou.xml - Information regarding the pedestrian's route and type.
<br /> Additional.add.xml - This file consists of added bus spots in the network.
<br /> osm.sumocfg - This file takes the input from all the above-mentioned files to run the simulation accordingly. The vehicle_0(Yellow) picks up two passengers and, vehicle_1 (Red) picks up three passengers.

# Output_SUMO

output.xml - This is an FCD-export file, which consists of all the information of the simulation for each time step(ID, Position, Speed, Edge).
<br /> emission.xml - This file consists of all the information regarding the emission for each vehicle id (CO2, CO, HC, NOx, PMx ).
<br /> junction.poly.xml - This is a vehicle type probe file, which gives output file(vehicle_0.xml, vehicle_1.xml) the information for a particular vehicle id with Speed, Position, Time Step.

# Output_Python

Output_script.py - This is a python file with code to create an Excel file(vehicle_0.csv, vehicle_1.csv) with emission data for all the time steps (CO2, CO, HC, NOx, PMx, Fuel).

# Output_TraCI

osm.py - This file gives the output of Speed, CO2, CO, HC, NOx, PMx, Duration for all the time steps during the simulation using the Traci function.
