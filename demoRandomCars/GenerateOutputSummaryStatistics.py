# -*- coding: utf-8 -*-
"""
Summary output statistics

"""
import xml.etree.ElementTree as ET
import pandas as pd

#Get into xml file
path1 = 'C:\\Users\\Gabriel\\Documents\\GitHub\\SUMO Sergio-Gabriel\\TrafficSimulatorAI\\demoRandomCars\\output\\Statistics.xml'
path2 = "/Users/sergio/sergioData/Everis2019/SUMO/demoRandomCars/output/Statistics.xml"


tree = ET.parse(path2)
root = tree.getroot()


columns = ['time', 'loaded', 'inserted', 'running','waiting','ended','arrived','collisions','teleports','halting','meanWaitingTime','meanTravelTime','meanSpeed','meanSpeedRelative','duration']

#Create Panda DataFrame
data = pd.DataFrame(columns=(columns))

for child in root:
    data.loc[len(data)]=[child.attrib['time'],child.attrib['loaded'],child.attrib['inserted'],child.attrib['running'],child.attrib['waiting'],child.attrib['ended'],child.attrib['arrived'],child.attrib['collisions'],child.attrib['teleports'],child.attrib['meanWaitingTime'],child.attrib['meanTravelTime'],child.attrib['meanSpeed'],child.attrib['halting'],child.attrib['meanSpeedRelative'],child.attrib['duration']]

print(data)

#Export csv
output_path1 = r'C:\\Users\\Gabriel\\Documents\\GitHub\\SUMO Sergio-Gabriel\\TrafficSimulatorAI\\demoRandomCars\\csv\\Statistics.csv'
output_path2 = "/Users/sergio/sergioData/Everis2019/SUMO/demoRandomCars/csv/Statistics.csv"
export_csv = data.to_csv (output_path2, index = None,sep=',',header=True) #Don't forget to add '.csv' at the end of the path
