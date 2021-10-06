import xml.etree.cElementTree as ET
import os
import pandas as pd
import pandasql
from datetime import date
#change directory
os.chdir ('D:\Emissions_scenario')


tree = ET.ElementTree(file='emission.xml')
root=tree.getroot()

#list containing column names in list
columns = ["time", "vehicle_id", "eclass", "CO2", "CO", "HC", "NOx", "PMx", "fuel", "electricity", "noise", "route", "type", "waiting", "lane", "pos", "speed", "angle", "x","y"]

#creating data frame
df1 = pd.DataFrame(columns = columns)
rowcount=0
for node in root:
    time =int(float(node.attrib.get("time")))
    
    
    for child in node:
        vehicle_id = child.attrib.get("id")
        eclass = child.attrib.get("eclass")        
        CO2 = child.attrib.get("CO2")
        CO = child.attrib.get("CO")
        HC = child.attrib.get("HC")    
        NOx = child.attrib.get("NOx")    
        PMx = child.attrib.get("PMx")    
        fuel = child.attrib.get("fuel")
        electricity = child.attrib.get("electricity")
        noise = child.attrib.get("noise")
        route = child.attrib.get("route")
        V_type = child.attrib.get("type")
        waiting = child.attrib.get("waiting")
        lane = child.attrib.get("lane")
        pos = child.attrib.get("pos")
        speed = child.attrib.get("speed")
        angle = child.attrib.get("angle")
        x = child.attrib.get("x")
        y = child.attrib.get("y")
        df1 = df1.append(pd.Series([time,vehicle_id,eclass,CO2,CO,HC,NOx,PMx,fuel,electricity,noise,route, V_type,waiting,lane,pos,speed,angle,x,y], index = columns), ignore_index = True)
        
df2=pandasql.sqldf("select time,vehicle_id,speed,CO2,CO,HC,NOx,PMx,fuel from df1 where df1.vehicle_id='vehicle_1'")
df2.insert(9, 'ROWCOUNT', range(1,1+len(df2)))
vehID= pandasql.sqldf("select distinct vehicle_id from df2")
VehID=vehID.values[0]
#print(vehID)
today_date=date.today()
#print(today_date)
#if VehID =='veh0':
df3=pandasql.sqldf("select  time ,speed from df2 ")
#else:
df4=pandasql.sqldf("select  ROWCOUNT as time,vehicle_id,speed,CO2,CO,HC,NOx,PMx,fuel from df2 ")
df2.to_csv("Trail.csv",index=False,header=True)
df3.to_csv("Data3"+str(VehID)+str(today_date)+".csv",index=False,header=False)
df4.to_csv("Egovehicle"+str(VehID)+".csv",index=False,header=True)



