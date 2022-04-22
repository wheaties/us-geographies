from iops.database import RawDataTable
from metadata.methods import file_metadata
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


def load_raw_cbsa(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, cbsa_table.group, force) as file_loaded:
        if not file_loaded or force:
            rows = parse_file(str(filepath), 2, 4)
            print(f'Read {len(rows)} records from cbsa at {filepath}.')
            cbsa_table.populate(connection, year, rows)
