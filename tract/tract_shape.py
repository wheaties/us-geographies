from metadata.methods import file_metadata
from parsers.shapefile import parse_file


def _table_name(year):
    return f'tract_shapes_{year}'


def tract_shape_setup(connection, year, force=False):
    _create_tract_shape_table(connection, year)
    if force:
        _clear_tract_shape_table(connection, year)


def _create_tract_shape_table(connection, year):
    with connection.cursor() as cursor:
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {_table_name(year)} (
            statefp TEXT NOT NULL,
            countfp TEXT NOT NULL,
            tractce TEXT NOT NULL,
            geoid TEXT NOT NULL,
            name TEXT NOT NULL,
            namelsad TEXT NOT NULL,
            mtfcc TEXT NOT NULL,
            funcstat TEXT NOT NULL,
            aland BIGINT,
            awater BIGINT,
            intptlat TEXT NOT NULL,
            intptlon TEXT NOT NULL,
            geom GEOMETRY)''')


def _clear_tract_shape_table(conn, year):
    with conn.cursor() as cursor:
        cursor.execute(f'''DELETE FROM {_table_name(year)}''')


def _populate_tract_shape_table(records, connection, year):
    with connection.cursor() as cursor:
        for record in records:
            cursor.execute(f'''
            INSERT INTO {_table_name(year)}
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ST_GeomFromGeoJSON(%s))''',
                           record)


def load_tract_shapefile(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, 'TRACT', force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from tract shapefile at {filepath}.')
            _populate_tract_shape_table(records, connection, year)
