from iops.database import ShapeDataTable
from metadata.methods import file_metadata, single_file_load
from parsers.shapefile import parse_file


fips_state = ShapeDataTable('fips_state')
fips_state.columns = ['region TEXT NOT NULL',
                      'division TEXT NOT NULL',
                      'statefp TEXT NOT NULL',
                      'statens TEXT',
                      'geoid TEXT NOT NULL',
                      'stusps TEXT NOT NULL',
                      'name TEXT NOT NULL',
                      'lsad TEXT NOT NULL',
                      'mtfcc TEXT NOT NULL',
                      'funcstate TEXT NOT NULL',
                      'aland BIGINT NOT NULL',
                      'awater BIGINT NOT NULL',
                      'intptlat TEXT NOT NULL',
                      'intptlon TEXT NOT NULL']


load_fips_state_shapefile = single_file_load(fips_state, parse_file)

fips_county = ShapeDataTable('fips_county')
fips_county.columns = ['statefp TEXT NOT NULL',
                       'countyfp TEXT NOT NULL',
                       'countyns TEXT NOT NULL',
                       'geoid TEXT NOT NULL',
                       'name TEXT NOT NULL',
                       'namelsad TEXT NOT NULL',
                       'lsad TEXT NOT NULL',
                       'classfp TEXT NOT NULL',
                       'mtfcc TEXT NOT NULL',
                       'csafp TEXT',
                       'cbsafp TEXT',
                       'metdivfp TEXT',
                       'funcstat TEXT NOT NULL',
                       'aland BIGINT NOT NULL',
                       'awater BIGINT NOT NULL',
                       'intptlat TEXT NOT NULL',
                       'intptlon TEXT NOT NULL']


def load_fips_county_shapefile(connection, filepath, year, force=False):
    fips_county.setup(connection, year, force)
    with file_metadata(connection, filepath, fips_county.group, force) as file_loaded:
        if not file_loaded or force:
            records = parse_file(str(filepath))
            print(f'Read {len(records)} records from {fips_county.group} shapefile at {filepath}.')
            fips_county.populate(connection, year, records)
