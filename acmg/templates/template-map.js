// (c) ammap.com | SVG (in JSON format) map of {{MAP_NAME}}
AmCharts.maps.{{MAP_NAME}}={
	"svg": {
		"defs": {
			"amcharts:ammap": {
				"projection":"mercator",
				"leftLongitude":"{{MIN_LON}}",
				"topLatitude":"{{MAX_LAT}}",
				"rightLongitude":"{{MAX_LON}}",
				"bottomLatitude":"{{MIN_LAT}}"
			}
		},
		"g":{
			{{SVG_PATH_AS_JSON}}
		}
	}
};