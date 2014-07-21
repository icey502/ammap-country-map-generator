#!/usr/bin/env python
"""
Config for common elements like the shape file name; also, functions to ensure common generated file names
"""

# the shapefile to use
SHAPEFILE = "shapefiles/ne_10m_admin_1_states_provinces.shp"

def get_generated_svg_name(mapname):
    return "_generated_" + mapname + ".svg"

def get_generated_js_name(mapname):
    return "generated-map-" + mapname + ".js"

def get_generated_html_name(mapname):
    return "generated-map-" + mapname + ".html"

def get_generated_file_path():
    return "generated_maps"