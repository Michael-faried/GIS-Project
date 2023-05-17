# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_admin_0_countries.shp'
airports = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_airports.shp'
Roads = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_roads.shp'
output = r'E:\8th Semester\GIS\GIS Application\Output\Task3_output'

# 3- Create a shapefile for roads in “Asia” continent + Print their number in Pycharm
arcpy.MakeFeatureLayer_management(Roads, 'Roads_Layer', """  "continent"='Asia'""")
arcpy.MakeFeatureLayer_management(countries, 'country_layer')
arcpy.SelectLayerByLocation_management('Roads_Layer', 'WITHIN', 'country_layer')
arcpy.FeatureClassToFeatureClass_conversion('Roads_Layer', output, 'Asia Roads')
# Get the count of the features in the shapefile
count = arcpy.GetCount_management('Roads_Layer')
print("Number of Roads In Asia = " + str(count))
