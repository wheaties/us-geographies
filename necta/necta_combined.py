from metadata.methods import file_metadata
from parsers.xls import parse_file


def necta_combined_setup(connection, year, force=False):
    _create_raw_necta_table(connection, year)
    if force:
        _clear_raw_necta_table(connection, year)


def _table_name(year):
    return f'necta_combined_raw_{year}'


def _clear_raw_necta_table(conn, year):
    with conn.cursor() as cursor:
        cursor.execute(f'''DELETE FROM {_table_name(year)}''')


def _create_raw_necta_table(conn, year):
    with conn.cursor() as cursor:
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {_table_name(year)} (
            necta_code TEXT NOT NULL,
            necta_division_code TEXT,
            necta_combined_code TEXT,
            necta_title TEXT NOT NULL,
            metro_micro_necta TEXT NOT NULL,
            necta_division_title TEXT,
            necta_combined_title TEXT,
            city_name TEXT,
            fips_state_code TEXT NOT NULL,
            fips_county_code TEXT,
            fips_county_subdivision_code TEXT)''')


def _populate_raw_necta_table(connection, year, rows):
    with connection.cursor() as cursor:
        for row in rows:
            cursor.execute(f'''
            INSERT INTO {_table_name(year)}
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                           row)


def load_raw_necta_combined(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, 'NECTA', force) as file_loaded:
        if not file_loaded or force:
            rows = parse_file(str(filepath), 2, 4)
            print(f'Read {len(rows)} records from necta at {filepath}.')
            _populate_raw_necta_table(connection, year, rows)
