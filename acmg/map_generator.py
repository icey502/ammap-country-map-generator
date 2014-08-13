#!/usr/bin/env python
import sys
import shape_to_svg
import svg_to_ammap
import config
        
def generate_single_map(countryIso2Code):
    """
    Generates a single map using shape_to_svg and svg_to_ammap
    """
    print ("+++map_generator: generate_single_map() generating SVG for country: %s" % countryIso2Code)
    shape_to_svg.generate_svg(countryIso2Code, config.SHAPEFILE)
    svg_to_ammap.run(countryIso2Code)
    print ("+++map_generator: done.")
    
def generate_all_maps(countryIso2CodeList):
    """
    Generates a set of maps using a supplied list of ISO-3166-2 codes.
    """
    print ("+++map_generator: generateAllMaps()")
    for country in countryIso2CodeList:
        generate_single_map(country)
    print ("+++map_generator: done.")
    
if __name__ == "__main__":
    # example invokation
    generate_single_map("UY")
