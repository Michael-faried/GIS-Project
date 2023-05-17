# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_admin_0_countries.shp'
points = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_populated_places.shp'
airports = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_airports.shp'
Roads = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_roads.shp'
Ports = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_ports.shp'
output = r'E:\8th Semester\GIS\GIS Application\Output\Task2_output'


# 2- Create a shapefile for countries that have “military” airports + Print them in Pycharm
arcpy.MakeFeatureLayer_management(airports, 'Airports_layer', """ "type" IN ('military', 'major and military', 'mid and military', 'military mid') """)
arcpy.MakeFeatureLayer_management(countries, 'country_layer')
arcpy.SelectLayerByLocation_management('country_layer', 'INTERSECT', 'Airports_layer')
arcpy.FeatureClassToFeatureClass_conversion('country_layer', output, 'Countries_Militaries_Airports')
with arcpy.da.SearchCursor('E:\8th Semester\GIS\GIS Application\Output\Task2_output\Countries_Militaries_Airports.shp', ['NAME']) as cursor:
    for row in cursor:
        print(row[0])
