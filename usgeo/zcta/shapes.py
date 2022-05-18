from usgeo.iops.database import ShapeDataTable
from usgeo.iops.metadata import single_file_load
from usgeo.parsers.shapefile import parse_file


zcta_shapes = ShapeDataTable('zcta')
zcta_shapes.columns = ['zcta TEXT NOT NULL',
                       'geoid TEXT NOT NULL',
                       'classfp TEXT NOT NULL',
                       'mtfcc TEXT NOT NULL',
                       'funcstat TEXT NOT NULL',
                       'aland BIGINT',
                       'awater BIGINT',
                       'intptlat TEXT NOT NULL',
                       'intptlon TEXT NOT NULL']

# reference doc describes these attributes but there's no .dbf file in the zip!
load_zcta_shapefile = single_file_load(zcta_shapes, parse_file)
