from metadata.methods import file_metadata
from parsers.xls import parse_file


def cbsa_delineation_setup(connection, year, force=False):
    _create_raw_cbsa_table(connection, year)
    if force:
        _clear_raw_cbsa_table(connection, year)


def _table_name(year):
    return f'cbsa_raw_{year}'


def _clear_raw_cbsa_table(conn, year):
    with conn.cursor() as cursor:
        cursor.execute(f'''DELETE FROM {_table_name(year)}''')


def _create_raw_cbsa_table(conn, year):
    with conn.cursor() as cursor:
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {_table_name(year)} (
          cbsa_code TEXT NOT NULL,
          metro_division_code TEXT,
          csa_code TEXT,
          cbsa_title TEXT NOT NULL,
          metro_micro_statistical_area TEXT,
          metro_division_title TEXT,
          csa_title TEXT,
          county_equiv TEXT NOT NULL,
          state_name TEXT NOT NULL,
          fips_state_code TEXT NOT NULL,
          fips_county_code TEXT NOT NULL,
          central_outlying TEXT NOT NULL
        )''')


def _populate_raw_cbsa_table(connection, year, rows):
    with connection.cursor() as cursor:
        for row in rows:
            cursor.execute(f'''
            INSERT INTO {_table_name(year)}
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                           row)


def load_raw_cbsa(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, 'CBSA', force) as file_loaded:
        if not file_loaded or force:
            rows = parse_file(str(filepath), 2, 4)
            print(f'Read {len(rows)} records from cbsa at {filepath}.')
            _populate_raw_cbsa_table(connection, year, rows)
