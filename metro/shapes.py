from iops.database import ShapeDataTable
from iops.metadata import single_file_load
from parsers.shapefile import parse_file


GROUP = 'metro'


cbsa_shapes = ShapeDataTable('metro', GROUP)
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

metdiv_shapes = ShapeDataTable('metdiv', GROUP)
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

csa_shapes = ShapeDataTable('csa', GROUP)
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

necta_combined_shapes = ShapeDataTable('necta_combined', GROUP)
necta_combined_shapes.columns = ['cnectafp TEXT',
                        'geoid TEXT',
                        'name TEXT',
                        'namelsad TEXT',
                        'lsad TEXT',
                        'mtfcc TEXT',
                        'aland BIGINT',
                        'awater BIGINT',
                        'intptlat TEXT',
                        'intptlon TEXT']

load_necta_combined_shapefile = single_file_load(necta_combined_shapes, parse_file)

necta_division_shapes = ShapeDataTable('necta_divisions', GROUP)
necta_division_shapes.columns = ['cnectafp TEXT',
                                 'nectafp TEXT NOT NULL',
                                 'nctadvfp TEXT NOT NULL',
                                 'geoid TEXT NOT NULL',
                                 'name TEXT NOT NULL',
                                 'namelsad TEXT NOT NULL',
                                 'lsad TEXT NOT NULL',
                                 'mtfcc TEXT NOT NULL',
                                 'aland BIGINT NOT NULL',
                                 'awater BIGINT NOT NULL',
                                 'intptlat TEXT NOT NULL',
                                 'intptlon TEXT NOT NULL']

load_necta_division_shapefile = single_file_load(necta_division_shapes, parse_file)

necta_shapes = ShapeDataTable('necta', GROUP)
necta_shapes.columns = ['cnetafp TEXT',
                        'nectafp TEXT NOT NULL',
                        'geoid TEXT NOT NULL',
                        'name TEXT NOT NULL',
                        'namelsad TEXT NOT NULL',
                        'lsad TEXT NOT NULL',
                        'nmemi TEXT NOT NULL',
                        'mtfcc TEXT NOT NULL',
                        'aland BIGINT NOT NULL',
                        'awater BIGINT NOT NULL',
                        'intptlat TEXT NOT NULL',
                        'intptlon TEXT NOT NULL']

load_necta_shapefile = single_file_load(necta_shapes, parse_file)
