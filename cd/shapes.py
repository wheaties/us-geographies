from iops.database import ShapeDataTable
from metadata.methods import single_file_load
from parsers.shapefile import parse_file


cd_shapes = ShapeDataTable('cd')
cd_shapes.columns = ['statefp TEXT NOT NULL',
                     'cd TEXT NOT NULL',
                     'geoid TEXT NOT NULL',
                     'NAMELSAD TEXT NOT NULL',
                     'LSAD TEXT NOT NULL',
                     'CDSESSN TEXT NOT NULL',
                     'MTFCC TEXT NOT NULL',
                     'FUNCSTAT TEXT NOT NULL',
                     'ALAND BIGINT',
                     'AWATER BIGINT',
                     'INTPTLAT TEXT NOT NULL',
                     'INTPTLON TEXT NOT NULL']

load_cd_shapefile = single_file_load(cd_shapes, parse_file)
