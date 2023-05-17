# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_admin_0_countries.shp'
points = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_populated_places.shp'
output = r'E:\8th Semester\GIS\GIS Application\Output\Task5_output'

#5- Create a shapefile for all Arabic cities using 2 methods ( Multiple Selections - If Condition )

# Multiple Selections Method
arabic_countries = ['Algeria', 'Bahrain', 'Comoros', 'Djibouti', 'Egypt', 'Iraq', 'Jordan', 'Kuwait',
                    'Lebanon', 'Libya', 'Mauritania', 'Morocco', 'Oman', 'Palestine', 'Qatar', 'Saudi Arabia',
                    'Somalia', 'Sudan', 'Syria', 'Tunisia', 'United Arab Emirates', 'Yemen']
arcpy.MakeFeatureLayer_management(points, 'Points_Layer')
for i in arabic_countries:
    arcpy.MakeFeatureLayer_management(countries, 'country_layer', """ "NAME" ='{}' """.format(i))
    arcpy.SelectLayerByLocation_management('Points_Layer', 'WITHIN', 'country_layer')
    arcpy.FeatureClassToFeatureClass_conversion('Points_Layer', output, '{} Cities'.format(i))

# MAKE JUST ONE ShapeFile HAS ALL Arabic Countries
arcpy.MakeFeatureLayer_management(countries, 'country_layer', """ "NAME" IN {} """.format(tuple(arabic_countries)))
arcpy.SelectLayerByLocation_management('Points_Layer', 'WITHIN', 'country_layer')
arcpy.FeatureClassToFeatureClass_conversion('Points_Layer', output, 'Arabic cities')


# # If Condition Method
# arabic_countries = ['Algeria', 'Bahrain', 'Comoros', 'Djibouti', 'Egypt', 'Iraq', 'Jordan', 'Kuwait',
#                     'Lebanon', 'Libya', 'Mauritania', 'Morocco', 'Oman', 'Palestine', 'Qatar', 'Saudi Arabia',
#                     'Somalia', 'Sudan', 'Syria', 'Tunisia', 'United Arab Emirates', 'Yemen']
# arcpy.MakeFeatureLayer_management(points, 'Points_Layer')
# arcpy.MakeFeatureLayer_management(countries, 'country_Layer')
# with arcpy.da.SearchCursor('country_Layer', ['NAME']) as countries_cursor:
#     for x in countries_cursor:
#         if x[0] in arabic_countries:
#             arcpy.MakeFeatureLayer_management(countries, 'country_layer', """ "NAME" ='{}' """.format(x[0]))
#             arcpy.SelectLayerByLocation_management('Points_Layer', 'WITHIN', 'country_layer')
#             arcpy.FeatureClassToFeatureClass_conversion('Points_Layer', output, '{}'.format(x[0]))
#
