from iops.database import RawDataTable
from metadata.methods import file_metadata
from parsers.xlsx import parse_file as xlsx_file
from parsers.xls import parse_file as xls_file
from openpyxl.utils.exceptions import InvalidFileException


fips_stategeocodes = RawDataTable('fips_stategeocodes')
fips_stategeocodes.columns = ['region TEXT NOT NULL',
                              'division TEXT NOT NULL',
                              'state TEXT NOT NULL',
                              'name TEXT NOT NULL']


def load_raw_fips_stategeocodes(connection, filepath, year, force=False):
    fips_stategeocodes.setup(connection, year, force)
    with file_metadata(connection, filepath, fips_stategeocodes.group, force) as file_loaded:
        if not file_loaded or force:
            try:
                rows = xlsx_file(str(filepath), 7)
            except InvalidFileException:
                rows = xls_file(str(filepath), 5)
            print(f'Read {len(rows)} records from fips at {filepath}.')
            fips_stategeocodes.populate(connection, year, rows)
