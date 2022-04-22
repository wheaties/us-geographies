from iops.database import ShapeDataTable
from metadata.methods import file_metadata
from parsers.shapefile import parse_file


cbsa_shapes = ShapeDataTable('cbsa')
cbsa_shapes.columns = ['csafp TEXT',
                       'cbsafp TEXT',
                       'geoid TEXT',
                       'name TEXT NOT NULL',
                       'namelsad TEXT',
                       'lsad TEXT',
                       'memi TEXT',
                       'mtfcc TEXT',
                       'aland BIGINT',
                       'awater BIGINT',
                       'intptlat TEXT',
                       'intptlon TEXT']


def load_cbsa_shapefile(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, cbsa_shapes.group, force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from cbsa shapefile at {filepath}.')
            cbsa_shapes.populate(connection, year, records)
