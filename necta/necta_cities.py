from iops.database import RawDataTable
from metadata.methods import file_metadata
from parsers.xls import parse_file


necta_cities = RawDataTable('necta_cities')
necta_cities.columns = ['necta_code TEXT NOT NULL',
                        'necta_title TEXT NOT NULL',
                        'metro_micro_necta TEXT NOT NULL',
                        'principal_city_name TEXT NOT NULL',
                        'fips_state_code TEXT NOT NULL',
                        'fips_place_code TEXT NOT NULL']


def load_raw_necta_cities(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, necta_cities.group, force) as file_loaded:
        if not file_loaded or force:
            rows = parse_file(str(filepath), 2, 4)
            print(f'Read {len(rows)} records from necta at {filepath}.')
            necta_cities.populate(connection, year, rows)
