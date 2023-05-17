# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_admin_0_countries.shp'
points = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_populated_places.shp'
airports = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_airports.shp'
Roads = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_roads.shp'
Ports = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_ports.shp'
output = r'E:\8th Semester\GIS\GIS Application\Output'

# 1- List all data we’re working with and show them on ArcMap
arcpy.env.workspace = r'E:\8th Semester\GIS\GIS Application\Data'
feature_list = arcpy.ListFeatureClasses()
print (feature_list)
