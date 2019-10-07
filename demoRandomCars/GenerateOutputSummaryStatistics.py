# -*- coding: utf-8 -*-
"""
Summary output statistics

"""
import xml.etree.ElementTree as ET
import pandas as pd

#Get into xml file
tree = ET.parse('C:\\Users\\Gabriel\\Documents\\GitHub\\SUMO Sergio-Gabriel\\TrafficSimulatorAI\\demoRandomCars\\Statistics.xml')
root = tree.getroot()

#Create Panda DataFrame
data = pd.DataFrame(columns=('time', 'loaded', 'inserted', 'running','waiting','ended','arrived','collisions','teleports','halting','meanWaitingTime','meanTravelTime','meanSpeed','meanSpeedRelative','duration'))

for child in root:
    data.loc[len(data)]=[child.attrib['time'],child.attrib['loaded'],child.attrib['inserted'],child.attrib['running'],child.attrib['waiting'],child.attrib['ended'],child.attrib['arrived'],child.attrib['collisions'],child.attrib['teleports'],child.attrib['meanWaitingTime'],child.attrib['meanTravelTime'],child.attrib['meanSpeed'],child.attrib['halting'],child.attrib['meanSpeedRelative'],child.attrib['duration']] 

#Export csv    
export_csv = data.to_csv (r'C:\\Users\\Gabriel\\Documents\\GitHub\\SUMO Sergio-Gabriel\\TrafficSimulatorAI\\demoRandomCars\\Statistics.csv', index = None,sep=',',header=True) #Don't forget to add '.csv' at the end of the path
    