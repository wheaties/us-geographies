from iops.database import ShapeDataTable
from metadata.methods import single_file_load
from parsers.shapefile import parse_file


necta_shapes = ShapeDataTable('necta')
necta_shapes.columns = ['centafp TEXT',
                        'geoid TEXT',
                        'name TEXT',
                        'namelsad TEXT',
                        'lsad TEXT',
                        'mtfcc TEXT',
                        'aland BIGINT',
                        'awater BIGINT',
                        'intptlat TEXT',
                        'intptlon TEXT']

load_necta_shapefile = single_file_load(necta_shapes, parse_file)
