from iops.database import ShapeDataTable
from iops.metadata import multi_file_load
from parsers.shapefile import parse_file


tract_shapes = ShapeDataTable('tract')
tract_shapes.columns = ['statefp TEXT NOT NULL',
                        'countfp TEXT NOT NULL',
                        'tractce TEXT NOT NULL',
                        'geoid TEXT NOT NULL',
                        'name TEXT NOT NULL',
                        'namelsad TEXT NOT NULL',
                        'mtfcc TEXT NOT NULL',
                        'funcstat TEXT NOT NULL',
                        'aland BIGINT',
                        'awater BIGINT',
                        'intptlat TEXT NOT NULL',
                        'intptlon TEXT NOT NULL']

load_files = multi_file_load(tract_shapes, parse_file)
