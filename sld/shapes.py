from iops.database import ShapeDataTable
from iops.metadata import single_file_load
from parsers.shapefile import parse_file


sldu_shapes = ShapeDataTable('sldu', 'sld')
sldu_shapes.columns = ['statefp TEXT NOT NULL',
                       'sldust TEXT NOT NULL',
                       'geoid TEXT NOT NULL',
                       'namelsad TEXT NOT NULL',
                       'lsad TEXT NOT NULL',
                       'lsy TEXT NOT NULL',
                       'mtfcc TEXT NOT NULL',
                       'funcstat TEXT NOT NULL',
                       'aland BIGINT NOT NULL',
                       'awater BIGINT NOT NULL',
                       'intptlat TEXT NOT NULL',
                       'intptlon TEXT NOT NULL']

load_sldu_shapefile = single_file_load(sldu_shapes, parse_file)

sldl_shapes = ShapeDataTable('sldl', 'sld')
sldl_shapes.columns = ['statefp TEXT NOT NULL',
                       'sldlst TEXT NOT NULL',
                       'geoid TEXT NOT NULL',
                       'namelsad TEXT NOT NULL',
                       'lsad TEXT NOT NULL',
                       'lsy TEXT NOT NULL',
                       'mtfcc TEXT NOT NULL',
                       'funcstat TEXT NOT NULL',
                       'aland BIGINT NOT NULL',
                       'awater BIGINT NOT NULL',
                       'intptlat TEXT NOT NULL',
                       'intptlon TEXT NOT NULL']

load_sldl_shapefile = single_file_load(sldl_shapes, parse_file)
