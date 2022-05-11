from functools import partial
from iops.database import RawDataTable
from iops.metadata import single_file_load
from parsers.pdf import parse_file

GROUP = 'census'


mtfcc = RawDataTable('mtfcc', GROUP)
mtfcc.columns = ['mtfcc TEXT NOT NULL',
                 'feature_class TEXT NOT NULL',
                 'superclass TEXT NOT NULL',
                 'point TEXT NOT NULL',
                 'linear TEXT NOT NULL',
                 'areal TEXT NOT NULL',
                 'description TEXT NOT NULL']

load_mtfcc_table = single_file_load(mtfcc, parse_file)

funcstat = RawDataTable('funcstat', GROUP)
funcstat.columns = ['funcstat TEXT NOT NULL',
                    'description TEXT NOT NULL',
                    'associated_geography TEXT NOT NULL']

load_funcstat_table = single_file_load(funcstat, partial(parse_file, skip_beginning=1))