from iops.database import ShapeDataTable
from metadata.methods import single_file_load
from parsers.shapefile import parse_file


cbsa_shapes = ShapeDataTable('cbsa')
cbsa_shapes.columns = ['csafp TEXT',
                       'cbsafp TEXT',
                       'geoid TEXT',
                       'name TEXT NOT NULL',
                       'namelsad TEXT',
                       'lsad TEXT',
                       'memi TEXT',
                       'mtfcc TEXT',
                       'aland BIGINT',
                       'awater BIGINT',
                       'intptlat TEXT',
                       'intptlon TEXT']

load_cbsa_shapefile = single_file_load(cbsa_shapes, parse_file)
