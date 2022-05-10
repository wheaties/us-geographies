from iops.database import ShapeDataTable
from iops.metadata import single_file_load
from parsers.shapefile import parse_file

GROUP = 'aiannh'

anrc = ShapeDataTable('anrc', GROUP)
anrc.columns = ['statefp TEXT NOT NULL',
                'anrcfp TEXT NOT NULL',
                'anrcns TEXT NOT NULL',
                'geoid TEXT NOT NULL',
                'name TEXT NOT NULL',
                'namelsad TEXT NOT NULL',
                'lsad TEXT NOT NULL',
                'classfp TEXT NOT NULL',
                'mtfcc TEXT NOT NULL',
                'funcstat TEXT NOT NULL',
                'aland BIGINT NOT NULL',
                'awater BIGINT NOT NULL',
                'intptlat TEXT NOT NULL',
                'intptlon TEXT NOT NULL']


load_anrc_shapefile = single_file_load(anrc, parse_file)

aiannh = ShapeDataTable('aiannh', GROUP)
aiannh.columns = ['aiannhce TEXT NOT NULL',
                  'aiannhns TEXT NOT NULL',
                  'geoid TEXT NOT NULL',
                  'name TEXT NOT NULL',
                  'namelsad TEXT NOT NULL',
                  'lsad TEXT NOT NULL',
                  'classfp TEXT NOT NULL',
                  'comptyp TEXT NOT NULL',
                  'aiannhr TEXT NOT NULL',
                  'mtfcc TEXT NOT NULL',
                  'funcstat TEXT NOT NULL',
                  'aland BIGINT NOT NULL',
                  'awater BIGINT NOT NULL',
                  'intptlat TEXT NOT NULL',
                  'intptlon TEXT NOT NULL']

load_aiannh_shapefile = single_file_load(aiannh, parse_file)

aitsn = ShapeDataTable('aitsn', GROUP)
aitsn.columns = ['aiannhce TEXT NOT NULL',
                 'trsubce TEXT NOT NULL',
                 'trsubns TEXT NOT NULL',
                 'geoid TEXT NOT NULL',
                 'name TEXT NOT NULL',
                 'namelsad TEXT NOT NULL',
                 'lsad TEXT NOT NULL',
                 'classfp TEXT NOT NULL',
                 'mtfcc TEXT NOT NULL',
                 'funcstat TEXT NOT NULL',
                 'aland BIGINT NOT NULL',
                 'awater BIGINT NOT NULL',
                 'intptlat TEXT NOT NULL',
                 'intptlon TEXT NOT NULL']

load_aitsn_shapefile = single_file_load(aitsn, parse_file)

ttract = ShapeDataTable('ttract', GROUP)
ttract.columns = ['aiannhce TEXT NOT NULL',
                  'ttractce TEXT NOT NULL',
                  'geoid TEXT NOT NULL',
                  'name TEXT NOT NULL',
                  'namelsad TEXT NOT NULL',
                  'mtfcc TEXT NOT NULL',
                  'aland BIGINT NOT NULL',
                  'awater BIGINT NOT NULL',
                  'intptlat TEXT NOT NULL',
                  'intptlon TEXT NOT NULL']

load_ttract_shapefile = single_file_load(ttract, parse_file)

tbg = ShapeDataTable('tbg', GROUP)
tbg.columns = ['aiannhce TEXT NOT NULL',
               'ttractce TEXT NOT NULL',
               'tblkgpce TEXT NOT NULL',
               'geoid TEXT NOT NULL',
               'namelsad TEXT NOT NULL',
               'mtfcc TEXT NOT NULL',
               'aland BIGINT NOT NULL',
               'awater BIGINT NOT NULL',
               'intptlat TEXT NOT NULL',
               'intptlon TEXT NOT NULL']

load_tbg_shapefile = single_file_load(tbg, parse_file)
