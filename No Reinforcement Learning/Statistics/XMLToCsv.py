
import xml.etree.ElementTree as ET
import pandas as pd

#Get into xml file
path2 = "./demoRandomCars/output/tripinfo.xml"


tree = ET.parse(path2)
root = tree.getroot()
columns = root[0].attrib.keys()


#Create Panda DataFrame
data = pd.DataFrame(columns=(columns))


for child in root:
    atts = []
    for c in columns:
        atts.append(child.attrib[c])
    data.loc[len(data)]= atts

# print(data)

#Export csv
output_path2 = "./demoRandomCars/csv/tl.csv"
export_csv = data.to_csv (output_path2, index = None,sep=',',header=True) #Don't forget to add '.csv' at the end of the path
