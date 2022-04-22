from iops.database import ShapeDataTable
from metadata.methods import file_metadata
from parsers.shapefile import parse_file


necta_shapes = ShapeDataTable('necta')
necta_shapes.columns = ['centafp TEXT',
                        'geoid TEXT',
                        'name TEXT',
                        'namelsad TEXT',
                        'lsad TEXT',
                        'mtfcc TEXT',
                        'aland BIGINT',
                        'awater BIGINT',
                        'intptlat TEXT',
                        'intptlon TEXT']


def load_necta_shapefile(connection, filepath, year, force=False):
    with file_metadata(connection, filepath, necta_shapes.group, force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from necta shapefile.')
            necta_shapes.populate(records, connection, year)