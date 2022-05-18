from functools import partial
from usgeo.iops.database import RawDataTable
from usgeo.iops.metadata import single_file_load
from usgeo.parsers.pdf import parse_file

GROUP = 'census'


mtfcc = RawDataTable('mtfcc', GROUP)
mtfcc.columns = ['mtfcc TEXT NOT NULL',
                 'feature_class TEXT NOT NULL',
                 'superclass TEXT NOT NULL',
                 'point TEXT NOT NULL',
                 'linear TEXT NOT NULL',
                 'areal TEXT NOT NULL',
                 'description TEXT NOT NULL']

load_mtfcc_table = single_file_load(mtfcc, partial(parse_file, skip_header=1))

funcstat = RawDataTable('funcstat', GROUP)
funcstat.columns = ['funcstat TEXT NOT NULL',
                    'description TEXT NOT NULL',
                    'associated_geography TEXT NOT NULL']

load_funcstat_table = single_file_load(funcstat, partial(parse_file, skip_beginning=1))

class_codes = RawDataTable('class', GROUP)
class_codes.columns = ['class TEXT NOT NULL',
                       'description TEXT NOT NULL',
                       'associated_geography TEXT NOT NULL']

load_class_table = single_file_load(class_codes, partial(parse_file, skip_beginning=1))

lsad = RawDataTable('lsad', GROUP)
lsad.columns = ['lsad TEXT NOT NULL',
                'description TEXT NOT NULL',
                'associated_geography TEXT NOT NULL']

load_lsad_table = single_file_load(lsad, partial(parse_file, skip_beginning=1))
