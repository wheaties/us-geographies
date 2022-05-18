from usgeo.iops.database import ShapeDataTable
from usgeo.iops.metadata import multi_file_load
from usgeo.parsers.shapefile import parse_file


puma_shapes = ShapeDataTable('puma')
puma_shapes.columns = ['statefp TEXT NOT NULL',
                       'pumace TEXT NOT NULL',
                       'geoid TEXT NOT NULL',
                       'namelsad TEXT NOT NULL',
                       'mtfcc TEXT NOT NULL',
                       'funcstat TEXT NOT NULL',
                       'aland BIGINT',
                       'awater BIGINT',
                       'intptlat TEXT NOT NULL',
                       'intptlon TEXT NOT NULL']

load_puma_shapefile = multi_file_load(puma_shapes, parse_file)
