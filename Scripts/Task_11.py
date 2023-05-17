import arcpy

#arcpy.env.overwriteOutput = True

countries = r'E:\8th Semester\GIS\GIS Application\Data\ne_10m_admin_0_countries.shp'
arcpy.MakeFeatureLayer_management(countries, 'countries_layer')

with arcpy.da.SearchCursor("countries_layer", ["NAME", "FEATURECLA"]) as cursor:
    for x in cursor:
        # Print the name and type of place for each record
        print(x[0] +" : "+ x[1])