from metadata.methods import file_metadata
from parsers.xlsx import parse_file as xlsx_file
from parsers.xls import parse_file as xls_file
from openpyxl.utils.exceptions import InvalidFileException

def fips_stategeocode_setup(connection, year, force=False):
    _create_raw_fips_table(connection, year)
    if force:
        _clear_raw_fips_table(connection, year)


def _table_name(year):
    return f'fips_stategeocodes_raw_{year}'


def _clear_raw_fips_table(conn, year):
    with conn.cursor() as cursor:
        cursor.execute(f'''DELETE FROM {_table_name(year)}''')


def _create_raw_fips_table(conn, year):
    with conn.cursor() as cursor:
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {_table_name(year)} (
        region TEXT NOT NULL,
        division TEXT NOT NULL,
        state TEXT NOT NULL,
        name TEXT NOT NULL)''')


def _populate_raw_fips_table(conn, year, rows):
    with conn.cursor() as cursor:
        for row in rows:
            cursor.execute(f'''
            INSERT INTO {_table_name(year)}
            VALUES(%s, %s, %s, %s)''',
                           row)


def load_raw_fips_stategeocodes(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, 'FIPS', force) as file_loaded:
        if not file_loaded or force:
            try:
                rows = xlsx_file(str(filepath), 7)
            except InvalidFileException:
                rows = xls_file(str(filepath), 5)
            print(f'Read {len(rows)} records from fips at {filepath}.')
            _populate_raw_fips_table(connection, year, rows)
