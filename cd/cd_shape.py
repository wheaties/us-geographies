from iops.database import ShapeDataTable
from metadata.methods import file_metadata
from parsers.shapefile import parse_file


cd_shapes = ShapeDataTable('cd')
cd_shapes.columns = ['statefp TEXT NOT NULL',
                     'cd TEXT NOT NULL',
                     'geoid TEXT NOT NULL',
                     'NAMELSAD TEXT NOT NULL',
                     'LSAD TEXT NOT NULL',
                     'CDSESSN TEXT NOT NULL',
                     'MTFCC TEXT NOT NULL',
                     'FUNCSTAT TEXT NOT NULL',
                     'ALAND BIGINT',
                     'AWATER BIGINT',
                     'INTPTLAT TEXT NOT NULL',
                     'INTPTLON TEXT NOT NULL']


def load_cd_shapefile(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, 'CD', force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from cd shapefile at {filepath}.')
            cd_shapes.populate(connection, year, records)
