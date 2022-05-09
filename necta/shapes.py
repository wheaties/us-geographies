from iops.database import ShapeDataTable
from iops.metadata import single_file_load
from parsers.shapefile import parse_file


necta_combined_shapes = ShapeDataTable('necta_combined')
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

necta_division_shapes = ShapeDataTable('necta_divisions')
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

necta_shapes = ShapeDataTable('necta')
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
