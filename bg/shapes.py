from iops.database import ShapeDataTable
from iops.metadata import single_file_load
from parsers.shapefile import parse_file


blockgroup_shapes = ShapeDataTable('blockgroup')
blockgroup_shapes.columns = ['statefp TEXT NOT NULL',
                             'countyfp TEXT NOT NULL',
                             'tractce TEXT NOT NULL',
                             'blkgrpce TEXT NOT NULL',
                             'geoid TEXT NOT NULL',
                             'namelsad TEXT NOT NULL',
                             'mtfcc TEXT NOT NULL',
                             'funcstat TEXT NOT NULL',
                             'aland BIGINT NOT NULL',
                             'awater BIGINT NOT NULL',
                             'intptlat TEXT NOT NULL',
                             'intptlon TEXT NOT NULL']

load_blockgroup_shapefile = single_file_load(blockgroup_shapes, parse_file)
