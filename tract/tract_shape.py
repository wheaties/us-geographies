from iops.database import ShapeDataTable
from metadata.methods import file_metadata
from parsers.shapefile import parse_file


tract_shapes = ShapeDataTable('tract')
tract_shapes.columns = ['statefp TEXT NOT NULL',
                        'countfp TEXT NOT NULL',
                        'tractce TEXT NOT NULL',
                        'geoid TEXT NOT NULL',
                        'name TEXT NOT NULL',
                        'namelsad TEXT NOT NULL',
                        'mtfcc TEXT NOT NULL',
                        'funcstat TEXT NOT NULL',
                        'aland BIGINT',
                        'awater BIGINT',
                        'intptlat TEXT NOT NULL',
                        'intptlon TEXT NOT NULL']


def load_tract_shapefile(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, 'TRACT', force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from tract shapefile at {filepath}.')
            tract_shapes.populate(connection, year, records)
