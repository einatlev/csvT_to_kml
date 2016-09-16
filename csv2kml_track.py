import sys
import csv
#Input the file name."JoeDupes3_forearth"
#fname = input("Enter file name WITHOUT extension: ")
#get file name from command line arument
fname = str(sys.argv[1])

data = csv.reader(open(fname + '.csv'), delimiter = ',')
#Skip the 1st header row.
#data.next()
#Open the file to be written.
f = open(fname + '.kml', 'w')

#Writing the kml file.

f.write("<?xml version=\"1.0\" standalone=\"yes\"?>\n")
f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n")
f.write("<Document>\n")
f.write("    <name><![CDATA[test]]></name>\n")
f.write("    <visibility>1</visibility>\n")
f.write("    <open>1</open>\n")
f.write("    <Style id=\"gv_track\">\n")
f.write("      <LineStyle>\n")
f.write("        <color>00ff00e6</color>\n")
f.write("        <width>4</width>\n")
f.write("      </LineStyle>\n")
f.write("    </Style>\n")
f.write("    <Folder id=\"Tracks\">\n")
f.write("      <name>Tracks</name>\n")
f.write("      <visibility>1</visibility>\n")
f.write("      <open>0</open>\n")
f.write("      <Placemark>\n")
f.write("        <description><![CDATA[&nbsp;]]></description>\n")
f.write("        <styleUrl>#gv_track</styleUrl>\n")
f.write("        <Style>\n")
f.write("          <LineStyle>\n")
f.write("            <color>ff0000e6</color>\n")
f.write("            <width>4</width>\n")
f.write("          </LineStyle>\n")
f.write("        </Style>\n")
f.write("        <MultiGeometry>\n")
f.write("          <LineString>\n")
f.write("            <tessellate>1</tessellate>\n")
f.write("            <altitudeMode>clampToGround</altitudeMode>\n")
f.write("<coordinates>")

header = data.next()
for row in data:
	f.write( str(row[0]) + "," + str(row[1]) + str() + "\n" )

f.write("</coordinates>")
f.write("          </LineString>\n")
f.write("        </MultiGeometry>\n")
f.write("      </Placemark>\n")
f.write("    </Folder>\n")
f.write("  </Document>\n")
f.write("</kml>")
f.close()

print ("File Created. ")
print ("Press ENTER to exit. ")

