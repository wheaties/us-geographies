from metadata.methods import file_metadata
from parsers.shapefile import parse_file


def _table_name(year):
    return f'cd_shapes_{year}'


def cd_shape_setup(connection, year, force=False):
    _create_cd_shape_table(connection, year)
    if force:
        _clear_cd_shape_table(connection, year)


def _create_cd_shape_table(connection, year):
    with connection.cursor() as cursor:
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {_table_name(year)} (
            statefp TEXT NOT NULL,
            cd TEXT NOT NULL,
            geoid TEXT NOT NULL,
            NAMELSAD TEXT NOT NULL,
            LSAD TEXT NOT NULL,
            CDSESSN TEXT NOT NULL,
            MTFCC TEXT NOT NULL,
            FUNCSTAT TEXT NOT NULL,
            ALAND BIGINT,
            AWATER BIGINT,
            INTPTLAT TEXT NOT NULL,
            INTPTLON TEXT NOT NULL,
            geom GEOMETRY)''')


def _clear_cd_shape_table(conn, year):
    with conn.cursor() as cursor:
        cursor.execute(f'''DELETE FROM {_table_name(year)}''')


def _populate_cd_shape_table(records, connection, year):
    with connection.cursor() as cursor:
        for record in records:
            cursor.execute(f'''
            INSERT INTO {_table_name(year)}
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ST_GeomFromGeoJSON(%s))''',
                           record)


def load_cd_shapefile(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, 'CD', force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from cd shapefile at {filepath}.')
            _populate_cd_shape_table(records, connection, year)
