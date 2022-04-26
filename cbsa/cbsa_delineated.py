from functools import partial
from iops.database import RawDataTable
from metadata.methods import single_file_load
from parsers.xls import parse_file


cbsa_table = RawDataTable('cbsa')
cbsa_table.columns = ['cbsa_code TEXT NOT NULL',
                      'metro_division_code TEXT',
                      'csa_code TEXT',
                      'cbsa_title TEXT NOT NULL',
                      'metro_micro_statistical_area TEXT',
                      'metro_division_title TEXT',
                      'csa_title TEXT',
                      'county_equiv TEXT NOT NULL',
                      'state_name TEXT NOT NULL',
                      'fips_state_code TEXT NOT NULL',
                      'fips_county_code TEXT NOT NULL',
                      'central_outlying TEXT NOT NULL']

load_raw_cbsa = single_file_load(cbsa_table,
                                 partial(parse_file, skip_beginning=2, skip_ending=4))
