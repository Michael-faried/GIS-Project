# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
airports = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_airports.shp'


# 6- Using Search Cursor print the name, location & wikipedia for all airports which are major
arcpy.MakeFeatureLayer_management(airports, 'Airports_layer')
where_clause = "type = 'major'"
with arcpy.da.SearchCursor('Airports_layer', ['name', 'location', 'wikipedia', 'type'], where_clause) as airports_cursor:
    for x in airports_cursor:
        print(u"Airport name: {}".format(x[0]).encode('utf-8'))
        print(u"Location: {}".format(x[1]).encode('utf-8'))
        print(u"wikipedia: {}".format(x[2]).encode('utf-8'))
        # print x[3]
        print ""
