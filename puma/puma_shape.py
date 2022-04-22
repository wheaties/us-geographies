from iops.database import ShapeDataTable
from metadata.methods import file_metadata
from parsers.shapefile import parse_file


puma_shapes = ShapeDataTable('puma')
puma_shapes.columns = ['statefp TEXT NOT NULL',
                       'pumace TEXT NOT NULL',
                       'geoid TEXT NOT NULL',
                       'namelsad TEXT NOT NULL',
                       'mtfcc TEXT NOT NULL',
                       'funcstat TEXT NOT NULL',
                       'aland BIGINT',
                       'awater BIGINT',
                       'intptlat TEXT NOT NULL',
                       'intptlon TEXT NOT NULL']


def load_puma_shapefile(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, 'PUMA', force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from puma shapefile at {filepath}.')
            puma_shapes.populate(connection, year, records)
