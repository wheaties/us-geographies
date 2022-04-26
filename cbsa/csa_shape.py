from iops.database import ShapeDataTable
from metadata.methods import single_file_load
from parsers.shapefile import parse_file


csa_shapes = ShapeDataTable('csa', 'cbsa')
csa_shapes.columns = ['csafp TEXT',
                      'geoid TEXT',
                      'name TEXT NOT NULL',
                      'namelsad TEXT',
                      'lsad TEXT',
                      'mtfcc TEXT',
                      'aland BIGINT',
                      'awater BIGINT',
                      'intptlat TEXT',
                      'intptlon TEXT']

load_csa_shapefile = single_file_load(csa_shapes, parse_file)
