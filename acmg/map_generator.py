#!/usr/bin/env python
import sys
import shape_to_svg
import svg_to_ammap
import config

# the countries I want to go after
COUNTRIES = [
"ZW"
]
COUNTRIES_FULL = [
"AF","AL","DZ","AD","AO","AG","AR","AM","AU","AT","AZ","BH","BD","BB","BY","BE","BZ","BJ","BM","BT",
"BO","BA","BW","BR","BN","BG","BF","BI","KH","CM","CA","CV","KY","CF","TD","CL","CN","CO","KM","CG",
"CD","CR","HR","CU","CY","CZ","DK","DJ","DM","DO","TL","EC","EG","SV","GQ","ER","EE","ET","FJ","FI",
"FR","GF","GA","GE","DE","GH","GR","GL","GD","GT","GN","GW","GY","HT","HN","HK","HU","IS","IN","ID",
"IR","IQ","IE","IL","IT","CI","JM","JP","JO","KZ","KE","KI","KW","KG","LA","LV","LB","LS","LR","LY",
"LI","LT","LU","MO","MK","MG","MW","MY","MV","ML","MT","MH","MQ","MR","MU","MX","FM","MD","MC","MN",
"ME","MA","MZ","MM","NA","NR","NP","NL","NZ","NI","NE","NG","KP","NO","OM","PK","PA","PG","PY","PE",
"PH","PL","PT","PR","QA","RO","RU","RW","WS","SM","ST","SA","SN","RS","SC","SL","SG","SK","SI","SB",
"SO","ZA","KR","ES","LK","KN","LC","VC","SD","SR","SZ","SE","CH","SY","TW","TJ","TZ","TH","BS","GM",
"TG","TO","TT","TN","TR","TM","TV","UG","UA","AE","GB","US","UY","UZ","VU","VE","VN","EH","YE","ZM",
"ZW"
]
        
def generate_single_map(countryIso2Code):
    """
    Generates a single map using shape_to_svg and svg_to_ammap
    """
    print "+++map_generator: generateSingleMap() generating SVG for country:", countryIso2Code
    shape_to_svg.generate_svg(countryIso2Code, config.SHAPEFILE)
    svg_to_ammap.run(countryIso2Code)
    print "+++map_generator: done."
    
def generate_all_maps(countryIso2CodeList):
    """
    Generates a set of maps using a supplied list of ISO-3166-2 codes.
    """
    print "+++map_generator: generateAllMaps()"
    for country in countryIso2CodeList:
        print "+++map_generator: generating SVG for country:", country
        shape_to_svg.generate_svg(country, config.SHAPEFILE)
        svg_to_ammap.run(countryIso2Code)
    print "+++map_generator: done."
    
if __name__ == "__main__":
    # example invokation
    generate_single_map("UY")
