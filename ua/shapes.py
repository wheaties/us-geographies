from iops.database import ShapeDataTable
from iops.metadata import multi_file_load
from parsers.shapefile import parse_file


GROUP = 'ua'


ua_shapes = ShapeDataTable('urban_areas', GROUP)
ua_shapes.columns = ['uace10 TEXT NOT NULL',
                     'geoid10 TEXT NOT NULL',
                     'name10 TEXT NOT NULL',
                     'namelsad10 TEXT NOT NULL',
                     'lsad10 TEXT NOT NULL',
                     'mtfcc10 TEXT NOT NULL',
                     'uatyp10 TEXT NOT NULL',
                     'funcstat10 TEXT NOT NULL',
                     'aland10 BIGINT NOT NULL',
                     'awater10 BIGINT NOT NULL',
                     'intptlat10 TEXT NOT NULL',
                     'intptlon10 TEXT NOT NULL']


load_files = multi_file_load(ua_shapes, parse_file)
