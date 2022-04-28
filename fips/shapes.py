from iops.database import ShapeDataTable
from metadata.methods import multi_file_load, single_file_load
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

load_fips_county_shapefile = single_file_load(fips_county, parse_file)

fips_county_subdivision = ShapeDataTable('fips_county_subdivision')
fips_county_subdivision.columns = ['statefp TEXT NOT NULL',
                                   'countyfp TEXT NOT NULL',
                                   'cousubfp TEXT NOT NULL',
                                   'cousubns TEXT NOT NULL',
                                   'geoid TEXT NOT NULL',
                                   'name TEXT NOT NULL',
                                   'namelsad TEXT NOT NULL',
                                   'lsad TEXT NOT NULL',
                                   'classfp TEXT NOT NULL',
                                   'mtfcc TEXT NOT NULL',
                                   'cnectafp TEXT',
                                   'nectafp TEXT',
                                   'nctadvfp TEXT',
                                   'funcstat TEXT NOT NULL',
                                   'aland BIGINT NOT NULL',
                                   'awater BIGINT NOT NULL',
                                   'intptlat TEXT NOT NULL',
                                   'intptlon TEXT NOT NULL']

load_fips_county_subdivision_shapefile = multi_file_load(fips_county_subdivision, parse_file)

fips_place = ShapeDataTable('fips_place')
fips_place.columns = ['statefp TEXT NOT NULL',
                      'placefp TEXT NOT NULL',
                      'placens TEXT NOT NULL',
                      'geoid TEXT NOT NULL',
                      'name TEXT NOT NULL',
                      'namelsad TEXT NOT NULL',
                      'lsad TEXT NOT NULL',
                      'classfp TEXT NOT NULL',
                      'pcicbsa TEXT',
                      'pcinecta TEXT',
                      'mtfcc TEXT NOT NULL',
                      'funcstat TEXT NOT NULL',
                      'aland BIGINT NOT NULL',
                      'awater BIGINT NOT NULL',
                      'intptlat TEXT NOT NULL',
                      'intptlon TEXT NOT NULL']

load_fips_place_shapefile = multi_file_load(fips_place, parse_file)

fips_city = ShapeDataTable('fips_city')
fips_city.columns = ['statepf TEXT NOT NULL',
                     'conctyfp TEXT NOT NULL',
                     'conctyns TEXT NOT NULL',
                     'geoid TEXT NOT NULL',
                     'name TEXT NOT NULL',
                     'namelsad TEXT NOT NULL',
                     'lsad TEXT NOT NULL',
                     'classfp TEXT NOT NULL',
                     'mtfcc TEXT NOT NULL',
                     'funcstat TEXT NOT NULL',
                     'aland BIGINT NOT NULL',
                     'awater BIGINT NOT NULL',
                     'intptlat TEXT NOT NULL',
                     'intptlon TEXT NOT NULL']

load_fips_city_shapefile = multi_file_load(fips_city, parse_file)
