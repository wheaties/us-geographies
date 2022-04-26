from iops.database import RawDataTable
from metadata.methods import single_file_load
from parsers.xlsx import parse_file as xlsx_file
from parsers.xls import parse_file as xls_file
from openpyxl.utils.exceptions import InvalidFileException


fips_stategeocodes = RawDataTable('fips_stategeocodes')
fips_stategeocodes.columns = ['region TEXT NOT NULL',
                              'division TEXT NOT NULL',
                              'state TEXT NOT NULL',
                              'name TEXT NOT NULL']


def _parse_both(filepath):
    try:
        return xlsx_file(str(filepath), 7)
    except InvalidFileException:
        return xls_file(str(filepath), 5)


load_raw_fips_stategeocodes = single_file_load(fips_stategeocodes, _parse_both)
