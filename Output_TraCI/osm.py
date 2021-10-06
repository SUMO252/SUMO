import os, sys
import time

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:   
    sys.exit("please declare environment variable 'SUMO_HOME'")
    
import traci
import traci.constants

sumoCmd = ["sumo-gui", "-c", "osm.sumocfg", "--start"]
traci.start(sumoCmd)

print("Starting SUMO")
traci.gui.setSchema("View #0", "real world")

j = 0;

while(j<160):
    time.sleep(0.5);
    traci.simulationStep();
    
    vehicles=traci.vehicle.getIDList();
    if (j%10)==0: #every 10 sec

        for i in range(0,len(vehicles)): 
            # actual speed, emission and, total distance travelled of vehicles
            print("Speed ", vehicles[i], ": ",traci.vehicle.getSpeed(vehicles[i]), " m/s")
            print("CO2Emission ", vehicles[i], ": ", traci.vehicle.getCO2Emission(vehicles[i]), " mg/s")
            print("COEmission ", vehicles[i], ": ", traci.vehicle.getCOEmission(vehicles[i]), " mg/s")
            print("HCEmission ", vehicles[i], ": ", traci.vehicle.getHCEmission(vehicles[i]), " mg/s")
            print("PMxEmission ", vehicles[i], ": ", traci.vehicle.getPMxEmission(vehicles[i]), " mg/s")
            print("NOxEmission ", vehicles[i], ": ", traci.vehicle.getNOxEmission(vehicles[i]), " mg/s")
            print("EdgeID of veh ", vehicles[i], ": ", traci.vehicle.getRoadID(vehicles[i]))
            print('Distance ', vehicles[i], ": ", traci.vehicle.getDistance(vehicles[i]), " m")
        
    j = j+1;

traci.close()
sys.stdout.flush()


