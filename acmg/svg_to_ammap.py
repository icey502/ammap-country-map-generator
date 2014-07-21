#!/usr/bin/env python
from xml.dom import minidom
import fokenizer
import config
import os

# tokens to replace in the AMMAP json file
MAP_NAME_TOKEN = "MAP_NAME"
SVG_PATH_TOKEN = "SVG_PATH_AS_JSON"
MIN_LAT_TOKEN = "MIN_LAT"
MIN_LON_TOKEN = "MIN_LON"
MAX_LAT_TOKEN = "MAX_LAT"
MAX_LON_TOKEN = "MAX_LON"

# the template files
JS_TEMPLATE_FILE = "templates/template-map.js"
HTML_TEMPLATE_FILE = "templates/template-map.html"

class Point:
    """
    Represents a lat-lon pair.
    """
    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
    
class SVG_Figure:
    """
    Represents the bare minimum information that is needed from a Natural-Earth-derived SVG string, to an AMMAP javascript path literal.
    """
    def __init__(self, id, title, region, path, latitude, longitude):
        self.id = id
        self.title = title
        self.region = region
        self.point = Point(latitude, longitude)
        self.pathString = path
     
    def get_point(self):
        return self.point
    
    def __repr__(self):
        return "SVG_Figure:",self.id,self.title
        
    def __str__(self):
        return "SVG_Figure: %s: %s: %s" % (self.id,self.region,self.title)

def calculate_bounding_box(figureList):
    """
    Calculates a bounding box.  I borrowed this from stackoverflow at the link below, but it's basically just a min/max calculation:
    http://stackoverflow.com/questions/1303265/algorithm-for-determining-minimum-bounding-rectangle-for-collection-of-latitude
    Note the important assumption here - this only works if you are using data having the same projection!
    """
    minLat = 900.0;
    minLon = 900.0;
    maxLat = -900.0;
    maxLon = -900.0;
    for point in [figure.get_point() for figure in figureList]:
        minLat = min( minLat, point.latitude );
        minLon = min( minLon, point.longitude );
        maxLat = max( maxLat, point.latitude );
        maxLon = max( maxLon, point.longitude );
        
    return minLat, minLon, maxLat, maxLon

def figuresToJsonString(figureList):
    """
    Produces a json string in the worst, most desperate, horrible hack manner imaginable.  Todo, improve this later.
    """
    pathString = ""
    if figureList:
        pathString = "\"path\":["
        for figure in figureList:
            pathString += "{\"id\":\"" + figure.id + "\",\"title\":\"" + figure.title + "\",\"d\":\"" + figure.pathString + "\"},"
        pathString += "]"
    return pathString

def generate_map(mapname, inputfile, js_templatefile, js_outputfile, html_templatefile, html_outputfile, karto=True):
    """
    From the given svg input file, extract the relevant info and use the given .js and .html template files to produce the "populated" js and html files.
    Setting karto=False should work for indiemap-generated SVG; Karto-generated SVG will have slightly different attribute names.
    """
    print "+++svg_to_ammap: parsing file", inputfile
    try:
        svg = minidom.parse(inputfile)
        pathlist = svg.getElementsByTagName('path')
        print "+++svg_to_ammap: svg loaded."
        
        figureList = []
        tokenDict = {}
        elementCount = 0
        PREFIX = ""
        if karto:
            PREFIX = "data-"
            
        for path in pathlist:
            elementDict = dict(path.attributes.items())
            if karto:
                discriminant = PREFIX+'gn-name'
            else:
                discriminant = "gn_name"
                
            if discriminant in elementDict:
                # this will be the second set of "g" elements
                if karto:
                    svgFigure = SVG_Figure(elementDict[PREFIX+'code-hasc'] + "-" + str(elementCount), elementDict[PREFIX+'gn-name'], elementDict[PREFIX+'gns-region'],
                                          elementDict['d'], elementDict[PREFIX+'latitude'], elementDict[PREFIX+'longitude'])
                else:
                    svgFigure = SVG_Figure(elementDict[PREFIX+'code_hasc'] + "-" + str(elementCount), elementDict[PREFIX+'gn_name'], elementDict[PREFIX+'gns_region'],
                                      elementDict['d'], elementDict[PREFIX+'latitude'], elementDict[PREFIX+'longitude'])
                figureList.append(svgFigure)
                print "+++svg_to_ammap: %s:%s" % (str(elementCount),svgFigure)
                elementCount += 1
                
        print "+++svg_to_ammap: %d elements found." % elementCount
        # now we have a list of SVG_Figures, we can calculate a bounding box
        minLat, minLon, maxLat, maxLon = calculate_bounding_box(figureList)
        print "+++svg_to_ammap: bounding box: %f,%f: %f,%f" % (minLat, minLon, maxLat, maxLon)
        
        # generate json suitable for ammap
        jsonPath = figuresToJsonString(figureList)
        print "+++svg_to_ammap: jsonPath:",jsonPath
        
        tokenDict = {MAP_NAME_TOKEN:mapname, MIN_LAT_TOKEN:str(minLat), MIN_LON_TOKEN:str(minLon), MAX_LAT_TOKEN:str(maxLat), MAX_LON_TOKEN:str(maxLon),SVG_PATH_TOKEN:jsonPath} #customized for map generation
        print "+++svg_to_ammap: generating ",js_outputfile
        # generate the js
        fokenizer.fokenize(js_templatefile, os.path.join(config.get_generated_file_path(), js_outputfile), tokenDict)
        print "+++svg_to_ammap: generating ",html_outputfile
        # generate the html
        fokenizer.fokenize(html_templatefile, os.path.join(config.get_generated_file_path(), html_outputfile), tokenDict)
    except:
        print "+++svg_to_ammap: error - the input file could not be parsed."

def run(mapName):
    """
    Convenience function that allows calling the generator with only the map name.
    """
    generate_map(mapName, os.path.join(config.get_generated_file_path(), config.get_generated_svg_name(mapName)), JS_TEMPLATE_FILE, config.get_generated_js_name(mapName), HTML_TEMPLATE_FILE, config.get_generated_html_name(mapName))
    
if __name__ == "__main__":
    # some test code
    map = "ZW"
    # generate the map js and the html file around it
    run(map)