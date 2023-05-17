# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_admin_0_countries.shp'
Ports = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_ports.shp'
output = r'E:\8th Semester\GIS\GIS Application\Output\Task4_output'

# 4- Create a shapefile for ports in countries (Italy, Spain, France)
arcpy.MakeFeatureLayer_management(Ports, 'Ports_Layer')
arcpy.MakeFeatureLayer_management(countries, 'country_layer', """ "NAME" IN ('Italy','Spain','France') """)
arcpy.SelectLayerByLocation_management('Ports_Layer', 'INTERSECT', 'country_layer')
arcpy.FeatureClassToFeatureClass_conversion('Ports_Layer', output, 'Ports In Italy_Spain_France')
