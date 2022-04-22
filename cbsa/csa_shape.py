from iops.database import ShapeDataTable
from metadata.methods import file_metadata
from parsers.shapefile import parse_file


csa_shapes = ShapeDataTable('csa', 'cbsa')
csa_shapes.columns = ['csafp TEXT',
                      'geoid TEXT',
                      'name TEXT NOT NULL',
                      'namelsad TEXT',
                      'lsad TEXT',
                      'mtfcc TEXT',
                      'aland BIGINT',
                      'awater BIGINT',
                      'intptlat TEXT',
                      'intptlon TEXT']


def load_csa_shapefile(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, csa_shapes.group, force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from csa shapefile.')
            csa_shapes.populate(connection, year, records)