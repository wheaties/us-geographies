from iops.database import ShapeDataTable
from metadata.methods import single_file_load
from parsers.shapefile import parse_file


cbsa_shapes = ShapeDataTable('metro')
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

metdiv_shapes = ShapeDataTable('metdiv', 'metro')
metdiv_shapes.columns = ['csafp TEXT',
                         'cbsafp TEXT NOT NULL',
                         'metdivfp TEXT NOT NULL',
                         'geoid TEXT NOT NULL',
                         'name TEXT NOT NULL',
                         'namelsad TEXT NOT NULL',
                         'lsad TEXT NOT NULL',
                         'mtfcc TEXT NOT NULL',
                         'aland BIGINT NOT NULL',
                         'awater BIGINT NOT NULL',
                         'intptlat TEXT NOT NULL',
                         'intptlon TEXT NOT NULL']

load_metdiv_shapefile = single_file_load(metdiv_shapes, parse_file)

csa_shapes = ShapeDataTable('csa', 'metro')
csa_shapes.columns = ['csafp TEXT NOT NULL',
                      'geoid TEXT NOT NULL',
                      'name TEXT NOT NULL',
                      'namelsad TEXT NOT NULL',
                      'lsad TEXT NOT NULL',
                      'mtfcc TEXT NOT NULL',
                      'aland BIGINT NOT NULL',
                      'awater BIGINT NOT NULL',
                      'intptlat TEXT NOT NULL',
                      'intptlon TEXT NOT NULL']

load_csa_shapefile = single_file_load(csa_shapes, parse_file)
