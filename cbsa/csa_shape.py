from metadata.methods import file_metadata
from parsers.shapefile import parse_file


def _table_name(year):
    return f'csa_shapes_{year}'


def csa_shape_setup(connection, year, force=False):
    _create_csa_shape_table(connection, year)
    if force:
        _clear_csa_shape_table(connection, year)


def _create_csa_shape_table(connection, year):
    with connection.cursor() as cursor:
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {_table_name(year)} (
            csafp TEXT,
            geoid TEXT,
            name TEXT NOT NULL,
            namelsad TEXT,
            lsad TEXT,
            mtfcc TEXT,
            aland BIGINT,
            awater BIGINT,
            intptlat TEXT,
            intptlon TEXT,
            geom GEOMETRY
            )''')


def _clear_csa_shape_table(connection, year):
    with connection.cursor() as cursor:
        cursor.execute(f'''DELETE FROM {_table_name(year)}''')


def _populate_csa_shape_table(records, connection, year):
    with connection.cursor() as cursor:
        for record in records:
            cursor.execute(f'''
            INSERT INTO {_table_name(year)}
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ST_GeomFromGeoJSON(%s))''',
                           record)


def load_csa_shapefile(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, 'CBSA', force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from csa shapefile.')
            _populate_csa_shape_table(records, connection, year)