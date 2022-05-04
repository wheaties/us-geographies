from iops.database import ShapeDataTable
from metadata.methods import single_file_load
from parsers.shapefile import parse_file


places_shapes = ShapeDataTable('place')
places_shapes.columns = ['statefp TEXT NOT NULL',
                         'placefp TEXT NOT NULL',
                         'placens TEXT NOT NULL',
                         'geoid TEXT NOT NULL',
                         'name TEXT NOT NULL',
                         'namelsad TEXT NOT NULL',
                         'lsad TEXT NOT NULL',
                         'classfp TEXT NOT NULL',
                         'pcicbsa TEXT',
                         'pcinecta TEXT',
                         'mtfcc TEXT NOT NULL',
                         'funcstat TEXT NOT NULL',
                         'aland BIGINT',
                         'awater BIGINT',
                         'intptlat TEXT NOT NULL',
                         'intptlon TEXT NOT NULL']

load_places_shapefile = single_file_load(places_shapes, parse_file)
