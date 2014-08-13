#!/usr/bin/env python
import sys
from kartograph import Kartograph
import config
import os

# instantiate the one and only Kartograph
k = Kartograph()

# I ended up not using this, I think Karto has a bug in this area, this is an example of kartograph's callback for filtering
def shape_file_filter(record):
    return record['iso_a2'] == currentCountry # look for a specific iso a2 code

def generate_svg(countryIso2Code, shapefile):
    # config: pull out certain data attributes, that we will need later to generate ammap-consumable paths
    cfg = {"layers": [{"id": "mylayer", "src":shapefile, "filter":{"iso_a2": countryIso2Code},"attributes":{"code_hasc":"code_hasc","gn_name":"gn_name","gns_region":"gns_region","latitude":"latitude","longitude":"longitude"}}], "proj":{"id":"mercator"}}
    
    try:
        print ("+++shape_to_svg: about to generate country %s with config %s" % (countryIso2Code, ', '.join("%s=%r" % (key,val) for (key,val) in cfg.iteritems())))
        k.generate(cfg, outfile=os.path.join(config.get_generated_file_path(), config.get_generated_svg_name(countryIso2Code)))
    except:
        e = sys.exc_info()
        print ("+++shape_to_svg: could not generate map for country: %s Exception: %s" % (countryIso2Code, e))
        
def generate_all_svg():
    for country in COUNTRIES:
        print ("+++shape_to_svg: generating SVG for country:", country)
        generate_svg(country,config.SHAPEFILE)
    
if __name__ == "__main__":
    # todo - run this over everything; catch exceptions
    generate_svg("ZW",config.SHAPEFILE)
