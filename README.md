# TrafficSimulatorAI
El objetivo de este proyecto es poder reducir el tiempo de espera de los coches 
en un cruce de semáforos gracias al control automático del estado de estos mismos,
de tal manera que ellos sean capaces por si solo de ir modificándose según el tráfico
que se acumule en la carretera.

1.GENERACIÓN DE LA RED
1.1.Configuración de la red
netconvert --node-files my_nodes.nod.xml -- edge-files my_edge.edg.xml -t my_type.type.xml -o my_net.net.xml

1.2.Configuración de la ruta aleatoria de coches en nuestra red
python randomTrips.py -n ./simple.net.xml

1.3.Archivo de configuración
sumo-gui config.sumocfg

2.GENERACIÓN DE ESTADÍSTICAS
sumo -c config.sumocfg –summary <FILEOUTPUT>

3.TRACI
python “No Reinforcement Learning”/testTracy.py

4.REINFORCEMENT LEARNING
4.1. Q-Learning
python "Reinforcement Learning"/QL/Ql_2way_intersection.py
4.1.1 Plots:
  a.Tiempo total de espera por coche por step:
  python "Reinforcement Learning"/Plots/plot.py -f "Reinforcement Learning"/QL/Outputs -out "Reinforcement Learning"/QL/Plots/Total_Waiting_Time_Per_Vehicle_Per_Step
  b.Tiempo total de espera de todos los coches por step:
  python "Reinforcement Learning"/Plots/plot2.py -f "Reinforcement Learning"/A2C/Outputs -out "Reinforcement Learning"/A2C/Plots/Total_Waiting_Time_Of_Vehicles

4.2.A2C
python "Reinforcement Learning"/A2C/A2C_2way_intersection.py
4.2.1.Plots:
  a.Tiempo total de espera por coche por step:
  python "Reinforcement Learning"/Plots/plot.py -f "Reinforcement Learning"/A2C/Outputs -out "Reinforcement Learning"/A2C/Plots/Total_Waiting_Time_Per_Vehicle_Per_Step
  b.Tiempo total de espera de todos los coches por step:
  python "Reinforcement Learning"/Plots/plot2.py -f "Reinforcement Learning"/A2C/Outputs -out "Reinforcement Learning"/A2C/Plots/Total_Waiting_Time_Of_Vehicles
