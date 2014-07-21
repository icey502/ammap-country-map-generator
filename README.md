ammap-country-map-generator
===========================

This is a work in progress; more info is coming (TODO)

Amcharts ([http://www.amcharts.com/](http://www.amcharts.com/ "Amcharts")) is a very nice Javascript charting and mapping product.  Their Javascript + SVG approach makes the product ideal to use with customized maps.

To make a long story short, the purpose of the ammap-country-map-generator is to make life a bit easier for those that want to bring an ESRI shapefile to life by showing it in the Amcharts Ammap product.

## The Usual Approach ##
The normal approach when bringing a shape file to something visual, is a hands-on process.  The process involves finding a source for shape files, then using a variety of GIS tooling such as OSGeo4W or QGIS, to generate SVG or similar output.  Generally there is some editing of shapes involved, in order to reduce the map's size, remove unnecessary features, and so forth.  All this is very interesting stuff, but for my purposes (and not being a GIS expert), I wanted something to reduce the process to its mechanical minimum, without being concerned about the relative purity of it. 

## How It Works ##
Simply put, here are the steps to follow, to generate a country map:


- GIT clone this project, or just grab the structure and place it where you want it.
- Install the dependencies - really, that means the python kartograph library ([http://kartograph.org](http://kartograph.org)).  I also found that I had to hack around some GDAL issues, so I used the directions here: ([http://pythongisandstuff.wordpress.com/2011/07/07/installing-gdal-and-ogr-for-python-on-windows/](http://pythongisandstuff.wordpress.com/2011/07/07/installing-gdal-and-ogr-for-python-on-windows/))
- Get a shapefile from the awesome Natural Earth; since we are talking country-level maps here, we can't just grab any old data; we really want the admin level 1 data here:
[http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/)
Downloading this will include the shapefile (.shp) and several other files that relate to the shapefile (specifics not discussed here).
- Put the downloaded shapefile and all the supporting files in the shapefiles directory
- Run the code with the country name.  In python, you can generate an operational ammaps html page with this code (here we provide the Iso-2 code for "Canada"):

    `mapGenerator.generateSingleMap("CA")`
    
