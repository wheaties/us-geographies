from iops.database import RawDataTable
from metadata.methods import file_metadata
from parsers.xls import parse_file


necta_combined = RawDataTable('necta_combined')
necta_combined.columns =['necta_code TEXT NOT NULL',
                         'necta_division_code TEXT',
                         'necta_combined_code TEXT',
                         'necta_title TEXT NOT NULL',
                         'metro_micro_necta TEXT NOT NULL',
                         'necta_division_title TEXT',
                         'necta_combined_title TEXT',
                         'city_name TEXT',
                         'fips_state_code TEXT NOT NULL',
                         'fips_county_code TEXT',
                         'fips_county_subdivision_code TEXT']


def load_raw_necta_combined(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, necta_combined.group, force) as file_loaded:
        if not file_loaded or force:
            rows = parse_file(str(filepath), 2, 4)
            print(f'Read {len(rows)} records from necta at {filepath}.')
            necta_combined.populate(connection, year, rows)
