from iops.database import RawDataTable
from metadata.methods import file_metadata
from parsers.xlsx import parse_file as xlsx_file
from parsers.xls import parse_file as xls_file
from openpyxl.utils.exceptions import InvalidFileException


fips_allgeocodes = RawDataTable('fips_allgeocodes')
fips_allgeocodes.columns = ['summary_level TEXT NOT NULL',
                            'state_code TEXT NOT NULL',
                            'county_code TEXT NOT NULL',
                            'count_subdivision_code TEXT NOT NULL',
                            'place_code TEXT NOT NULL',
                            'consolidated_city_code TEXT NOT NULL',
                            'area_name TEXT NOT NULL']


def load_raw_fips_allgeocodes(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, fips_allgeocodes.group, force) as file_loaded:
        if not file_loaded or force:
            try:
                rows = xlsx_file(str(filepath), 6)
            except InvalidFileException:
                rows = xls_file(str(filepath), 4)
            print(f'Read {len(rows)} records from fips at {filepath}.')
            fips_allgeocodes.populate(connection, year, rows)
