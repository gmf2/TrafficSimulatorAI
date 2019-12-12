# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:16:42 2019

@author: Gabriel
"""

from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
#print('hello')
#Tools SUMO
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)				
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # Checks for the binary in environ vars
import traci




def run():
    print('hello')
#        """execute the TraCI control loop"""
    step = 0
    #Phase 1:North
    #Phase 2:East
    #Phase 3:South
    #Phase 4:West
    print('phase{}'.format(traci.trafficlight.getPhase('n1')))
    traci.trafficlight.setPhase("n1", 2)
#    print('eu')
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        #Traffic light in Phase 0: (Initial)
        print('phase cond:{}'.format(traci.trafficlight.getPhase("n1") ==0))
        if traci.trafficlight.getPhase("n1") ==0:
            # we are not already switching
            print((traci.inductionloop.getLastStepVehicleNumber("loop2_0") > 0) or (traci.inductionloop.getLastStepVehicleNumber("loop2_1") > 0) or (traci.inductionloop.getLastStepVehicleNumber("loop3_0") > 0) or (traci.inductionloop.getLastStepVehicleNumber("loop3_1") > 0))
            #If there are more than one vehicle through west or east, switch
            if (traci.inductionloop.getLastStepVehicleNumber("loop2_0") > 0) or (traci.inductionloop.getLastStepVehicleNumber("loop2_1") > 0) or (traci.inductionloop.getLastStepVehicleNumber("loop3_0") > 0) or (traci.inductionloop.getLastStepVehicleNumber("loop3_1") > 0)  :
                # there is a vehicle from the east or weast, switch
                traci.trafficlight.setPhase("n1", 2)
            else:
                # otherwise try to keep green for north or south
                traci.trafficlight.setPhase("n1", 1)  
        print('Setphase{}'.format(traci.trafficlight.getPhase('n1')))
        #Traffic light in Phase 1 or 3 :(North or South)
        if traci.trafficlight.getPhase("n1") ==1 or traci.trafficlight.getPhase("n1") ==3 :
            # we are not already switching
            if (traci.inductionloop.getLastStepVehicleNumber("loop2_0") > 0) or (traci.inductionloop.getLastStepVehicleNumber("loop2_1") > 0) or (traci.inductionloop.getLastStepVehicleNumber("loop3_0") > 0) or (traci.inductionloop.getLastStepVehicleNumber("loop3_1") > 0)  :
                # there is a vehicle from the east or weast, switch
                traci.trafficlight.setPhase("n1", 2)
            else:
                # otherwise try to keep green for north or south
                traci.trafficlight.setPhase("n1",3)
        step += 1
    traci.close()
    sys.stdout.flush()


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()
    print('ok')

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, "-c", "./Net/config.sumocfg",
                             "--tripinfo-output", "./Net/Output/NRL/tripinfoTracy.xml"])
    run()
