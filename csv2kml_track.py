import csv
#Input the file name."JoeDupes3_forearth"
fname = input("Enter file name WITHOUT extension: ")
data = csv.reader(open(fname + '.csv'), delimiter = ',')
#Skip the 1st header row.
#data.next()
#Open the file to be written.
f = open(fname + '.kml', 'w')

#Writing the kml file.
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
f.write("<Document>\n")
f.write("   <name>" + fname + '.kml' +"</name>\n")
f.write("<Style id=\"gv_track\"\n")
f.write(" <LineStyle> <color>ff0000e6</color> <width>4</width> </LineStyle>\n")
f.write("</Style>\n")
f.write("<MultiGeometry>\n")
f.write("<LineString>\n")
f.write("<tessellate>1</tessellate>\n")
f.write("<altitudeMode>clampToGround</altitudeMode>\n")
f.write("<coordinates>")
for row in data:
    f.write( str(row[0]) + "," + str(row[1]) + "," + str() ) 

f.write("</coordinates>\n")
f.write("</MultiGeometry>")

f.write("</Document>\n")
f.write("</kml>\n")
print ("File Created. ")
print ("Press ENTER to exit. ")
input()
f.close()
