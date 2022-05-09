from iops.database import ShapeDataTable
from iops.metadata import single_file_load
from parsers.shapefile import parse_file


GROUP = 'sd'


elsd_shapes = ShapeDataTable('elementary_school_districts', GROUP)
elsd_shapes.columns = ['statefp TEXT NOT NULL',
                       'elsdlea TEXT NOT NULL',
                       'geoid TEXT NOT NULL',
                       'name TEXT NOT NULL',
                       'lsad TEXT NOT NULL',
                       'lograde TEXT NOT NULL',
                       'higrade TEXT NOT NULL',
                       'mtfcc TEXT NOT NULL',
                       'sdtyp TEXT',
                       'funcstat TEXT NOT NULL',
                       'aland BIGINT NOT NULL',
                       'awater BIGINT NOT NULL',
                       'intptlat TEXT NOT NULL',
                       'intptlon TEXT NOT NULL']

load_elsd_shapefile = single_file_load(elsd_shapes, parse_file)

scsd_shapes = ShapeDataTable('secondary_school_districts', GROUP)
scsd_shapes.columns = ['statefp TEXT NOT NULL',
                       'scsdlea TEXT NOT NULL',
                       'geoid TEXT NOT NULL',
                       'name TEXT NOT NULL',
                       'lsad TEXT NOT NULL',
                       'lograde TEXT NOT NULL',
                       'higrade TEXT NOT NULL',
                       'mtfcc TEXT NOT NULL',
                       'sdtyp TEXT',
                       'funcstat TEXT NOT NULL',
                       'aland BIGINT NOT NULL',
                       'awater BIGINT NOT NULL',
                       'intptlat TEXT NOT NULL',
                       'intptlon TEXT NOT NULL']

load_scsd_shapefile = single_file_load(scsd_shapes, parse_file)

unsd_shapes = ShapeDataTable('unified_school_districts', GROUP)
unsd_shapes.columns = ['statefp TEXT NOT NULL',
                       'unsdlea TEXT NOT NULL',
                       'geoid TEXT NOT NULL',
                       'name TEXT NOT NULL',
                       'lsad TEXT NOT NULL',
                       'lograde TEXT NOT NULL',
                       'higrade TEXT NOT NULL',
                       'mtfcc TEXT NOT NULL',
                       'sdtyp TEXT',
                       'funcstat TEXT NOT NULL',
                       'aland BIGINT NOT NULL',
                       'awater BIGINT NOT NULL',
                       'intptlat TEXT NOT NULL',
                       'intptlon TEXT NOT NULL']

load_unsd_shapefile = single_file_load(unsd_shapes, parse_file)
