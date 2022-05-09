from iops.database import ShapeDataTable
from iops.metadata import single_file_load
from parsers.shapefile import parse_file


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

load_puma_shapefile = single_file_load(puma_shapes, parse_file)
