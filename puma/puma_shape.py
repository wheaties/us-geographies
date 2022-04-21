from metadata.methods import file_metadata
from parsers.shapefile import parse_file


def _table_name(year):
    return f'puma_shapes_{year}'


def puma_shape_setup(connection, year, force=False):
    _create_puma_shape_table(connection, year)
    if force:
        _clear_puma_shape_table(connection, year)


def _create_puma_shape_table(connection, year):
    with connection.cursor() as cursor:
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {_table_name(year)} (
            statefp TEXT NOT NULL,
            pumace TEXT NOT NULL,
            geoid TEXT NOT NULL,
            namelsad TEXT NOT NULL,
            mtfcc TEXT NOT NULL,
            funcstat TEXT NOT NULL,
            aland BIGINT,
            awater BIGINT,
            intptlat TEXT NOT NULL,
            intptlon TEXT NOT NULL,
            geom GEOMETRY)''')


def _clear_puma_shape_table(conn, year):
    with conn.cursor() as cursor:
        cursor.execute(f'''DELETE FROM {_table_name(year)}''')


def _populate_puma_shape_table(records, connection, year):
    with connection.cursor() as cursor:
        for record in records:
            cursor.execute(f'''
            INSERT INTO {_table_name(year)}
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ST_GeomFromGeoJSON(%s))''',
                           record)


def load_puma_shapefile(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, 'PUMA', force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from puma shapefile at {filepath}.')
            _populate_puma_shape_table(records, connection, year)
